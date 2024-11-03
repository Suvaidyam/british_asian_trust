<template>
    <transition enter-active-class="transition ease-in-out duration-300 transform" enter-from-class="translate-x-full"
      enter-to-class="translate-x-0" leave-active-class="transition ease-in-out duration-300 transform"
      leave-from-class="translate-x-0" leave-to-class="translate-x-full">
      <div v-if="isOpen" class="fixed inset-0 overflow-hidden z-50">
        <div class="absolute inset-0 overflow-hidden">
          <div class="absolute inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
          <section class="absolute inset-y-0 right-0 pl-10 max-w-full flex" aria-labelledby="slide-over-heading">
            <div class="relative w-screen max-w-md">
              <div class="h-full flex flex-col py-6 bg-white shadow-xl overflow-y-scroll">
                <div class="px-4 sm:px-6">
                  <div class="flex items-start justify-between">
                    <h2 id="slide-over-heading" class="font-poppins text-[20px] font-semibold leading-[22px] tracking-[0.0015em] text-[#0D4688]">User Profile</h2>
                    <div class="ml-3 h-7 flex items-center">
                      <button @click="closeProfile"
                        class="bg-white rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                        <span class="sr-only">Close panel</span>
                        <XIcon class="h-6 w-6" aria-hidden="true" />
                      </button>
                    </div>
                  </div>
                </div>
                <div class="mt-6 relative flex-1 px-4 sm:px-6">
                  <div class="flex flex-col items-center">
                    <img :src="$auth?.user?.user_image || '/placeholder.svg?height=128&width=128'"
                      alt="User avatar" class="h-32 w-32 rounded-full mb-4" />
                    <h3 class="font-poppins text-[20px] font-semibold leading-[22px] tracking-[0.0015em] text-[#0D4688] mb-2">{{ $auth?.user?.full_name || 'User Name' }}</h3>
                    <p class="font-poppins text-[14px] font-normal leading-[19.6px] tracking-[0.0025em] text-[#596C8C] mb-6">{{ $auth?.user?.email || 'user@example.com' }}</p>
                  </div>
                  <div class="space-y-6">
                    <div>
                      <h4 class="font-poppins text-[14px] font-semibold leading-[19.6px] tracking-[0.0025em] text-[#596C8C] uppercase mb-2">Personal Information</h4>
                      <div class="bg-gray-50 rounded-lg p-4 space-y-2">
                        <p class="font-poppins text-[14px] font-normal leading-[19.6px] tracking-[0.0025em] text-[#212529]"><span class="font-semibold text-[#0D4688]">Username:</span> {{ $auth?.user?.username || 'Not provided' }}</p>
                        <p class="font-poppins text-[14px] font-normal leading-[19.6px] tracking-[0.0025em] text-[#212529]"><span class="font-semibold text-[#0D4688]">Phone:</span> {{ $auth?.user?.phone || 'Not provided' }}</p>
                        <p class="font-poppins text-[14px] font-normal leading-[19.6px] tracking-[0.0025em] text-[#212529]"><span class="font-semibold text-[#0D4688]">Location:</span> {{ $auth?.user?.location || 'Not provided' }}</p>
                      </div>
                    </div>
                    <div>
                      <h4 class="font-poppins text-[14px] font-semibold leading-[19.6px] tracking-[0.0025em] text-[#596C8C] uppercase mb-2">Account Information</h4>
                      <div class="bg-gray-50 rounded-lg p-4 space-y-2">
                        <p class="font-poppins text-[14px] font-normal leading-[19.6px] tracking-[0.0025em] text-[#212529]"><span class="font-semibold text-[#0D4688]">Account Type:</span> {{ $auth?.user?.account_type || 'Standard' }}</p>
                        <p class="font-poppins text-[14px] font-normal leading-[19.6px] tracking-[0.0025em] text-[#212529]"><span class="font-semibold text-[#0D4688]">Member Since:</span> {{ formatDate($auth?.user?.created_at) }}</p>
                      </div>
                    </div>
                  </div>
                  <!-- <div class="mt-8">
                    <button @click="editProfile"
                      class="w-full bg-orange-500 hover:bg-orange-600 text-white font-poppins text-[14px] font-semibold leading-[15.4px] tracking-[0.0125em] py-2 px-4 rounded-full transition duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-orange-500 focus:ring-opacity-50">
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
  import { ref, onMounted, inject } from 'vue'
  import { XIcon } from 'lucide-vue-next'
  
  const props = defineProps({
    isOpen: {
      type: Boolean,
      required: true
    }
  })
  
  const emit = defineEmits(['close'])
  const $auth = inject('$auth')
  
  const closeProfile = () => {
    emit('close')
  }
  
  const editProfile = () => {
    // Implement edit profile functionality
    console.log('Edit profile clicked')
  }
  
  const formatDate = (dateString) => {
    if (!dateString) return 'Not available'
    return new Date(dateString).toLocaleDateString('en-GB', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit'
    }).replace(/\//g, '-')
  }
  
  onMounted(() => {
    // Any necessary setup can be done here
  })
  </script>
  
  <style scoped>
  /* Add any component-specific styles here */
  </style>