<template>
    <div class="min-h-screen bg-[#EDE8E5] relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col lg:flex-row min-h-screen">
            <!-- Forgot Password Form Section -->
            <div class="w-full lg:w-1/2 flex items-center justify-center lg:justify-start relative z-10 py-12 lg:py-0">
                <div class="w-full max-w-md bg-white rounded-lg shadow-md p-8">
                    <h2 class="text-center font-semibold font-sans text-[#212529] mb-2">
                        Forgot Password
                    </h2>
                    <p class="text-center text-[#212529] mb-6">
                        Enter your email address and we'll send you instructions to reset your password.
                    </p>
                    <form @submit.prevent="resetPassword" class="space-y-4">
                        <div>
                            <label for="email" class="block mb-1">Email Address</label>
                            <div class="relative">
                                <input type="email" id="email" v-model="email" @input="validateEmail"
                                    class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 pl-10 pr-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                                    placeholder="Enter your email address">
                                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                        <path
                                            d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
                                        <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
                                    </svg>
                                </div>
                            </div>
                            <p v-if="error" class="text-red-500 text-sm mt-1">{{ error }}</p>
                        </div>
                        <div>
                            <button type="submit" :disabled="!isEmailValid"
                                class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#CA2247] hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 disabled:opacity-50 disabled:cursor-not-allowed">
                                Reset Password
                            </button>
                        </div>
                    </form>
                    <div class="mt-4 text-center">
                        <router-link to="/login" class="text-sm text-gray-600 hover:text-gray-900">Back to
                            Login</router-link>
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
import { ref, computed, inject } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'

const email = ref('')
const error = ref('')
const router = useRouter()
const toast = useToast()
const call = inject('$call')

const validateEmail = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!email.value) {
        error.value = 'Email is required'
    } else if (!emailRegex.test(email.value)) {
        error.value = 'Invalid email format'
    } else {
        error.value = ''
    }
}

const isEmailValid = computed(() => {
    return email.value && !error.value
})

const resetPassword = async () => {
    if (isEmailValid.value) {
        try {
            const res = await fetch('/api/method/frappe.core.doctype.user.user.reset_password', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    user: email.value
                })
            })
            console.log(res,"res");
            toast.success("Password reset instructions sent to your email.", {
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
            // Redirect to login page after successful password reset request
            router.push('/login')
        } catch (error) {
            toast.error("Failed to send password reset instructions. Please try again.", {
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
</script>