<template>
    <nav class="bg-gray-900 text-white ">

        <div class=" mx-16  h-[60px] flex items-center justify-between">
            <div class="flex items-center">
                <svg width="238" height="31" viewBox="0 0 238 31" fill="none" xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink">
                    <rect width="238" height="31" fill="url(#pattern0_173_529)" />
                    <defs>
                        <pattern id="pattern0_173_529" patternContentUnits="objectBoundingBox" width="1" height="1">
                            <use xlink:href="#image0_173_529"
                                transform="matrix(0.0033398 0 0 0.025641 -0.000969619 0)" />
                        </pattern>
                        <image id="image0_173_529" width="300" height="39"
                            xlink:href="data:image/png;base64,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" />
                    </defs>
                </svg>

            </div>

            <button v-if="currentRoute === '/login'" @click="$router.push({ name: 'Register' })"
                class="text-[12px] leading-[15.4px] text-yellow-400 hover:text-yellow-300 transition-colors duration-200">
                REGISTER AS A NGO
            </button>
            <button v-if="currentRoute === '/register'" @click="$router.push({ name: 'Login' })"
                class="text-[12px]  leading-[15.4px]  text-yellow-400 hover:text-yellow-300 transition-colors duration-200 ">
                LOGIN
            </button>
            <!-- User Section -->
            <div v-if="$auth.isLoggedIn" class="flex text-[12px] leading-[15.4px] items-center space-x-4">
                <!-- Navigation Links -->
                <div class="hidden md:flex space-x-6">
                    <a href="/" class="hover:text-gray-300">Home</a>
                    <a href="/assessment" class="hover:text-gray-300">Assessments</a>
                    <a href="/myuser" class="hover:text-gray-300">My Users</a>
                </div>
                <button class="hover:text-gray-300" aria-label="Notifications">
                    <BellIcon class="h-6 w-6" />
                </button>
                <div class="relative">
                    <button @click="toggleDropdown"
                        class="flex items-center space-x-2 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-900 focus:ring-white rounded-full"
                        aria-haspopup="true" :aria-expanded="isDropdownOpen">
                        <img src="../assets/main_bg.png" alt="User Avatar" class="h-8 w-8 rounded-full" />
                        <span class="hidden md:inline">{{ $auth?.cookie?.full_name }}</span>
                        <ChevronDownIcon class="h-4 w-4" :class="{ 'transform rotate-180': isDropdownOpen }" />
                    </button>
                    <transition enter-active-class="transition ease-out duration-100"
                        enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
                        leave-active-class="transition ease-in duration-75"
                        leave-from-class="transform opacity-100 scale-100"
                        leave-to-class="transform opacity-0 scale-95">
                        <div v-if="isDropdownOpen"
                            class="absolute right-0 mt-2 w-48 z-40 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5"
                            role="menu" aria-orientation="vertical" aria-labelledby="user-menu">
                            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                                role="menuitem">Your Profile</a>
                            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                                role="menuitem">Settings</a>
                            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem"
                                @click="$auth.logout()">Logout</a>
                        </div>
                    </transition>
                </div>
            </div>

            <!-- Mobile menu button -->
            <div class="md:hidden">
                <button @click="toggleMobileMenu"
                    class="text-gray-300 hover:text-white focus:outline-none focus:text-white">
                    <MenuIcon v-if="!isMobileMenuOpen" class="h-6 w-6" />
                    <XIcon v-else class="h-6 w-6" />
                </button>
            </div>
        </div>

        <!-- Mobile menu -->
        <transition enter-active-class="transition ease-out duration-100"
            enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
            leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100"
            leave-to-class="transform opacity-0 scale-95">
            <div v-if="isMobileMenuOpen" class="md:hidden mt-2">
                <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                    <a href="#"
                        class="block px-3 py-2 rounded-md text-base font-medium text-white hover:text-gray-300 hover:bg-gray-700">Home</a>
                    <a href="#"
                        class="block px-3 py-2 rounded-md text-base font-medium text-white hover:text-gray-300 hover:bg-gray-700">Assessments</a>
                    <a href="#"
                        class="block px-3 py-2 rounded-md text-base font-medium text-white hover:text-gray-300 hover:bg-gray-700">My
                        Users</a>
                </div>
            </div>
        </transition>
    </nav>
    <!-- Add login/register buttons here -->



</template>
<script setup>
import { ref, onMounted, watch } from 'vue'
import { BellIcon, ChevronDownIcon, MenuIcon, XIcon } from 'lucide-vue-next'
import { useRoute, useRouter } from 'vue-router'


const isDropdownOpen = ref(false)
const isMobileMenuOpen = ref(false)
const currentRoute = ref('')

const route = useRoute()
const router = useRouter()

// Track the route path and update currentRoute
onMounted(() => {
    currentRoute.value = route.path
})

// Watch for route changes
watch(() => route.path, (newPath) => {
    currentRoute.value = newPath
})

const toggleDropdown = () => {
    isDropdownOpen.value = !isDropdownOpen.value
}

const toggleMobileMenu = () => {
    isMobileMenuOpen.value = !isMobileMenuOpen.value
}

defineOptions({

    inject: ['$auth']
})
</script>