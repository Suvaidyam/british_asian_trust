<template>
  <transition
    enter-active-class="transition-all duration-300 ease-in-out"
    enter-from-class="translate-x-full"
    enter-to-class="translate-x-0"
    leave-active-class="transition-all duration-300 ease-in-out"
    leave-from-class="translate-x-0"
    leave-to-class="translate-x-full"
  >
    <div v-if="isOpen" class="fixed inset-y-0 right-0 w-full sm:w-96 bg-white shadow-lg z-50 overflow-y-auto">
      <div class="p-4 sm:p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="font-poppins text-[20px] font-semibold leading-[22px] tracking-[0.0015em] text-[#0D4688]">Notifications</h2>
          <button @click="close" class="text-gray-500 hover:text-gray-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 rounded-md">
            <span class="sr-only">Close panel</span>
            <XIcon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div v-if="notifications.length === 0" class="text-center py-8">
          <p class="font-poppins text-[14px] font-normal leading-[19.6px] tracking-[0.0025em] text-[#596C8C]">
            No new notifications
          </p>
        </div>
        <ul v-else class="space-y-4">
          <li v-for="notification in notifications" :key="notification.id" class="bg-gray-50 p-4 rounded-lg">
            <div class="flex items-start">
              <div class="flex-shrink-0">
                <BellIcon class="h-6 w-6 text-[#0D4688]" aria-hidden="true" />
              </div>
              <div class="ml-3 w-0 flex-1 pt-0.5">
                <p class="font-poppins text-[14px] font-semibold leading-[19.6px] tracking-[0.0025em] text-[#0D4688]">
                  {{ notification.title }}
                </p>
                <p class="mt-1 font-poppins text-[14px] font-normal leading-[19.6px] tracking-[0.0025em] text-[#212529]">
                  {{ notification.message }}
                </p>
                <p class="mt-1 font-poppins text-[12px] font-normal leading-[16.8px] tracking-[0.004em] text-[#596C8C]">
                  {{ formatDate(notification.date) }}
                </p>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'
import { XIcon, BellIcon } from 'lucide-vue-next'

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true
  },
  notifications: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['close'])

const close = () => {
  emit('close')
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('en-GB', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  }).replace(/\//g, '-')
}
</script>

<style scoped>
/* Add any component-specific styles here */
</style>