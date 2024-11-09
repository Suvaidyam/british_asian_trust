<template>
    <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg p-8 max-w-md w-full">
        <h2 class="text-2xl font-bold mb-4">Change Password</h2>
        <form @submit.prevent="changePassword">
          <div class="mb-4">
            <label for="currentPassword" class="block text-sm font-medium text-gray-700">Current Password</label>
            <input type="password" id="currentPassword" v-model="currentPassword" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
          </div>
          <div class="mb-4">
            <label for="newPassword" class="block text-sm font-medium text-gray-700">New Password</label>
            <input type="password" id="newPassword" v-model="newPassword" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
          </div>
          <div class="mb-4">
            <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Confirm New Password</label>
            <input type="password" id="confirmPassword" v-model="confirmPassword" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
          </div>
          <div class="flex justify-end">
            <button type="button" @click="$emit('close')" class="mr-2 px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300">Cancel</button>
            <button type="submit" class="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700">Change Password</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const props = defineProps({
    isOpen: Boolean
  })
  
  const emit = defineEmits(['close'])
  
  const currentPassword = ref('')
  const newPassword = ref('')
  const confirmPassword = ref('')
  
  const changePassword = () => {
    // Implement password change logic here
    // You may want to add validation, API calls, etc.
    console.log('Changing password...')
    emit('close')
  }
  </script>