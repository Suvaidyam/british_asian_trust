<template>
    <footer class="bg-[#0D4688] text-white py-4 px-6 flex flex-col sm:flex-row justify-between items-center max-w-[2048px] mx-auto w-full">
      <div class="text-sm mb-2 sm:mb-0">
        © {{ currentYear }} All Rights Reserved
      </div>
      <div class="flex flex-col sm:flex-row items-center">
        <div class="text-sm mb-2 sm:mb-0 sm:mr-4">
          <a href="#" class="hover:underline">Data Privacy Policy</a>
          <span class="mx-2">•</span>
          <a href="#" class="hover:underline">Copyright Policy</a>
        </div>
        <div class="flex space-x-4">
          <a href="#" class="hover:text-gray-300">
            <FacebookIcon class="w-5 h-5" />
          </a>
          <a href="#" class="hover:text-gray-300">
            <TwitterIcon class="w-5 h-5" />
          </a>
          <a href="#" class="hover:text-gray-300">
            <LinkedinIcon class="w-5 h-5" />
          </a>
          <a href="#" class="hover:text-gray-300">
            <YoutubeIcon class="w-5 h-5" />
          </a>
        </div>
      </div>
    </footer>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { FacebookIcon, TwitterIcon, LinkedinIcon, YoutubeIcon } from 'lucide-vue-next'
  
  const currentYear = ref(new Date().getFullYear())
  </script>