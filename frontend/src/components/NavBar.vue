<template>
  <div class="relative">
    <!-- Fixed Navigation Bar -->
    <nav class="fixed top-0 left-0 right-0 bg-white z-50">
      <div class="max-w-[1512px] mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-20">
          <div class="flex items-center">
            <img src="/logo.png" alt="ISDM Logo" class="h-12 w-auto" />
          </div>

          <!-- Desktop Navigation -->
          <div class="hidden md:flex items-center space-x-4">
            <div class="flex flex-col items-center">

              <button @click="toggleNavigation" class="text-[#0D4688] hover:text-[#0D4688] focus:outline-none">
                <span class="sr-only">Toggle navigation</span>
                <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path v-if="!isNavigationOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M4 6h16M4 12h16m-7 6h7" />
                  <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
              <span class="text-[#0D4688] font-poppins text-[12px] md:text-sm font-bold leading-[13.2px] tracking-[0.004em] mb-1">MENU</span>
            </div>

            <template v-if="!$auth?.isLoggedIn && currentRoute == '/'">
              <button @click="$router.push({ name: 'Login' })"
                class="px-6 py-3 font-poppins text-[14px] md:text-base font-semibold leading-[15.4px] tracking-[0.0125em] text-white bg-[#FF8A00] hover:bg-[#FF8A00] rounded-full transition-colors duration-200 w-40">
                Login
              </button>
            </template>
            <template v-if="$auth?.isLoggedIn">
              <button @click="toggleNotifications"
                class="text-gray-600 hover:text-gray-800 focus:outline-none relative">
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
                </svg>
                <span v-if="unreadNotificationsCount > 0"
                  class="absolute -top-1 -right-1 bg-red-500 text-white text-[10px] rounded-full h-4 w-4 flex items-center justify-center">
                  {{ unreadNotificationsCount }}
                </span>
              </button>
              <div class="relative">
                <button @click="toggleUserMenu"
                  class="flex items-center text-gray-600 hover:text-gray-800 focus:outline-none">
                  <img class="h-8 w-8 rounded-full" :src="$auth?.cookie?.user_image" alt="User avatar" />
                  <span class="ml-2 text-[14px] sm:text-[15px] md:text-[16px] text-gray-700">{{ $auth?.cookie?.full_name
                    }}</span>
                </button>
                <div v-if="isUserMenuOpen"
                  class="absolute right-0 mt-2 w-48 bg-white border border-gray-300 rounded-md shadow-lg z-50">
                  <a href="#" @click.prevent="openProfileSlider"
                    class="block px-4 py-2 text-[14px] sm:text-[15px] md:text-[16px] text-gray-700 hover:bg-gray-100">Your
                    Profile</a>
                  <a href="#" @click="$auth.logout()"
                    class="block px-4 py-2 text-[14px] sm:text-[15px] md:text-[16px] text-gray-700 hover:bg-gray-100">Log
                    out</a>
                </div>
              </div>
            </template>
          </div>

          <!-- Mobile Menu Button -->
          <div class="md:hidden flex flex-col items-center">

            <button @click="toggleNavigation" class="text-[#0D4688] hover:text-[#0D4688] focus:outline-none">
              <span class="sr-only">Toggle menu</span>
              <svg v-if="!isNavigationOpen" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
              </svg>
              <svg v-else class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
            <span class="text-[#0D4688] font-poppins text-[12px] md:text-sm font-bold leading-[13.2px] tracking-[0.004em] mb-1">MENU</span>
          </div>
        </div>
      </div>
    </nav>

    <!-- Sliding Navigation Menu -->
    <transition enter-active-class="transition-all duration-300 ease-in-out"
      enter-from-class="opacity-0 -translate-y-full" enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition-all duration-300 ease-in-out" leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-full">
      <div v-if="isNavigationOpen" class="fixed inset-x-0 top-16 bg-[#0D4688] z-40 overflow-y-auto shadow-md"
        style="max-height: calc(100vh - 4rem);">
        <div class="max-w-[1512px] mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div class="space-y-4">
            <!-- Navigation Items -->
            <a @click="navigateTo('AboutUs')"
              class="block py-2 px-4 text-[16px] sm:text-[17px] md:text-[18px] text-white hover:text-gray-200 cursor-pointer">About
              Us</a>
            <a @click="navigateTo('Assignment')"
              class="block py-2 px-4 text-[16px] sm:text-[17px] md:text-[18px] text-white hover:text-gray-200 cursor-pointer">Assignment</a>

            <!-- Mobile view: Login/Logout and Profile options -->
            <div class="md:hidden">
              <template v-if="!$auth.isLoggedIn">
                <a @click="navigateTo('Login')"
                  class="block py-2 px-4 text-[16px] sm:text-[17px] md:text-[18px] text-white hover:text-gray-200 cursor-pointer">Login</a>
              </template>
              <template v-else>
                <a @click="toggleNotifications"
                  class="block py-2 px-4 text-[16px] sm:text-[17px] md:text-[18px] text-white hover:text-gray-200 cursor-pointer">Notifications</a>
                <a @click="openProfileSlider"
                  class="block py-2 px-4 text-[16px] sm:text-[17px] md:text-[18px] text-white hover:text-gray-200 cursor-pointer">Your
                  Profile</a>
                <a @click="$auth.logout()"
                  class="block py-2 px-4 text-[16px] sm:text-[17px] md:text-[18px] text-white hover:text-gray-200 cursor-pointer">Log
                  out</a>
              </template>
            </div>
          </div>
        </div>
      </div>
    </transition>

    <!-- Main Content Area (adjust top padding to account for fixed navbar) -->
    <main class="pt-16 max-w-[1512px] mx-auto">
      <!-- Your main content goes here -->
    </main>

    <!-- User Profile Slider -->
    <UserProfileSlider :is-open="isProfileSliderOpen" @close="closeProfileSlider" />

    <!-- Notification Slider -->
    <NotificationSlider :is-open="isNotificationSliderOpen" :notifications="notifications"
      @close="closeNotificationSlider" />
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import { useRouter } from 'vue-router'
import UserProfileSlider from '../views/UserProfileSlider.vue'
import NotificationSlider from '../views/NotificationSlider.vue'

const router = useRouter()
const isNavigationOpen = ref(false)
const isUserMenuOpen = ref(false)
const isProfileSliderOpen = ref(false)
const isNotificationSliderOpen = ref(false)
const currentRoute = ref('')

// Mock notifications data (replace with actual data fetching logic)
const notifications = ref([
  { id: 1, title: 'New Message', message: 'You have a new message from John Doe', date: new Date() },
  { id: 2, title: 'Task Completed', message: 'Your task "Project Review" has been completed', date: new Date(Date.now() - 86400000) },
])

const unreadNotificationsCount = computed(() => {
  return notifications.value.length
})

const toggleNavigation = () => {
  isNavigationOpen.value = !isNavigationOpen.value
}

const toggleUserMenu = () => {
  isUserMenuOpen.value = !isUserMenuOpen.value
}

const toggleNotifications = () => {
  isNotificationSliderOpen.value = !isNotificationSliderOpen.value
  if (isNotificationSliderOpen.value) {
    closeNavigation()
    isUserMenuOpen.value = false
  }
}

const closeNavigation = () => {
  isNavigationOpen.value = false
}

const openProfileSlider = () => {
  isProfileSliderOpen.value = true
  isUserMenuOpen.value = false
  closeNavigation()
}

const closeProfileSlider = () => {
  isProfileSliderOpen.value = false
}

const closeNotificationSlider = () => {
  isNotificationSliderOpen.value = false
}

const navigateTo = (routeName) => {
  router.push({ name: routeName })
  closeNavigation()
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
/* Add any additional styles here if needed */
</style>