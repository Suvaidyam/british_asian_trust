<template>
  <div class="flex justify-center min-h-screen bg-gray-100 p-4 sm:p-0">
    <div class="w-full max-w-[1512px] flex flex-col lg:flex-row shadow-2xl">
      <!-- Image Section -->
      <div class="lg:w-1/2 h-64 lg:h-auto relative">
        <img src="/login1.png" alt="Two women in traditional attire" class="object-cover w-full h-full" />
      </div>
      <!-- Forgot Password Form Section -->
      <div class="lg:w-1/2 p-4 sm:p-8 flex flex-col justify-center items-center bg-white">
        <div class="w-full max-w-lg">
          <h2 class="font-poppins text-[24px] font-semibold leading-[28px] lg:text-[34px] lg:leading-[37.4px] text-[#0D4688] mb-4 sm:mb-6 text-center">
            Forgot Password
          </h2>
          <p class="font-poppins text-[14px] font-normal leading-[18.34px] tracking-[0.0025em] text-[#2F2F2F] lg:text-[14px] lg:leading-[18.34px] mb-6 sm:mb-8 text-center">
            Enter your email address and we'll send you instructions to reset your password.
          </p>
          <form @submit.prevent="resetPassword" class="space-y-4">
            <div>
              <label for="email" class="block mb-1 font-poppins text-[14px] font-normal leading-[18.34px] text-[#2F2F2F]">Email Address</label>
              <div class="relative">
                <input
                  type="email"
                  id="email"
                  v-model="email"
                  @input="validateEmail"
                  class="w-full px-4 h-12 pl-10 border border-gray-300 rounded-md font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#2F2F2F] focus:outline-none focus:ring-2 focus:ring-[#0D4688] focus:border-[#0D4688]"
                  placeholder="Enter your email address"
                />
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <MailIcon class="h-5 w-5 text-gray-400" />
                </div>
              </div>
              <p v-if="error" class="text-red-500 text-xs sm:text-sm mt-1">{{ error }}</p>
            </div>
            <button
              type="submit"
              :disabled="!isEmailValid || isLoading"
              class="w-full bg-orange-500 text-white h-12 px-4 rounded-full hover:bg-orange-600 transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] flex items-center justify-center"
            >
              <span v-if="!isLoading">Reset Password</span>
              <span v-else class="flex items-center">
                <LoaderIcon class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" />
                Processing...
              </span>
            </button>
          </form>
          <div class="mt-4 text-center">
            <router-link to="/login" class="font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#0D4688] hover:underline">
              Back to Login
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { MailIcon, LoaderIcon } from 'lucide-vue-next'

const email = ref('')
const error = ref('')
const isLoading = ref(false)
const router = useRouter()
const toast = useToast()

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

const validateEmail = () => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!email.value) {
    error.value = 'Email is required'
  } else if (!emailRegex.test(email.value)) {
    error.value = 'Invalid email format'
  } else {
    const domain = email.value.split('@')[1].toLowerCase()
    if (blockedDomains.includes(domain)) {
      error.value = 'Please use your business email address'
    } else {
      error.value = ''
    }
  }
}

const isEmailValid = computed(() => {
  return email.value && !error.value
})

const resetPassword = async () => {
  if (isEmailValid.value) {
    try {
      isLoading.value = true
      const res = await fetch('/api/method/frappe.core.doctype.user.user.reset_password', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          user: email.value
        })
      })
      
      if (res.ok) {
        toast.success("Password reset instructions sent to your email.", {
          position: "top-right",
          timeout: 5000,
         
        })
        router.push('/login')
      } else {
        throw new Error('Failed to reset password')
      }
    } catch (error) {
      toast.error("Failed to send password reset instructions. Please try again.", {
        position: "top-right",
        timeout: 5000,
       
      })
    } finally {
      isLoading.value = false
    }
  }
}
</script>

