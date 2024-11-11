<template>
  <div class="flex justify-center min-h-screen bg-gray-100 p-4 sm:p-0">
    <div class="w-full max-w-[1512px] flex flex-col lg:flex-row shadow-2xl">
      <!-- Image Section -->
      <div class="lg:w-1/2 h-64 lg:h-auto relative">
        <img src="/login1.png" alt="Two women in traditional attire" class="object-cover w-full h-full" />
      </div>
      <!-- Update Password Form Section -->
      <div class="lg:w-1/2 p-4 sm:p-8 flex flex-col justify-center items-center bg-white">
        <div class="w-full max-w-lg">
          <h2
            class="font-poppins text-[24px] font-semibold leading-[28px] lg:text-[34px] lg:leading-[37.4px] text-[#0D4688] mb-4 sm:mb-6 text-center">
            Set Password
          </h2>
          <!-- <p class="font-poppins text-[14px] font-normal leading-[18.34px] tracking-[0.0025em] text-[#2F2F2F] lg:text-[14px] lg:leading-[18.34px] mb-6 sm:mb-8 text-center">
              Please enter your new password below.
            </p> -->
          <form @submit.prevent="updatePassword" class="space-y-4">
            <div>
              <label for="password" class="sr-only">Create Password</label>
              <div class="relative">
                <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password"
                  class="w-full px-4 h-12 pl-10 border border-gray-300 rounded-md font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#2F2F2F] focus:outline-none focus:ring-2 focus:ring-[#0D4688] focus:border-[#0D4688]"
                  placeholder="Create password" />
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <LockIcon class="h-5 w-5 text-gray-400" />
                </div>
                <button type="button" @click="togglePasswordVisibility('password')"
                  class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm leading-5">
                  <EyeIcon v-if="!showPassword" class="h-5 w-5 text-gray-400" />
                  <EyeOffIcon v-else class="h-5 w-5 text-gray-400" />
                </button>
              </div>
            </div>
            <div>
              <label for="confirmPassword" class="sr-only">Confirm Password</label>
              <div class="relative">
                <input :type="showConfirmPassword ? 'text' : 'password'" id="confirmPassword" v-model="confirmPassword"
                  class="w-full px-4 h-12 pl-10 border border-gray-300 rounded-md font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#2F2F2F] focus:outline-none focus:ring-2 focus:ring-[#0D4688] focus:border-[#0D4688]"
                  placeholder="Confirm Password" />
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <LockIcon class="h-5 w-5 text-gray-400" />
                </div>
                <button type="button" @click="togglePasswordVisibility('confirmPassword')"
                  class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm leading-5">
                  <EyeIcon v-if="!showConfirmPassword" class="h-5 w-5 text-gray-400" />
                  <EyeOffIcon v-else class="h-5 w-5 text-gray-400" />
                </button>
              </div>
            </div>
            <p v-if="error" class="text-red-500 text-xs sm:text-sm mt-1">{{ error }}</p>
            <button type="submit" :disabled="!isFormValid || isLoading"
              class="w-full bg-orange-500 text-white h-12 px-4 rounded-full hover:bg-orange-600 transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] flex items-center justify-center">
              <span v-if="!isLoading">SUBMIT</span>
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
import { ref, computed, onMounted, inject } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { LockIcon, EyeIcon, EyeOffIcon, LoaderIcon } from 'lucide-vue-next'

const router = useRouter()
const toast = useToast()

const password = ref('')
const call = inject('$call')
const confirmPassword = ref('')
const showPassword = ref(false)
const showConfirmPassword = ref(false)
const error = ref('')
const isLoading = ref(false)
const key = ref('')

onMounted(() => {
  key.value = router.currentRoute.value.query.key
})

const togglePasswordVisibility = (field) => {
  if (field === 'password') {
    showPassword.value = !showPassword.value
  } else if (field === 'confirmPassword') {
    showConfirmPassword.value = !showConfirmPassword.value
  }
}

const isFormValid = computed(() => {
  return password.value && confirmPassword.value && password.value === confirmPassword.value
})

const updatePassword = async () => {
  if (isFormValid.value) {
    try {
      isLoading.value = true
      error.value = ''
      // Ensure key is defined
      if (key.value) {
        const response = await call('frappe.core.doctype.user.user.update_password', {
          "key": key.value,
          "new_password": password.value,
          "confirm_password": confirmPassword.value,
          "logout_all_sessions": 1
        })
        if (response === '/app') {
          toast.success("Password updated successfully!", {
            position: "top-right",
            timeout: 3000
          })
          setTimeout(() => {
            router.push('/login')
          }, 3000)
        } 
      } else {
        error.value = "Invalid key. Please check the URL."
      }
    } catch (err) {
      console.error('Failed to update password:', err)
      error.value = "Failed to update password. Please try again."
    } finally {
      isLoading.value = false
    }
  } else {
    error.value = "Passwords do not match or are empty."
  }
}
</script>
