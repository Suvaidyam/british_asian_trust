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
        <div class="p-4">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-semibold">Notifications</h2>
            <button @click="close" class="text-gray-500 hover:text-gray-700 focus:outline-none">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          <div v-if="notifications.length === 0" class="text-center text-gray-500 py-8">
            No new notifications
          </div>
          <ul v-else class="space-y-4">
            <li v-for="notification in notifications" :key="notification.id" class="bg-gray-50 p-4 rounded-lg">
              <div class="flex items-start">
                <div class="flex-shrink-0">
                  <svg class="h-6 w-6 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                      d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                  </svg>
                </div>
                <div class="ml-3 w-0 flex-1 pt-0.5">
                  <p class="text-sm font-medium text-gray-900">{{ notification.title }}</p>
                  <p class="mt-1 text-sm text-gray-500">{{ notification.message }}</p>
                  <p class="mt-1 text-xs text-gray-400">{{ formatDate(notification.date) }}</p>
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
    return new Date(date).toLocaleString()
  }
  </script>