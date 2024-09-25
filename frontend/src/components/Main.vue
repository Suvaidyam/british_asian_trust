<template>
    <div class="min-h-screen bg-white px-16 py-4">
        <div
            class="mb-6 bg-gradient-to-r from-[#F2E6D4] to-[#F2E6D8] rounded-lg shadow-md flex justify-center items-center">
            <div class="p-6 ">
                <h1 class="text-[32px] font-bold mb-4">Welcome, Abhinav! Ready to make an impact?</h1>
                <div class="flex justify-center space-x-4">
                    <button
                        class="bg-[#CA2247] h-[38px] hover:bg-red-700 text-white font-bold py-2 px-4 rounded flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
                        </svg>
                        <span class="text-[14px]  leading-[18.34px] font-sans">FILL OUT YOUR SURVEY</span>
                    </button>
                    <button
                        class=" h-[38px] bg-transparent text-[#CA2247] font-semibold py-2 px-4 border border-[#CA2247] rounded shadow flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                        </svg>
                        <span class="text-[14px]  leading-[18.34px] font-sans">INVITE USERS TO JOIN</span>
                    </button>
                </div>
            </div>
        </div>


        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="md:col-span-2">
                <div class="bg-white rounded-lg shadow-md">
                    <div class="p-6">
                        <h2 class="text-xl font-semibold mb-4">Announcements & Updates</h2>
                        <div class="space-y-4">
                            <div v-for="announcement in announcements" :key="announcement.id"
                                class="flex items-start space-x-4">
                                <img :src="announcement.image" :alt="announcement.title" class="w-12 h-12 rounded-full">
                                <div>
                                    <p class="text-sm text-gray-600">{{ announcement.title }}</p>
                                    <p class="text-xs text-gray-400">{{ announcement.date }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div>
                <div class="bg-white rounded-lg shadow-md">
                    <div class="p-6">
                        <div class="flex justify-between items-center mb-4">
                            <h2 class="text-xl font-semibold">Users</h2>
                            <a href="#" class="text-blue-600 hover:underline text-sm">View All</a>
                        </div>
                        <div class="space-y-4">
                            <div v-for="user in users" :key="user.id" class="flex items-center space-x-4">
                                <img :src="user.image" :alt="user.name" class="w-10 h-10 rounded-full">
                                <div>
                                    <p class="font-medium">{{ user.name }}</p>
                                    <p class="text-sm text-gray-500">{{ user.role }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const announcements = ref([
    { id: 1, title: "We're excited to announce the launch of our new survey on community impact! Participate now to share your insights.", date: "June 2023", image: "/placeholder.svg?height=50&width=50" },
    { id: 2, title: "We've updated our points system! Starting next month, you can earn additional points for completing surveys within the first week.", date: "May 2023", image: "/placeholder.svg?height=50&width=50" },
    { id: 3, title: "Join us for an informative webinar on 'Best Practices for NGO Fundraising' on October 15th at 3 PM. Register now to secure your spot.", date: "June 2023", image: "/placeholder.svg?height=50&width=50" },
    { id: 4, title: "Congratulations to sample NGO for successfully completing their first survey! Your feedback is invaluable in driving change.", date: "July 2023", image: "/placeholder.svg?height=50&width=50" },
])

const users = ref([
    { id: 1, name: "Meera Kumar", role: "Manager", image: "/placeholder.svg?height=50&width=50" },
    { id: 2, name: "Ajay Singh", role: "Volunteer", image: "/placeholder.svg?height=50&width=50" },
    { id: 3, name: "Priya Patel", role: "Coordinator", image: "/placeholder.svg?height=50&width=50" },
])
</script>