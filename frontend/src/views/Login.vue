<template>
	<div class="min-h-screen bg-[#EDE8E5] relative overflow-hidden">
		<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col lg:flex-row min-h-screen">
			<!-- Login Form Section -->
			<div class="w-full lg:w-1/2 flex items-center justify-center lg:justify-start relative z-10 py-12 lg:py-0">
				<div class="w-full max-w-md bg-white rounded-lg shadow-md p-8">
					<h2 class="text-center font-semibold font-sans text-[#212529] mb-10 sm:mb-2">
						Welcome to British Asian Trust Portal
					</h2>
					<p class="text-center text-[#212529] mb-6">
						Login to access your dashboard, complete surveys, earn points, and get personalized
						recommendations to support your wellness.
					</p>
					<form @submit.prevent="login" class="space-y-4">
						<div>
							<label for="email" class="block mb-1">Email</label>
							<input type="email" id="email" v-model="email" @input="validateField('email')"
								class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
								placeholder="Enter your email address">
							<p v-if="errors.email" class="text-red-500 text-sm mt-1">{{ errors.email }}</p>
						</div>
						<div>
							<label for="password" class="block mb-1">Password</label>
							<input type="password" id="password" v-model="password" @input="validateField('password')"
								class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
								placeholder="Enter your password">
							<p v-if="errors.password" class="text-red-500 text-sm mt-1">{{ errors.password }}</p>
						</div>
						<div class="flex justify-end">
							<router-link :to="{ name: 'Forgot' }"
								class="text-sm text-gray-600 hover:text-gray-900">Forgot
								Password?</router-link>
						</div>
						<div>
							<button type="submit" :disabled="!isFormValid"
								class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#CA2247] hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 disabled:opacity-50 disabled:cursor-not-allowed">
								LOGIN
							</button>
						</div>
					</form>
					<div class="mt-4 space-y-3">
						<a href="https://accounts.google.com/o/oauth2/auth?redirect_uri=https%3A%2F%2Fbtasian.suvaidyam.com%2Fapi%2Fmethod%2Ffrappe.integrations.oauth2_logins.login_via_google&state=eyJzaXRlIjogImh0dHA6Ly9idGFzaWFuLnN1dmFpZHlhbS5jb20iLCAidG9rZW4iOiAiMjg1YjVhYmQ1YTY2Y2RiNGU3NTZkZmFmNmZiNWNhODc0ZDI3ZTY4M2U3NzU4NTQwZTgwMmRmZjkiLCAicmVkaXJlY3RfdG8iOiAiL2FwcC9idWlsZCJ9&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&response_type=code&client_id=720319117261-1kuhqoutuq2j8ud0b8dsp1oen4glmruq.apps.googleusercontent.com"
							class="w-full flex justify-center items-center py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
							<svg class="w-5 h-5 mr-2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
								<path
									d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
									fill="#4285F4" />
								<path
									d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
									fill="#34A853" />
								<path
									d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
									fill="#FBBC05" />
								<path
									d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
									fill="#EA4335" />
							</svg>
							Login with Google

						</a>
						<a href="https://login.microsoftonline.com/common/oauth2/v2.0/authorize?redirect_uri=https%3A%2F%2Fbtasian.suvaidyam.com%2Fapi%2Fmethod%2Ffrappe.integrations.oauth2_logins.login_via_office365&state=eyJzaXRlIjogImh0dHA6Ly9idGFzaWFuLnN1dmFpZHlhbS5jb20iLCAidG9rZW4iOiAiZWI2Y2I3ZTVkZDY0N2QwMDVjNzQ5Y2Q3NDc2N2U4OTM3YmJkYmYwZTc5MWQyMGQ1NDUwMjkwYWYiLCAicmVkaXJlY3RfdG8iOiAiL2FwcC9idWlsZCJ9&response_type=code&scope=openid+email+profile&client_id=c28ed05b-846a-414e-b8df-bbb602316b22"
							class="w-full flex justify-center items-center py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
							<svg class="w-5 h-5 mr-2" viewBox="0 0 23 23" xmlns="http://www.w3.org/2000/svg">
								<path fill="#f3f3f3" d="M0 0h23v23H0z" />
								<path fill="#f35325" d="M1 1h10v10H1z" />
								<path fill="#81bc06" d="M12 1h10v10H12z" />
								<path fill="#05a6f0" d="M1 12h10v10H1z" />
								<path fill="#ffba08" d="M12 12h10v10H12z" />
							</svg>
							Login with Microsoft

						</a>
					</div>
				</div>
			</div>

			<!-- Image Section -->
			<div class="hidden lg:block lg:w-1/2 relative">
				<svg class="absolute right-0 bottom-0 w-[300px] h-[300px] lg:w-[700px] lg:h-[600px]"
					viewBox="0 0 719 681" fill="none" xmlns="http://www.w3.org/2000/svg">
					<path fill-rule="evenodd" clip-rule="evenodd"
						d="M10.6721 358.09C43.7944 290.528 148.486 299.88 203.921 248.991C237.118 218.516 233.243 164.646 260.492 128.755C298.361 78.8762 330.329 2.09349 392.93 0.0381908C454.772 -1.99227 485.461 77.4593 530.486 119.891C565.441 152.832 598.797 184.384 628.553 222.085C662.81 265.488 725.275 303.219 718.489 358.09C711.449 415.017 625.945 426.357 597.155 475.972C568.46 525.423 606.218 613.235 555.318 639.29C503.188 665.974 451.086 573.596 392.93 580.511C321.677 588.984 278.12 686.509 206.596 680.755C139.575 675.363 89.6252 610.766 54.7335 553.303C19.5091 495.292 -19.2021 419.028 10.6721 358.09Z"
						fill="#DBB729" />
				</svg>
				<img src="../../public/login_banner.png" alt="Two women in traditional attire"
					class="absolute inset-0 w-full h-full object-cover">
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { inject } from 'vue'
import { useToast } from 'vue-toastification'
// import { auth, googleProvider, signInWithPopup } from '../../firebase.js'

const email = ref('')
const password = ref('')
const redirect_route = ref(null)
const errors = reactive({
	email: '',
	password: ''
})

const $auth = inject('$auth')
const router = useRouter()
const route = useRoute()
const toast = useToast()

const validateEmail = (value) => {
	const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
	return emailRegex.test(value)
}

const validateField = (field) => {
	errors[field] = ''
	switch (field) {
		case 'email':
			if (!email.value) errors.email = 'Email is required'
			else if (!validateEmail(email.value)) errors.email = 'Invalid email format'
			break
		case 'password':
			if (!password.value) errors.password = 'Password is required'
			else if (password.value.length < 6) errors.password = 'Password must be at least 6 characters long'
			break
	}
}

const isFormValid = computed(() => {
	return email.value && password.value && !errors.email && !errors.password
})

const login = async () => {
	validateField('email')
	validateField('password')

	if (isFormValid.value) {
		try {
			let res = await $auth.login(email.value, password.value)
			if (res) {
				toast.success("Login successful!", {
					position: "top-right",
					timeout: 5000,
					closeOnClick: true,
					pauseOnFocusLoss: true,
					pauseOnHover: true,
					draggable: true,
					draggablePercent: 0.6,
					showCloseButtonOnHover: false,
					hideProgressBar: true,
					closeButton: "button",
					icon: true,
					rtl: false
				})
				router.push({ name: 'Home' })
			}
		} catch (error) {
			toast.error("Login failed. Please check your credentials and try again.", {
				position: "top-right",
				timeout: 5000,
				closeOnClick: true,
				pauseOnFocusLoss: true,
				pauseOnHover: true,
				draggable: true,
				draggablePercent: 0.6,
				showCloseButtonOnHover: false,
				hideProgressBar: true,
				closeButton: "button",
				icon: true,
				rtl: false
			})
		}
	}
}

// const loginWithGoogle = async () => {
// 	try {
// 		const result = await signInWithPopup(auth, googleProvider)
// 		console.log(user,"user");
// 		const user = result.user
// 		toast.success(`Welcome ${user.displayName}!`, {
// 			position: "top-right",
// 			timeout: 5000,
// 			closeOnClick: true,
// 			pauseOnFocusLoss: true,
// 			pauseOnHover: true,
// 			draggable: true,
// 			draggablePercent: 0.6,
// 			hideProgressBar: true,
// 			closeButton: "button",
// 			icon: true
// 		});
// 		router.push({ name: 'Home' });
// 	} catch (error) {
// 		toast.error("Google login failed. Please try again.", {
// 			position: "top-right",
// 			timeout: 5000,
// 			closeOnClick: true,
// 			pauseOnFocusLoss: true,
// 			pauseOnHover: true,
// 			draggable: true,
// 			draggablePercent: 0.6,
// 			hideProgressBar: true,
// 			closeButton: "button",
// 			icon: true
// 		});
// 	}
// }

// const loginWithMicrosoft = () => {


// }

// Check for redirect route on component mount
if (route.query.route) {
	redirect_route.value = route.query.route
	router.replace({ query: null })
}
</script>