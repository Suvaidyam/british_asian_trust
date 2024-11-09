<template>
  <div class="relative max-w-[1920px]  mx-auto">
    <!-- Fixed Navigation Bar -->
    <nav class="z-50 w-full">
      <div class="max-w-[1920px]  mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16 sm:h-18 lg:h-20">
          <div class="flex items-center">
            <img src="/logo.png" alt="ISDM Logo" class="h-8 sm:h-10 lg:h-12 w-auto" />
          </div>

          <!-- Desktop Navigation -->
          <div class="hidden md:flex items-center space-x-4">
            <div class="flex flex-col items-center">
              <button @click="toggleNavigation" class="text-[#0D4688] hover:text-[#0D4688] focus:outline-none">
                <span class="sr-only">Toggle navigation</span>
                <svg class="h-6 w-6 sm:h-7 sm:w-7 lg:h-8 lg:w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path v-if="!isNavigationOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M4 6h16M4 12h16m-7 6h7" />
                  <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
              <span
                class="text-[#0D4688] font-poppins text-[10px] sm:text-[11px] lg:text-[12px] font-bold leading-tight tracking-[0.004em] mb-1">MENU</span>
            </div>

            <template v-if="!$auth?.isLoggedIn && currentRoute == '/'">
              <button @click="$router.push({ name: 'Login' })"
                class="px-4 sm:px-5 lg:px-6 py-2 sm:py-2.5 lg:py-3 font-poppins text-[12px] sm:text-[13px] lg:text-[14px] font-semibold leading-tight tracking-[0.0125em] text-white bg-[#FF8A00] hover:bg-[#FF8A00] rounded-full transition-colors duration-200 w-32 sm:w-36 lg:w-40">
                Login
              </button>
            </template>
            <template v-if="$auth?.isLoggedIn">
              <div class="relative">
                <button @click="toggleUserMenu"
                  class="flex items-center text-gray-600 hover:text-gray-800 focus:outline-none">
                  <span class="text-[12px] sm:text-[13px] lg:text-[14px] text-gray-700">{{ $auth?.cookie?.full_name }}</span>
                </button>
                <div v-if="isUserMenuOpen"
                  class="absolute right-0 mt-2 w-40 sm:w-44 lg:w-48 bg-white border border-gray-300 rounded-md shadow-lg z-50">
                  <a href="#" @click.prevent="openChangePasswordModal"
                    class="block px-4 py-2 text-[12px] sm:text-[13px] lg:text-[14px] text-gray-700 hover:bg-gray-100">Change Password</a>
                  <a href="#" @click="$auth.logout()"
                    class="block px-4 py-2 text-[12px] sm:text-[13px] lg:text-[14px] text-gray-700 hover:bg-gray-100">Log out</a>
                </div>
              </div>
            </template>
          </div>

          <!-- Mobile Menu Button -->
          <div class="md:hidden flex flex-col items-center">
            <button @click="toggleNavigation" class="text-[#0D4688] hover:text-[#0D4688] focus:outline-none">
              <span class="sr-only">Toggle menu</span>
              <svg v-if="!isNavigationOpen" class="h-5 w-5 sm:h-5.5 sm:w-5.5 lg:h-6 lg:w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
              </svg>
              <svg v-else class="h-5 w-5 sm:h-5.5 sm:w-5.5 lg:h-6 lg:w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
            <span
              class="text-[#0D4688] font-poppins text-[10px] sm:text-[11px] lg:text-[12px] font-bold leading-tight tracking-[0.004em] mb-1">MENU</span>
          </div>
        </div>
      </div>
    </nav>

    <!-- Sliding Navigation Menu -->
    <transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 -translate-y-full"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition-all duration-300 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-full"
    >
      <div v-if="isNavigationOpen" class="fixed inset-x-0 top-16 sm:top-18 lg:top-20 bg-[#0D4688] max-w-[1920px] mx-auto z-40 overflow-y-auto shadow-md"
        style="max-height: calc(100vh - 5rem);">
        <div class="max-w-[1920px] mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div class="space-y-4">
            <!-- Navigation Items -->
            <router-link :to='{ name: "Home" }'
              class="block py-2 px-4 font-poppins text-[16px] sm:text-[18px] lg:text-[20px] font-medium leading-tight text-left text-white hover:text-gray-200 cursor-pointer">
              Home</router-link>
            <router-link :to='{ name: "AssessmentTest" }'
              class="block py-2 px-4 font-poppins text-[16px] sm:text-[18px] lg:text-[20px] font-medium leading-tight text-left text-white hover:text-gray-200 cursor-pointer">
              Assignment</router-link>
            <router-link :to='{ name: "Home" }'
              class="block py-2 px-4 font-poppins text-[16px] sm:text-[18px] lg:text-[20px] font-medium leading-tight text-left text-white hover:text-gray-200 cursor-pointer">
              Compendium of Resources</router-link>
            <router-link :to='{ name: "Home" }'
              class="block py-2 px-4 font-poppins text-[16px] sm:text-[18px] lg:text-[20px] font-medium leading-tight text-left text-white hover:text-gray-200 cursor-pointer">
              Contact Us</router-link>

            <!-- Mobile view: Login/Logout and Profile options -->
            <div class="md:hidden">
              <template v-if="!$auth.isLoggedIn">
                <router-link :to='{ name: "Login" }'
                  class="block py-2 px-4 font-poppins text-[16px] sm:text-[18px] lg:text-[20px] font-medium leading-tight text-left text-white hover:text-gray-200 cursor-pointer">Login</router-link>
              </template>
              <template v-else>
                <button @click="openChangePasswordModal"
                  class="block py-2 px-4 font-poppins text-[16px] sm:text-[18px] lg:text-[20px] font-medium leading-tight text-left text-white hover:text-gray-200 cursor-pointer w-full text-left">Change Password</button>
                <button @click="$auth.logout()"
                  class="block py-2 px-4 font-poppins text-[16px] sm:text-[18px] lg:text-[20px] font-medium leading-tight text-left text-white hover:text-gray-200 cursor-pointer w-full text-left">Log out</button>
              </template>
            </div>
          </div>
        </div>
      </div>
    </transition>

    <!-- Change Password Modal -->
    <ChangePasswordModal :is-open="isChangePasswordModalOpen" @close="closeChangePasswordModal" />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import ChangePasswordModal from '../components/ChangePasswordModal.vue'

const router = useRouter()
const isNavigationOpen = ref(false)
const isUserMenuOpen = ref(false)
const isChangePasswordModalOpen = ref(false)
const currentRoute = ref('')

const toggleNavigation = () => {
  isNavigationOpen.value = !isNavigationOpen.value
}

const toggleUserMenu = () => {
  isUserMenuOpen.value = !isUserMenuOpen.value
}

const closeNavigation = () => {
  isNavigationOpen.value = false
}

const openChangePasswordModal = () => {
  isChangePasswordModalOpen.value = true
  isUserMenuOpen.value = false
  closeNavigation()
}

const closeChangePasswordModal = () => {
  isChangePasswordModalOpen.value = false
}

watch(() => router.currentRoute.value.path, (newRoute) => {
  currentRoute.value = newRoute
}, {
  immediate: true,
  deep: true
})

defineOptions({
  inject: ['$auth']
})
</script>

<style scoped>
.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

.duration-300 {
  transition-duration: 300ms;
}

.ease-out {
  transition-timing-function: cubic-bezier(0, 0, 0.2, 1);
}

.ease-in {
  transition-timing-function: cubic-bezier(0.4, 0, 1, 1);
}
</style>