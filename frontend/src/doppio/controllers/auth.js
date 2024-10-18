import call from './call';

export default class Auth {
	constructor() {
		this.isLoggedIn = false;
		this.user = null;
		this.user_image = null;
		this.cookie = null;

		this.cookie = Object.fromEntries(
			document.cookie
				.split('; ')
				.map((part) => part.split('='))
				.map((d) => [d[0], decodeURIComponent(d[1])])
		);

		this.isLoggedIn = this.cookie.user_id && this.cookie.user_id !== 'Guest';
	}

	async login(email, password) {
		let res = await call('login', {
			usr: email,
			pwd: password,
		});
		if (res) {
			this.isLoggedIn = true;
			this.user = await this.getUser(email);
			this.cookie = {... this.user};
			sessionStorage.setItem('user', JSON.stringify(this.user));
			return res;
		}
		return false;
	}

	async logout() {
		await call('logout');
		this.isLoggedIn = false;
		sessionStorage.removeItem('user');
		window.location.reload();
	}

	async resetPassword(email) {
		console.log('resetting password');
		// Implement if you want
	}

	async getUser( userId ) {
		const result = await call('british_asian_trust.api.get_user', {	userId: userId });
		return result;
	}

	async getUsers() {
		const usr= sessionStorage.getItem('user');
		return usr;
	}


}
