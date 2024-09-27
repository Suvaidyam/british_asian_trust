<template>
    <div class="min-h-screen bg-white px-4 sm:px-6 lg:px-16 py-4">
      <div class="mb-6 bg-[#F2E6D4] rounded-lg shadow-md overflow-hidden">
        <div class="p-6 text-center">
          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold mb-4">Welcome, Abhinav! Ready to make an impact?</h1>
          <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
            <button
              class="bg-[#CA2247] hover:bg-red-700 text-white font-bold py-2 px-4 rounded flex items-center justify-center"
            >
              <BellIcon class="h-4 w-4 mr-2" />
              <span class="text-sm leading-tight">FILL OUT YOUR SURVEY</span>
            </button>
            <button
              class="bg-transparent text-[#CA2247] font-semibold py-2 px-4 border border-[#CA2247] rounded shadow flex items-center justify-center"
            >
              <UsersIcon class="h-4 w-4 mr-2" />
              <span class="text-sm leading-tight">INVITE USERS TO JOIN</span>
            </button>
          </div>
        </div>
      </div>
  
      <div class="flex flex-col lg:flex-row gap-4">
        <!-- Announcements Section -->
        <div class="w-full lg:w-3/4 bg-white p-4">
          <h2 class="text-xl font-semibold mb-4">Announcements & Updates</h2>
          <div class="space-y-4">
            <div v-for="announcement in announcements" :key="announcement.id" class="bg-white rounded-lg shadow p-4">
              <div class="flex items-start space-x-4">
                <img :src="announcement.image" :alt="announcement.title" class="w-10 h-10 rounded-full flex-shrink-0" />
                <div>
                  <p class="text-sm">{{ announcement.title }}</p>
                  <p class="text-xs text-gray-500 mt-1">{{ announcement.date }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
  
        <!-- Users Section -->
        <div class="w-full lg:w-1/4 bg-pink-100 rounded-lg p-4">
          <h2 class="text-xl font-semibold mb-4">Users</h2>
          <div class="flex items-center mb-6">
            <div class="relative">
              <img :src="users[0].image" :alt="users[0].name" class="w-16 h-16 rounded-full" />
              <span v-if="users[0].isCrowned" class="absolute top-0 right-0 text-yellow-400 text-xl">👑</span>
            </div>
            <div class="ml-4">
              <p class="font-semibold">{{ users[0].name }}</p>
              <p class="text-sm text-gray-600">View All</p>
            </div>
          </div>
          <div class="flex justify-between mb-6">
            <div v-for="user in users.slice(1, 3)" :key="user.id" class="text-center">
              <img :src="user.image" :alt="user.name" class="w-10 h-10 rounded-full mx-auto" />
              <p class="text-xs mt-1">{{ user.name }}</p>
            </div>
          </div>
          <div class="space-y-2">
            <div v-for="user in topUsers" :key="user.id"
              class="flex items-center bg-white rounded-full py-1 px-3">
              <img :src="`/placeholder.svg?height=24&width=24`" :alt="user.name"
                class="w-6 h-6 rounded-full mr-2" />
              <span class="flex-grow text-sm">{{ user.name }}</span>
              <span class="text-sm font-semibold">+{{ user.score }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { BellIcon, UsersIcon } from 'lucide-vue-next'
  
  const announcements = ref([
    {
      id: 1,
      image: '/placeholder.svg?height=40&width=40',
      title: "We're excited to announce the launch of our new survey on community impact! Participate now to share your insights.",
      date: 'June 2023'
    },
    {
      id: 2,
      image: '/placeholder.svg?height=40&width=40',
      title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys within the first...",
      date: 'June 2023'
    },
  ])
  
  const users = ref([
    {
      id: 1,
      name: 'Meena Kumar',
      image: '/placeholder.svg?height=64&width=64',
      isCrowned: true
    },
    {
      id: 2,
      name: 'Ashok Sharma',
      image: '/placeholder.svg?height=40&width=40',
    },
    {
      id: 3,
      name: 'Jacob Sharma',
      image: '/placeholder.svg?height=40&width=40',
    },
  ])
  
  const topUsers = ref([
    { id: 1, name: 'Aayush Kumar', score: 4 },
    { id: 2, name: 'Gitesh', score: 5 },
    { id: 3, name: 'Umesh Sharma', score: 4 },
  ])
  </script>