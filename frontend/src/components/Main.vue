<template>
  <div class="min-h-screen bg-white px-4 sm:px-6 lg:px-16 py-4">
    <div class="mb-6 bg-[#F2E6D4] bg-main-img rounded-lg shadow-md overflow-y-scroll">
      <div class="p-6 text-center">
        <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold mb-4">Welcome, Abhinav! Ready to make an impact?</h1>
        <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
          <button
            class="bg-[#CA2247] hover:bg-red-700 text-white font-bold py-2 px-4 rounded flex items-center justify-center">
            <BellIcon class="h-4 w-4 mr-2" />
            <a href="/assessment"  class="text-sm leading-tight">FILL OUT YOUR SURVEY</a >
          </button>
          <button
            class="bg-transparent text-[#CA2247] font-semibold py-2 px-4 border border-[#CA2247] rounded shadow flex items-center justify-center">
            <UsersIcon class="h-4 w-4 mr-2" />
            <a href="/myuser" class="text-sm leading-tight">INVITE USERS TO JOIN</a>
          </button>
        </div>
      </div>
    </div>

    <!-- Main content -->
    <div class="flex flex-col lg:flex-row gap-4">
      <!-- Announcements Section -->
      <div class="w-full  lg:w-3/4 bg-white ">
        <h2 class="text-xl font-semibold mb-4">Announcements & Updates</h2>
        <div class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-2 gap-4">
          <div v-for="announcement in announcements" :key="announcement.id"
            class="bg-white rounded-lg shadow p-2.5 flex items-center space-x-2">
            <img src="../assets/main_bg.png" :alt="announcement.title" class="w-12 h-12 rounded-lg  object-cover" />
            <div>
              <h3 class="text-[14px] leading-[15.4px]">{{ announcement.title }}</h3>
              <p class="text-xs text-gray-500">{{ announcement.date }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Users Section -->
      <div class="w-full lg:w-1/4 bg-pink-100 rounded-lg p-4">
        <!-- Title with View All link -->
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-semibold">Users</h2>
          <a href="/myuser" class="text-sm text-gray-600 cursor-aointer hover:underline">View All</a>
        </div>

        <!-- Main User (Crowned User) -->
        <div class="flex flex-col items-center mb-6">
          <div class="relative">
            <!-- User Image -->
            <img :src="users[0].image" :alt="users[0].name" class="w-24 h-24 rounded-full shadow-md" />
            <span v-if="users[0].isCrowned"
              class="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-yellow-400 text-4xl">👑</span>
          </div>
            <!-- Crown Icon Centered on Top -->
          <!-- Main User Name -->
          <p class="mt-2 font-semibold text-sm">{{ users[0].name }}</p>
        </div>

        <!-- Smaller Users (List of Users) -->
        <div class="flex justify-between mb-6">
          <div v-for="user in users.slice(1, 3)" :key="user.id" class="text-center">
            <!-- User Image -->
            <img :src="user.image" :alt="user.name" class="w-14 h-14 rounded-full mx-auto shadow-sm" />
            <!-- User Name -->
            <p class="text-xs mt-1">{{ user.name }}</p>
          </div>
        </div>

        <!-- Top Users with Scores -->
        <div class="space-y-2 ">
          <div v-for="user in topUsers" :key="user.id"
            class="flex items-center bg-white  py-2 px-3 shadow-sm">
            <img :src="user.image || '/placeholder.svg?height=24&width=24'" :alt="user.name"
              class="w-6 h-6 rounded-full mr-2" />
            <!-- Top User Name -->
            <span class="flex-grow text-sm">{{ user.name }}</span>
            <!-- Score -->
            <span class="text-sm font-semibold text-gray-700">+{{ user.score }}</span>
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
    image: '../assets/main_bg.png',
    title: "We're excited to announce the launch of our new survey on community impact! Participate now to share your insights.",
    date: 'June 2023'
  },
  {
    id: 2,
    image: '../assets/assessiment.png',
    title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys.",
    date: 'June 2023'
  },
  {
    id: 3,
    image: '../assets/main_bg.png',
    title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys.",
    date: 'June 2023'
  },
  {
    id: 5,
    image: '../assets/main_bg.png',
    title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys.",
    date: 'June 2023'
  },
  {
    id: 5,
    image: '../assets/main_bg.png',
    title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys.",
    date: 'June 2023'
  },
  {
    id: 6,
    image: '../assets/main_bg.png',
    title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys.",
    date: 'June 2023'
  },
  {
    id: 1,
    image: '../assets/main_bg.png',
    title: "We're excited to announce the launch of our new survey on community impact! Participate now to share your insights.",
    date: 'June 2023'
  },
  {
    id: 2,
    image: '../assets/assessiment.png',
    title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys.",
    date: 'June 2023'
  },
  {
    id: 3,
    image: '../assets/main_bg.png',
    title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys.",
    date: 'June 2023'
  },
  {
    id: 5,
    image: '../assets/main_bg.png',
    title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys.",
    date: 'June 2023'
  },
  {
    id: 5,
    image: '../assets/main_bg.png',
    title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys.",
    date: 'June 2023'
  },
  {
    id: 6,
    image: '../assets/main_bg.png',
    title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys.",
    date: 'June 2023'
  },
  // Add more announcements here
])

const users = ref([
  {
    id: 1,
    name: 'Meena Kumar',
    image: '../assets/main_bg.png',
    isCrowned: true
  },
  {
    id: 2,
    name: 'Ashok Sharma',
    image: '../assets/main_bg.png',
  },
  {
    id: 3,
    name: 'Jacob Sharma',
    image: '../assets/main_bg.png',
  },
])

const topUsers = ref([
  { id: 1, name: 'Aayush Kumar', score: 4 },
  { id: 2, name: 'Gitesh', score: 5 },
  { id: 3, name: 'Umesh Sharma', score: 4 },
])
</script>

<style scoped>
/* Additional styles if needed */
</style>
