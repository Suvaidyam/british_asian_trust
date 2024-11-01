<template>
    <transition enter-active-class="transition ease-in-out duration-300 transform" enter-from-class="translate-x-full"
        enter-to-class="translate-x-0" leave-active-class="transition ease-in-out duration-300 transform"
        leave-from-class="translate-x-0" leave-to-class="translate-x-full">
        <div v-if="isOpen" class="fixed inset-0 overflow-hidden z-50">
            <div class="absolute inset-0 overflow-hidden">
                <div class="absolute inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
                <section class="absolute inset-y-0 right-0 pl-10 max-w-full flex" aria-labelledby="slide-over-heading">
                    <div class="relative w-screen max-w-md">
                        <div class="h-full flex flex-col py-6 bg-gray-900 shadow-xl overflow-y-scroll">
                            <div class="px-4 sm:px-6">
                                <div class="flex items-start justify-between">
                                    <h2 id="slide-over-heading" class="text-lg font-medium text-white">User Profile</h2>
                                    <div class="ml-3 h-7 flex items-center">
                                        <button @click="closeProfile"
                                            class="bg-gray-900 rounded-md text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white">
                                            <span class="sr-only">Close panel</span>
                                            <XIcon class="h-6 w-6" aria-hidden="true" />
                                        </button>
                                    </div>
                                </div>
                            </div>
                            <div class="mt-6 relative flex-1 px-4 sm:px-6">
                                <div class="flex flex-col items-center">
                                    <img :src="$auth?.cookie?.user_image"
                                        alt="User avatar" class="h-32 w-32 rounded-full mb-4" />
                                    <h3 class="text-xl font-semibold text-white mb-2">{{ $auth?.cookie?.full_name }}
                                    </h3>
                                    <p class="text-gray-400 mb-6">{{ $auth}}</p>
                                </div>
                                <div class="space-y-6">
                                    <div>
                                        <h4 class="text-sm font-medium text-gray-400 uppercase tracking-wider mb-2">
                                            Personal Information</h4>
                                        <div class="bg-gray-800 rounded-lg p-4 space-y-2">
                                            <p class="text-white"><span class="text-gray-400">Username:</span> {{
                                                userProfile.username }}</p>
                                            <p class="text-white"><span class="text-gray-400">Phone:</span> {{
                                                userProfile.phone || 'Not provided' }}</p>
                                            <p class="text-white"><span class="text-gray-400">Location:</span> {{
                                                userProfile.location || 'Not provided' }}</p>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 class="text-sm font-medium text-gray-400 uppercase tracking-wider mb-2">
                                            Account Information</h4>
                                        <div class="bg-gray-800 rounded-lg p-4 space-y-2">
                                            <p class="text-white"><span class="text-gray-400">Account Type:</span> {{
                                                userProfile.account_type || 'Standard' }}</p>
                                            <p class="text-white"><span class="text-gray-400">Member Since:</span> {{
                                                formatDate(userProfile.created_at) }}</p>
                                        </div>
                                    </div>
                                </div>
                                <!-- <div class="mt-8">
                                    <button @click="editProfile"
                                        class="w-full bg-yellow-400 hover:bg-yellow-300 text-gray-900 font-semibold py-2 px-4 rounded-md transition duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:ring-opacity-50">
                                        Edit Profile
                                    </button>
                                </div> -->
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </transition>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { XIcon } from 'lucide-vue-next'

const props = defineProps({
    isOpen: {
        type: Boolean,
        required: true
    }
})

const emit = defineEmits(['close'])

const userProfile = ref({
    full_name: 'Aniket Singh',
    email: 'aniketsinghne@gmail.com',
    image: '/placeholder.svg?height=128&width=128',
    username: 'aniket',
    phone: '9117029185',
    location: 'India',
    account_type: 'NGO',
    created_at: '2023-01-01T00:00:00Z'
})

const closeProfile = () => {
    emit('close')
}

const editProfile = () => {
    // Implement edit profile functionality
    console.log('Edit profile clicked')
}

const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    })
}

onMounted(() => {

})

defineOptions({
    inject: ['$auth']
})
</script>