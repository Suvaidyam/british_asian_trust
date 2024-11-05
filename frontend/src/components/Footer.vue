<template>
  <footer class="bg-[#0D4688] text-white py-4 px-6">
    <div class="flex flex-col sm:flex-row justify-between items-center max-w-[1920px] mx-auto w-full">
      <div class="font-poppins text-[14px] font-normal leading-[18.34px] tracking-[0.0025em] mb-2 sm:mb-0">
        © {{ currentYear }} All Rights Reserved
      </div>
      <div class="flex flex-col sm:flex-row items-center">
        <div class="font-poppins text-[14px] font-normal leading-[18.34px] tracking-[0.0025em] mb-2 sm:mb-0 sm:mr-4">
          <router-link to="/data-privacy-policy" class="hover:underline">Data Privacy Policy</router-link>
          <span class="mx-2">•</span>
          <router-link to="/copyright-policy" class="hover:underline">Copyright Policy</router-link>
        </div>
        <div class="flex space-x-4">
          <router-link to="/facebook" class="hover:text-gray-300 bg-white rounded-full p-1">
            <FacebookIcon class="w-5 h-5 text-[#0D4688]" />
          </router-link>
          <router-link to="/twitter" class="hover:text-gray-300 bg-white rounded-full p-1">
            <TwitterIcon class="w-5 h-5 text-[#0D4688]" />
          </router-link>
          <router-link to="/linkedin" class="hover:text-gray-300 bg-white rounded-full p-1">
            <LinkedinIcon class="w-5 h-5 text-[#0D4688]" />
          </router-link>
          <router-link to="/youtube" class="hover:text-gray-300 bg-white rounded-full p-1">
            <YoutubeIcon class="w-5 h-5 text-[#0D4688]" />
          </router-link>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import { FacebookIcon, TwitterIcon, LinkedinIcon, YoutubeIcon } from 'lucide-vue-next'

const currentYear = ref(new Date().getFullYear())
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

body {
  font-family: 'Poppins', sans-serif;
}
</style>