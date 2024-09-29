<template>
  <div class="min-h-screen bg-gray-100 px-16 py-4 ">
    <div class="max-w-7xl mx-auto bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Header -->
      <div class="p-4 flex flex-col md:flex-row justify-between items-center border-b">
        <h1 class="text-2xl font-semibold text-gray-800 mb-4 md:mb-0">My Users</h1>
        <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4 w-full md:w-auto">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search by name"
            class="px-3 py-1.5 placeholder:text-xs border rounded-md focus:outline-none focus:ring-2 focus:ring-pink-500 w-full sm:w-auto"
          />
          <button 
            @click="openModal"
            class="px-3 py-1.5 text-sm bg-[#CA2247] text-white rounded-md hover:bg-pink-700 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:ring-offset-2 w-full sm:w-auto"
          >
            INVITE NEW USER
          </button>
        </div>
      </div>

      <!-- Top Achiever Section -->
      <div class="relative bg-my-user p-8">
        <div class="absolute inset-0 bg-pink-200 opacity-50 radial-gradient"></div>
        <h2 class="text-center text-xl font-semibold mb-6 relative z-10">Top Achiever</h2>
        <div class="flex flex-col sm:flex-row items-center justify-around space-y-8 sm:space-y-0 sm:space-x-8 relative ">
          <div class="text-center">
            <img src="../../public/user.png" alt="Ashok Sharma" class="w-20 h-20 rounded-full mx-auto mb-2 border-2 border-white" />
            <p class="font-medium">Ashok Sharma</p>
            <p class="text-sm text-gray-600">Associate</p>
          </div>
          <div class="text-center sm:-mb-4">
            <div class="relative">
              <img src="../../public/user.png" alt="Meena Kumar" class="w-24 h-24 rounded-full mx-auto mb-2 border-2 border-white" />
              <span class="absolute top-0 right-0 bg-yellow-400 p-1 rounded-full">
                <AwardIcon class="h-4 w-4 text-white" />
              </span>
            </div>
            <p class="font-medium">Meena Kumar</p>
            <p class="text-sm text-gray-600">Manager</p>
          </div>
          <div class="text-center">
            <img src="../../public/user.png" alt="Jitesh Sharma" class="w-20 h-20 rounded-full mx-auto mb-2 border-2 border-white" />
            <p class="font-medium">Jitesh Sharma</p>
            <p class="text-sm text-gray-600">Associate</p>
          </div>
        </div>
      </div>

      <!-- User Listing -->
      <div class="p-4">
        <h3 class="text-lg font-semibold mb-4">Users Listing</h3>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Number</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y  divide-gray-200">
              <tr class="" v-for="(user, index) in filteredUsers" :key="user.id">
                <td class="px-6 py-3  whitespace-nowrap">
                  <div class="flex  items-center">
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
                  <span class="text-gray-900">{{ index + 1 }}</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Invite User Modal -->
    <div v-if="showModal" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center z-20">
      <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full m-4">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-semibold">Invite User</h2>
          <button @click="closeModal" class="text-gray-500 hover:text-gray-700">
            <XIcon class="h-6 w-6" />
          </button>
        </div>
        <form @submit.prevent="sendInvitation" class="space-y-4">
          <div>
            <label for="fullName" class="block text-sm font-medium text-gray-700">Full Name</label>
            <input type="text" id="fullName" v-model="newUser.fullName" placeholder="Enter user full name" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pink-500 focus:border-pink-500 sm:text-sm" required>
          </div>
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">Email Address</label>
            <input type="email" id="email" v-model="newUser.email" placeholder="Enter user email address" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pink-500 focus:border-pink-500 sm:text-sm" required>
          </div>
          <div>
            <label for="designation" class="block text-sm font-medium text-gray-700">Designation</label>
            <select id="designation" v-model="newUser.designation" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pink-500 focus:border-pink-500 sm:text-sm" required>
              <option value="">Select designation</option>
              <option value="Manager">Manager</option>
              <option value="Associate">Associate</option>
              <option value="Leader">Leader</option>
            </select>
          </div>
          <div>
            <label for="mobile" class="block text-sm font-medium text-gray-700">Mobile Number (Optional)</label>
            <div class="mt-1 flex rounded-md shadow-sm">
              <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 sm:text-sm">
                +91
              </span>
              <input type="tel" id="mobile" v-model="newUser.mobile" placeholder="Enter your phone number" class="flex-1 block w-full border border-gray-300 rounded-none rounded-r-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pink-500 focus:border-pink-500 sm:text-sm">
            </div>
          </div>
          <button type="submit" class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#CA2247] hover:bg-pink-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pink-500">
            SEND INVITATION
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { AwardIcon, XIcon } from 'lucide-vue-next'

const users = ref([
  { id: 1, name: 'Abhishek Tyagi', role: 'Leader', email: 'abhishek.tyagi@gmail.com', avatar: '../../public/user.png' },
  { id: 2, name: 'Aayush Kumar', role: 'Associate', email: 'aayush.kumar@gmail.com', avatar: '../../public/user.png' },
  { id: 3, name: 'Binod Sharma', role: 'Associate', email: 'binod.sharma@gmail.com', avatar: '../../public/user.png' },
  { id: 4, name: 'Yax Kumar', role: 'Associate', email: 'yax.kumar@gmail.com', avatar: '../../public/user.png' },
  { id: 5, name: 'Karthik Yadav', role: 'Associate', email: 'karthik.yadav@gmail.com', avatar: '../../public/user.png' },
])

const showModal = ref(false)
const searchQuery = ref('')
const newUser = ref({
  fullName: '',
  email: '',
  designation: '',
  mobile: ''
})

const filteredUsers = computed(() => {
  return users.value.filter(user => 
    user.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})

const openModal = () => {
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
  newUser.value = { fullName: '', email: '', designation: '', mobile: '' }
}

const sendInvitation = () => {
  // Here you would typically send the invitation to the backend
  console.log('Sending invitation to:', newUser.value)
  // Add the new user to the list (in a real app, you'd wait for confirmation from the backend)
  users.value.push({
    id: users.value.length + 1,
    name: newUser.value.fullName,
    role: newUser.value.designation,
    email: newUser.value.email,
    avatar: '../../public/user.png'
  })
  closeModal()
}
</script>

<style scoped>
.radial-gradient {
  background: radial-gradient(circle, rgba(252,231,243,1) 0%, rgba(252,231,243,0) 70%);
}
</style>