<template>
  <nav class="bg-gray-900 text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-[60px]">
        <div class="flex items-center justify-between">
         <router-link :to="{ name: 'Home' }">
          <div class="flex-shrink-0">
            <img class="h-7 w-auto" src="../../public/logo.png" alt="Logo">
          </div>
          </router-link>
        </div>

        <div class="hidden md:block">
          <div class="ml-4 flex items-center md:ml-6">
            <!-- Conditionally Render Register/Login Buttons -->
            <button v-if="currentRoute === '/login'" @click="$router.push({ name: 'Register' })"
              class="text-sm text-yellow-400 hover:text-yellow-300 transition-colors duration-200 mr-4">
              REGISTER AS A NGO
            </button>
            <button v-if="currentRoute === '/register'" @click="$router.push({ name: 'Login' })"
              class="text-sm text-yellow-400 hover:text-yellow-300 transition-colors duration-200 mr-4">
              LOGIN
            </button>
            <div v-if="$auth.isLoggedIn" class="ml-auto">
              <div class="flex items-baseline space-x-4">
                <router-link :to="{ name: 'Home' }"
                  class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Home</router-link>
                <router-link :to="{name: 'Assessment'}"
                  class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Assessments</router-link>
                <router-link :to="{name: 'MyUser'}"
                  class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">My
                  Users</router-link>
              </div>
            </div>

            <!-- User Dropdown if Logged In -->
            <template v-if="$auth.isLoggedIn">
              <button
                class="p-1 rounded-full text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white">
                <span class="sr-only">View notifications</span>
                <BellIcon class="h-6 w-6" aria-hidden="true" />
              </button>

              <!-- User Profile Dropdown -->
              <div class="ml-3 relative">
                <div class="flex items-center justify-center gap-3">
                  <button @click="toggleDropdown" type="button"
                    class="max-w-xs bg-gray-800 rounded-full flex items-center text-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white"
                    id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                    <span class="sr-only">Open user menu</span>
                    <img class="h-8 w-8 rounded-full" src="../../public/user.png" alt="User avatar">
                  </button>
                  <p class="text-sm text-gray-300">{{ $auth?.cookie?.full_name }}</p>
                </div>

                <!-- Dropdown Menu -->
                <transition enter-active-class="transition ease-out duration-100"
                  enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
                  leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100"
                  leave-to-class="transform opacity-0 scale-95">
                  <div v-if="isDropdownOpen"
                    class="origin-top-right absolute right-0 mt-2 w-48 z-50 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
                    role="menu" aria-orientation="vertical" aria-labelledby="user-menu-button" tabindex="-1">
                    <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Your
                      Profile</a>
                    <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      role="menuitem">Settings</a>
                    <a href="#" @click="$auth.logout()" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      role="menuitem">Log out</a>
                  </div>
                </transition>
              </div>
            </template>
          </div>
        </div>
        <!-- Mobile Menu Button -->
        <div class="md:hidden">
          <button @click="toggleMobileMenu" type="button"
            class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white"
            aria-controls="mobile-menu" :aria-expanded="isMobileMenuOpen">
            <span class="sr-only">{{ isMobileMenuOpen ? 'Close main menu' : 'Open main menu' }}</span>
            <MenuIcon v-if="!isMobileMenuOpen" class="block h-6 w-6" aria-hidden="true" />
            <XIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu (Slide from right) -->
    <transition
      enter-active-class="transition ease-out duration-300 transform"
      enter-from-class="translate-x-full"
      enter-to-class="translate-x-0"
      leave-active-class="transition ease-in duration-300 transform"
      leave-from-class="translate-x-0"
      leave-to-class="translate-x-full"
    >
      <div v-if="isMobileMenuOpen" 
           class="md:hidden fixed top-0 right-0 bottom-0 w-64 bg-gray-900 shadow-lg z-50 overflow-y-auto"
           id="mobile-menu">
        <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
          <button @click="closeMobileMenu" 
                  class="absolute top-4 right-4 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                  aria-label="Close menu">
            <XIcon class="h-6 w-6" aria-hidden="true" />
          </button>
          <button v-if="currentRoute === '/login'" @click="$router.push({ name: 'Register' }); closeMobileMenu();"
            class="block w-full text-left px-3 py-2 rounded-md text-base font-medium text-yellow-400 hover:text-yellow-300 hover:bg-gray-700 transition-colors duration-200">
            REGISTER AS A NGO
          </button>
          <button v-if="currentRoute === '/register'" @click="$router.push({ name: 'Login' }); closeMobileMenu();"
            class="block w-full text-left px-3 py-2 rounded-md text-base font-medium text-yellow-400 hover:text-yellow-300 hover:bg-gray-700 transition-colors duration-200">
            LOGIN
          </button>
          <template v-if="$auth.isLoggedIn">
            <router-link :to="{ name: 'Home' }" @click="closeMobileMenu"
              class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium">Home</router-link>
            <router-link :to="{ name: 'Assessment' }" @click="closeMobileMenu"
              class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium">Assessments</router-link>
            <router-link :to="{ name: 'MyUser' }" @click="closeMobileMenu"
              class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium">My
              Users</router-link>
          </template>
        </div>
        <div v-if="$auth.isLoggedIn" class="pt-4 pb-3 border-t border-gray-700">
          <div class="flex items-center px-5">
            <div class="flex-shrink-0">
              <img class="h-10 w-10 rounded-full" src="../../public/user.png" alt="User avatar">
            </div>
            <div class="ml-3">
              <div class="text-base font-medium leading-none text-white">{{ $auth?.cookie?.full_name }}</div>
              <div class="text-sm font-medium leading-none text-gray-400">{{ $auth?.cookie?.email }}</div>
            </div>
            <button type="button"
              class="ml-auto bg-gray-800 flex-shrink-0 p-1 rounded-full text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white">
              <span class="sr-only">View notifications</span>
              <BellIcon class="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
          <div class="mt-3 px-2 space-y-1">
            <a href="#" @click="closeMobileMenu"
              class="block px-3 py-2 rounded-md text-base font-medium text-gray-400 hover:text-white hover:bg-gray-700">Your
              Profile</a>
            <a href="#" @click="closeMobileMenu"
              class="block px-3 py-2 rounded-md text-base font-medium text-gray-400 hover:text-white hover:bg-gray-700">Settings</a>
            <a href="#" @click="$auth.logout(); closeMobileMenu();"
              class="block px-3 py-2 rounded-md text-base font-medium text-gray-400 hover:text-white hover:bg-gray-700">Log
              out</a>
          </div>
        </div>
      </div>
    </transition>
  </nav>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { BellIcon, MenuIcon, XIcon } from 'lucide-vue-next'
import { useRoute, useRouter } from 'vue-router'

const isDropdownOpen = ref(false)
const isMobileMenuOpen = ref(false)
const currentRoute = ref('')

const route = useRoute()
const router = useRouter()

onMounted(() => {
  currentRoute.value = route.path
})

watch(() => route.path, (newPath) => {
  currentRoute.value = newPath
})

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value
}

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false
}

defineOptions({
  inject: ['$auth']
})
</script>