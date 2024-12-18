// Author: Gavin D'souza <gavin@frappe.io>

import router from '@/router';
import { useToast } from 'vue-toastification'
const toast = useToast()

export default async function call(method, args) {
	if (!args) {
		args = {};
	}

	let headers = {
		Accept: 'application/json',
		'Content-Type': 'application/json; charset=utf-8',
		'X-Frappe-Site-Name': window.location.hostname
	};

	if (window.csrf_token && window.csrf_token !== '{{ csrf_token }}') {
		headers['X-Frappe-CSRF-Token'] = window.csrf_token;
	}

	updateState(this, 'RequestStarted', null);

	const res = await fetch(`/api/method/${method}`, {
		method: 'POST',
		headers,
		body: JSON.stringify(args)
	});

	if (res.ok) {
		updateState(this, null, null);
		const data = await res.json();
		if (data.docs || method === 'login') {
			return data;
		}
		if(data.code == 'SUC_200'){
			return data;
		}else{
		return data.message;
		}
	} else {
		const status_code = ['ERR_001', 'ERR_002', 'ERR_003', 'ERR_004','ERR_005','ERR_006','ERR_007'];
		let response = await res.text();
		let error, exception;
		try {
			error = JSON.parse(response);
			if (status_code.includes(error.code)) {
				toast.error(error.message, { position: "top-right", timeout: 3000 });
			}
			// eslint-disable-next-line no-empty
		} catch (e) {}
		let errorParts = [
			[method, error.exc_type, error._error_message].filter(Boolean).join(' ')
		];
		if (error.exc) {
			exception = error.exc;
			try {
				exception = JSON.parse(exception)[0];
				// eslint-disable-next-line no-empty
			} catch (e) {}
			errorParts.push(exception);
		}
		let e = new Error(errorParts.join('\n'));
		e.exc_type = error.exc_type;
		e.exc = exception;
		e.messages = error._server_messages
			? JSON.parse(error._server_messages)
			: [];
		e.messages = e.messages.concat(error.message);
		e.messages = e.messages.map(m => {
			try {
				return JSON.parse(m).message;
			} catch (error) {
				return m;
			}
		});
		e.messages = e.messages.filter(Boolean);
		if (!e.messages.length) {
			e.messages = error._error_message ? [error._error_message] : ['Internal Server Error'];
		}
		updateState(this, null, e.messages.join('\n'));

		if (
			[401, 403].includes(res.status) &&
			router.currentRoute.name !== 'Login'
		) {
			router.push('/login');
		}
		throw e;
	}

	function updateState(vm, state, errorMessage) {
		if (vm?.state !== undefined) {
			vm.state = state;
		}
		if (vm?.errorMessage !== undefined) {
			vm.errorMessage = errorMessage;
		}
	}
}
