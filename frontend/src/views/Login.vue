<template>
	<div class="min-h-screen bg-white">
	  <div class="max-w-[1920px] mx-auto relative">
		<NavBar />
		
		<div class="relative flex flex-col lg:flex-row justify-center min-h-screen bg-gray-100">
		  <!-- Image Section -->
		  <div class="lg:w-1/2 h-64 lg:h-auto">
			<img src="/login1.png" alt="Family using laptop" class="object-cover w-full h-full" />
		  </div>
		  <!-- Login Form Section -->
		  <div class="lg:w-1/2 p-4 sm:p-8 flex flex-col justify-center items-center bg-white shadow-xl">
			<div class="w-full max-w-lg">
			  <h1 class="font-poppins text-[24px] font-semibold leading-[28px] lg:text-[34px] lg:leading-[37.4px] text-[#0D4688] mb-4 sm:mb-6 text-center">
				Welcome to Outcome Readiness
			  </h1>
			  <p class="font-poppins text-[14px] font-normal leading-[18.34px] tracking-[0.0025em] text-[#2F2F2F] lg:text-[14px] lg:leading-[18.34px] mb-6 sm:mb-8 text-center">
				Login to empower your organization and gain access to surveys, personalized recommendations,
				and tools to drive impact.
			  </p>
			  <form @submit.prevent="handleSubmit" class="space-y-4">
				<div>
				  <label for="email" class="sr-only">Email ID</label>
				  <input id="email" v-model="email" type="email" required
					class="w-full px-4 h-12 border border-gray-300 rounded-md font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#2F2F2F] focus:outline-none focus:ring-2 focus:ring-[#0D4688] focus:border-[#0D4688]"
					placeholder="Email ID" @input="validateField('email')" />
				  <p v-if="errors.email" class="text-red-500 text-xs sm:text-sm mt-1">{{ errors.email }}</p>
				</div>
				<div class="relative">
				  <label for="password" class="sr-only">Password</label>
				  <input id="password" v-model="password" :type="showPassword ? 'text' : 'password'" required
					class="w-full px-4 h-12 border border-gray-300 rounded-md font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#2F2F2F] focus:outline-none focus:ring-2 focus:ring-[#0D4688] focus:border-[#0D4688]"
					placeholder="Password" @input="validateField('password')" />
				  <button type="button" @click="togglePassword"
					class="absolute inset-y-0 right-0 pr-3 flex items-center"
					aria-label="Toggle password visibility">
					<svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"
					  xmlns="http://www.w3.org/2000/svg">
					  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
						d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
					  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
						d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z">
					  </path>
					</svg>
				  </button>
				  <p v-if="errors.password" class="text-red-500 text-xs sm:text-sm mt-1">{{ errors.password }}</p>
				</div>
				<div class="flex justify-end mb-2">
				  <router-link to="/forgot"
					class="font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#0D4688] hover:underline">
					Forgot Password?
				  </router-link>
				</div>
				<button type="submit" :disabled="!isFormValid || isLoading"
				  class="w-full bg-orange-500 text-white h-12 px-4 rounded-full hover:bg-orange-600 transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] flex items-center justify-center">
				  <span v-if="!isLoading">LOGIN</span>
				  <span v-else class="flex items-center">
					<LoaderIcon class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" />
					Processing...
				  </span>
				</button>
			  </form>
			  <div class="mt-4 text-center">
				<router-link to="/register"
				  class="font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#0D4688] hover:underline">
				  Don't have an account? Sign up
				</router-link>
			  </div>
			  <div class="mt-6 flex items-center">
				<div class="flex-grow border-t border-gray-300"></div>
				<span class="flex-shrink mx-4 text-gray-600 font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left">OR</span>
				<div class="flex-grow border-t border-gray-300"></div>
			  </div>
			  <div class="mt-6 space-y-2">
				<button @click="handleGoogleLogin"
				  class="w-full border border-gray-300 text-gray-700 h-12 px-4 rounded-full hover:bg-gray-50 transition duration-300 flex items-center justify-center font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left">
				  <svg class="h-5 w-5 mr-2" viewBox="0 0 24 24">
					<path fill="#4285F4"
					  d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
					<path fill="#34A853"
					  d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
					<path fill="#FBBC05"
					  d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" />
					<path fill="#EA4335"
					  d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
					<path fill="none" d="M1 1h22v22H1z" />
				  </svg>
				  Continue with Google
				</button>
				<button @click="handleMicrosoftLogin"
				  class="w-full border border-gray-300 text-gray-700 h-12 px-4 rounded-full hover:bg-gray-50 transition duration-300 flex items-center justify-center font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left">
				  <svg class="h-5 w-5 mr-2" viewBox="0 0 23 23">
					<path fill="#f3f3f3" d="M0 0h23v23H0z" />
					<path fill="#f35325" d="M1 1h10v10H1z" />
					<path fill="#81bc06" d="M12 1h10v10H12z" />
					<path fill="#05a6f0" d="M1 12h10v10H1z" />
					<path fill="#ffba08" d="M12 12h10v10H12z" />
				  </svg>
				  Continue with Microsoft
				</button>
			  </div>
			</div>
		  </div>
		</div>
	  </div>
	</div>
  </template>
  
  <script setup>
  import { ref, reactive, computed } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import { inject } from 'vue'
  import { useToast } from 'vue-toastification'
  import { LoaderIcon } from 'lucide-vue-next'
  import NavBar from '../components/NavBar.vue'
  
  const email = ref('')
  const password = ref('')
  const showPassword = ref(false)
  const redirect_route = ref(null)
  const isLoading = ref(false)
  const errors = reactive({
	email: '',
	password: ''
  })
  
  const $auth = inject('$auth')
  const router = useRouter()
  const route = useRoute()
  const toast = useToast()
  
  const googleAuthUrl = "https://accounts.google.com/o/oauth2/auth?redirect_uri=https%3A%2F%2Fbtasian.suvaidyam.com%2Fapi%2Fmethod%2Fbritish_asian_trust.api.my_login_via_google&state=eyJzaXRlIjogImh0dHA6Ly9idGFzaWFuLnN1dmFpZHlhbS5jb20iLCAidG9rZW4iOiAiMjg1YjVhYmQ1YTY2Y2RiNGU3NTZkZmFmNmZiNWNhODc0ZDI3ZTY4M2U3NzU4NTQwZTgwMmRmZjkiLCAicmVkaXJlY3RfdG8iOiAiL2FwcC9idWlsZCJ9&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&response_type=code&client_id=720319117261-1kuhqoutuq2j8ud0b8dsp1oen4glmruq.apps.googleusercontent.com"
  
  const microsoftAuthUrl = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?redirect_uri=https%3a%2f%2fbtasian.suvaidyam.com%2fapi%2fmethod%2fbritish_asian_trust.api.my_login_via_office_365&state=eyJzaXRlIjogImh0dHA6Ly9idGFzaWFuLnN1dmFpZHlhbS5jb20iLCAidG9rZW4iOiAiYTIwNTJlY2YzODIzMDI5NTQ2NThjMjY2ZDliOGI3ZWYwYTAwYjJhMjYxODFjYzQ0YmFkNjQ1YjMiLCAicmVkaXJlY3RfdG8iOiAiL2FwcCJ9&response_type=code&scope=openid+email+profile&client_id=c28ed05b-846a-414e-b8df-bbb602316b22&sso_nonce=AwABEgEAAAADAOz_BQD0_6Ar8NwBdlHYKzVYmVX60SYWmU33iETSyQ_ougU6j_1JG37adzZ-SO-HreW8x9QnR79ZfuhZMek433986gCjxYcgAA&client-request-id=bceba0a3-5344-4ea6-a171-a8c06b638a9a&mscrid=bceba0a3-5344-4ea6-a171-a8c06b638a9a"
  
  const blockedDomains = [
	'gmail.com',
	'outlook.com',
	'hotmail.com',
	'yahoo.com',
	'aol.com',
	'mail.com',
	'protonmail.com',
	'icloud.com'
  ]
  
  const validateEmail = (value) => {
	const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
	if (!emailRegex.test(value)) return false
  
	const domain = value.split('@')[1].toLowerCase()
	return !blockedDomains.includes(domain)
  }
  
  const validateField = (field) => {
	errors[field] = ''
	switch (field) {
	  case 'email':
		if (!email.value) {
		  errors.email = 'Email is required'
		} else if (!validateEmail(email.value)) {
		  if (email.value.includes('@')) {
			const domain = email.value.split('@')[1].toLowerCase()
			if (blockedDomains.includes(domain)) {
			  errors.email = 'Please use your business email address'
			} else {
			  errors.email = 'Invalid email format'
			}
		  } else {
			errors.email = 'Invalid email format'
		  }
		}
		break
	  case 'password':
		if (!password.value) {
		  errors.password = 'Password is required'
		} else if (password.value.length < 6) {
		  errors.password = 'Password must be at least 6 characters long'
		}
		break
	}
  }
  
  const isFormValid = computed(() => {
	
	return email.value && password.value && !errors.email && !errors.password
  })
  
  const handleSubmit = async () => {
	validateField('email')
	validateField('password')
  
	if (isFormValid.value) {
	  try {
		isLoading.value = true
		let res = await $auth.login(email.value, password.value)
  
		if (res) {
		  toast.success("Login successful!", {
			position: "top-right",
			timeout: 5000,
		  })
		  router.push(redirect_route.value || { name: 'Home' })
		}
	  } catch (error) {
		toast.error("Login failed. Please check your credentials and try again.", {
		  position: "top-right",
		  timeout: 5000,
		})
	  } finally {
		isLoading.value = false
	  }
	}
  }
  
  const togglePassword = () => {
	showPassword.value = !showPassword.value
  }
  
  const handleGoogleLogin = () => {
	window.location.href = googleAuthUrl
  }
  
  const handleMicrosoftLogin = () => {
	window.location.href = microsoftAuthUrl
  }
  
  // Check for redirect route on component mount
  if (route.query.route) {
	redirect_route.value = route.query.route
	router.replace({ query: null })
  }
  </script>