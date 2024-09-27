<template>
  <div class="min-h-screen bg-gray-100 p-4 sm:p-6 lg:p-8">
    <div class="px-16 bg-white rounded-lg shadow-lg overflow-hidden">
      <div class="p-4 sm:p-6 lg:p-8">
        <div class="flex flex-col sm:flex-row justify-between items-center mb-6">
          <h1 class="text-2xl font-bold text-gray-800 mb-4 sm:mb-0">My Users</h1>
          <div class="flex w-full sm:w-auto space-x-2">
            <input
              type="text"
              placeholder="Search by name"
              class="flex-grow sm:flex-grow-0 px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-pink-500"
            />
            <button 
              @click="showInviteModal = true"
              class="px-4 py-2 bg-pink-600 text-white rounded-md hover:bg-pink-700 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:ring-offset-2"
            >
              INVITE NEW USER
            </button>
          </div>
        </div>

        <div class="bg-pink-100 rounded-lg p-6 mb-8">
          <div class="flex flex-wrap justify-center items-center gap-8">
            <div v-for="(user, index) in topUsers" :key="user.name" class="flex flex-col items-center">
              <div class="relative">
                <img :src="user.avatar" :alt="user.name" class="w-20 h-20 rounded-full border-4 border-white shadow-lg" />
                <div v-if="index === 1" class="absolute -top-2 left-1/2 transform -translate-x-1/2 bg-yellow-400 rounded-full p-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-white" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </div>
              </div>
              <p class="mt-2 font-semibold text-gray-800">{{ user.name }}</p>
              <p class="text-sm text-gray-600">{{ user.role }}</p>
            </div>
          </div>
        </div>

        <div>
          <h2 class="text-xl font-semibold text-gray-800 mb-4">Users Listing</h2>
          <div class="overflow-x-auto">
            <table class="w-full">
              <thead>
                <tr class="bg-gray-50">
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
                  <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Score</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="user in users" :key="user.email">
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-center">
                      <div class="flex-shrink-0 h-10 w-10">
                        <img class="h-10 w-10 rounded-full" :src="user.avatar" :alt="user.name" />
                      </div>
                      <div class="ml-4">
                        <div class="text-sm font-medium text-gray-900">{{ user.name }}</div>
                        <div class="text-sm text-gray-500">{{ user.role }}</div>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="text-sm text-gray-900">{{ user.email }}</div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                    <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                      {{ user.score }}
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- Invite User Modal -->
    <div v-if="showInviteModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-lg shadow-xl max-w-md w-full">
        <div class="flex justify-between items-center p-6 border-b">
          <h2 class="text-xl font-semibold text-gray-800">Invite User</h2>
          <button @click="showInviteModal = false" class="text-gray-400 hover:text-gray-600">
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <form @submit.prevent="sendInvitation" class="p-6">
          <div class="space-y-4">
            <div>
              <label for="fullName" class="block text-sm font-medium text-gray-700">Full Name</label>
              <input type="text" id="fullName" v-model="inviteForm.fullName" placeholder="Enter user full name" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-pink-500 focus:border-pink-500" required>
            </div>
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700">Email Address</label>
              <input type="email" id="email" v-model="inviteForm.email" placeholder="Enter user email address" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-pink-500 focus:border-pink-500" required>
            </div>
            <div>
              <label for="designation" class="block text-sm font-medium text-gray-700">Designation</label>
              <select id="designation" v-model="inviteForm.designation" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-pink-500 focus:border-pink-500">
                <option value="">Select designation</option>
                <option value="admin">Admin</option>
                <option value="manager">Manager</option>
                <option value="associate">Associate</option>
              </select>
            </div>
            <div>
              <label for="mobile" class="block text-sm font-medium text-gray-700">Mobile Number (Optional)</label>
              <div class="mt-1 flex rounded-md shadow-sm">
                <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 text-sm">
                  +91
                </span>
                <input type="tel" id="mobile" v-model="inviteForm.mobile" placeholder="Enter your phone number" class="flex-1 block w-full border-gray-300 rounded-none rounded-r-md focus:ring-pink-500 focus:border-pink-500">
              </div>
            </div>
          </div>
          <div class="mt-6">
            <button type="submit" class="w-full px-4 py-2 bg-pink-600 text-white rounded-md hover:bg-pink-700 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:ring-offset-2">
              SEND INVITATION
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const showInviteModal = ref(false)

const inviteForm = reactive({
  fullName: '',
  email: '',
  designation: '',
  mobile: ''
})

const sendInvitation = () => {
  // Here you would typically send the invitation data to your backend
  console.log('Sending invitation:', inviteForm)
  // Reset form and close modal
  Object.assign(inviteForm, { fullName: '', email: '', designation: '', mobile: '' })
  showInviteModal.value = false
}

const topUsers = [
  { name: 'Ashok Sharma', role: 'Associate', avatar: '/placeholder.svg?height=80&width=80' },
  { name: 'Meena Kumar', role: 'Manager', avatar: '/placeholder.svg?height=80&width=80' },
  { name: 'Jitesh Sharma', role: 'Associate', avatar: '/placeholder.svg?height=80&width=80' },
]

const users = [
  { name: 'Abhishek Singh (You)', role: 'Admin', email: 'abhishek123@gmail.com', score: 12, avatar: '/placeholder.svg?height=40&width=40' },
  { name: 'Aasrith Kumar', role: 'Associate', email: 'sample@gmail.com', score: 4, avatar: '/placeholder.svg?height=40&width=40' },
  { name: 'Binod Sharma', role: 'Associate', email: 'sample@gmail.com', score: 5, avatar: '/placeholder.svg?height=40&width=40' },
  { name: 'Gia Kumar', role: 'Associate', email: 'sample@gmail.com', score: 6, avatar: '/placeholder.svg?height=40&width=40' },
  { name: 'Kantesh Yadav', role: 'Associate', email: 'sample@gmail.com', score: 7, avatar: '/placeholder.svg?height=40&width=40' },
  { name: 'Ankit Yadav', role: 'Associate', email: 'sample@gmail.com', score: 8, avatar: '/placeholder.svg?height=40&width=40' },
  { name: 'Umesh', role: 'Associate', email: 'sample@gmail.com', score: 9, avatar: '/placeholder.svg?height=40&width=40' },
]
</script>