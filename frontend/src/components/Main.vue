<template>
  <div class="min-h-screen bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
      <div class="mb-6 bg-[#F2E6D4] bg-main-img bg-cover bg-center rounded-lg shadow-md overflow-hidden">
        <div class="p-4 sm:p-6 lg:p-8 text-center">
          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold mb-4 text-gray-800">Welcome, Abhinav! Ready to make an impact?</h1>
          <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
            <a href="/assessment" class="inline-flex items-center justify-center bg-[#CA2247] hover:bg-red-700 text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out">
              <BellIcon class="h-5 w-5 mr-2" />
              <span class="text-sm leading-tight">FILL OUT YOUR SURVEY</span>
            </a>
            <a href="/myuser" class="inline-flex items-center justify-center bg-transparent text-[#CA2247] font-semibold py-2 px-4 border border-[#CA2247] rounded shadow hover:bg-[#CA2247] hover:text-white transition duration-300 ease-in-out">
              <UsersIcon class="h-5 w-5 mr-2" />
              <span class="text-sm leading-tight">INVITE USERS TO JOIN</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Main content -->
      <div class="flex flex-col lg:flex-row gap-6">
        <!-- Announcements Section -->
        <div class="w-full lg:w-3/4">
          <h2 class="text-xl font-semibold mb-4">Announcements & Updates</h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-4">
            <div v-for="announcement in announcements" :key="announcement.id"
              class="bg-white rounded-lg shadow-md p-2 flex items-start space-x-3 hover:shadow-lg transition duration-300 ease-in-out">
              <img src="../assets/main_bg.png" :alt="announcement.title" class="w-16 h-16 rounded-lg object-cover flex-shrink-0" />
              <div>
                <h3 class="text-sm font-medium leading-snug">{{ announcement.title }}</h3>
                <p class="text-xs text-gray-500">{{ announcement.date }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Users Section -->
        <div class="w-full lg:w-1/4 bg-pink-100 rounded-lg p-4 shadow-md">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-semibold">Users</h2>
            <a href="/myuser" class="text-sm text-gray-600 hover:text-[#CA2247] transition duration-300 ease-in-out">View All</a>
          </div>

          <!-- Main User (Crowned User) -->
          <div class="flex flex-col items-center mb-6">
            <div class="relative">
              <img :src="users[0].image" :alt="users[0].name" class="w-24 h-24 rounded-full shadow-md" />
              <span v-if="users[0].isCrowned"
                class="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-yellow-400 text-4xl">👑</span>
            </div>
            <p class="mt-2 font-semibold text-sm">{{ users[0].name }}</p>
          </div>

          <!-- Smaller Users (List of Users) -->
          <div class="flex justify-around mb-6">
            <div v-for="user in users.slice(1, 3)" :key="user.id" class="text-center">
              <img :src="user.image" :alt="user.name" class="w-16 h-16 rounded-full mx-auto shadow-sm" />
              <p class="text-xs mt-2">{{ user.name }}</p>
            </div>
          </div>

          <!-- Top Users with Scores -->
          <div class="space-y-3">
            <div v-for="user in topUsers" :key="user.id"
              class="flex items-center bg-white rounded-lg py-2 px-3 shadow-sm hover:shadow-md transition duration-300 ease-in-out">
              <img :src="user.image" :alt="user.name" class="w-8 h-8 rounded-full mr-3" />
              <span class="flex-grow text-sm font-medium">{{ user.name }}</span>
              <span class="text-sm font-semibold text-gray-700">+{{ user.score }}</span>
            </div>
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
    title: "Join our upcoming webinar on sustainable development practices in NGOs. Register now!",
    date: 'July 2023'
  },
  {
    id: 4,
    image: '../assets/main_bg.png',
    title: "New partnership announcement: We're collaborating with local schools to promote education initiatives.",
    date: 'July 2023'
  },
  {
    id: 5,
    image: '../assets/main_bg.png',
    title: "Volunteer opportunity: Join us for a community clean-up event this weekend. Sign up today!",
    date: 'August 2023'
  },
  {
    id: 6,
    image: '../assets/main_bg.png',
    title: "Congratulations to our top contributors! Check out the leaderboard to see if you made it.",
    date: 'August 2023'
  }
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
  { id: 1, name: 'Aayush Kumar', score: 4, image: '../assets/main_bg.png' },
  { id: 2, name: 'Gitesh', score: 5, image: '../assets/main_bg.png' },
  { id: 3, name: 'Umesh Sharma', score: 4, image: '../assets/main_bg.png' },
])
</script>

<style scoped>
/* Additional styles if needed */
</style>