<template>
    <div class="min-h-screen bg-gray-100 py-8 ">
      <div class=" px-16">
        <div class="flex flex-col lg:flex-row gap-8">
          <!-- Main Content -->
          <div class="flex-1 bg-white rounded-lg shadow-lg overflow-hidden">
            <div class="p-6 sm:p-8">
              <nav class="text-sm mb-4">
                <a href="#" class="text-gray-500 hover:text-gray-700">Home</a>
                <ChevronRight class="inline-block w-4 h-4 text-gray-500 mx-1" />
                <span class="text-gray-700">Assessment</span>
              </nav>
              <div class="flex justify-between items-center mb-6 flex-col sm:flex-row">
                <h1 class="text-2xl font-bold text-gray-800">Assessment Sample Test</h1>
                <p class="text-sm text-gray-600 mt-2 sm:mt-0">
                  <Calendar class="inline-block w-4 h-4 mr-1" />
                  Posted on: September 20, 2024
                </p>
              </div>
  
              <img
                src="../assets/assessiment.png"
                alt="Person writing on paper"
                class="w-full h-48 sm:h-64 object-cover rounded-lg mb-6"
              />
  
              <div class="mb-6">
                <div class="flex border-b border-gray-200">
                  <button
                    v-for="tab in ['overview', 'sections']"
                    :key="tab"
                    @click="activeTab = tab"
                    :class="[
                      'px-4 py-2 text-sm font-medium focus:outline-none transition-colors duration-200',
                      activeTab === tab
                        ? 'border-b-2 border-[#CA2247] text-[#CA2247]'
                        : 'text-gray-500 hover:text-gray-700'
                    ]"
                  >
                    {{ tab.charAt(0).toUpperCase() + tab.slice(1) }}
                  </button>
                </div>
              </div>
  
              <div v-if="activeTab === 'overview'" class="text-sm text-gray-600 space-y-4">
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat.
                </p>
                <p>
                  Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque
                  laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto
                  beatae vitae dicta sunt explicabo.
                </p>
                <h2 class="text-lg font-semibold text-gray-800 mt-6 mb-2">
                  Survey Impact: Why Your Participation Matters
                </h2>
                <ol class="list-decimal pl-5 space-y-2">
                  <li>Improve Our Understanding: The data collected from this survey will help us better
                    understand the effectiveness of our current processes and identify areas for improvement.
                  </li>
                  <li>Funding and Resource Allocation: Survey responses provide valuable insights that allow us to
                    secure funding from donors and allocate resources where they are needed most.
                  </li>
                  <li>Community Empowerment: Your input will help us understand the needs of the communities we
                    serve, ensuring that our programs are more inclusive, sustainable, and impactful.
                  </li>
                </ol>
              </div>
  
              <div v-else-if="activeTab === 'sections'" class="text-sm text-gray-600">
                <p>Sections content goes here.</p>
              </div>
            </div>
          </div>
  
          <!-- Sidebar -->
          <div class="lg:w-1/4 space-y-6">
            <div class="bg-[#CA2247] text-white p-6 rounded-lg shadow-md">
              <h2 class="text-xl font-bold mb-4">Ready to take the survey?</h2>
              <button
                @click="showPopup = true"
                class="w-full bg-white text-[#CA2247] font-semibold py-2 px-4 rounded hover:bg-gray-100 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-[#CA2247] focus:ring-white"
              >
                START ASSESSMENT
              </button>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-md">
              <h2 class="text-lg font-semibold mb-4">Quick Links</h2>
              <ul class="space-y-2">
                <li v-for="link in ['FAQ', 'Contact Us', 'Privacy Policy']" :key="link">
                  <a href="#" class="text-[#CA2247] hover:underline">{{ link }}</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  
    <!-- Popup -->
    <Transition name="fade">
      <div v-if="showPopup" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
        <div class="bg-white p-6 rounded-lg max-w-md w-full">
          <h2 class="text-xl font-bold mb-4">Start Assessment</h2>
          <p class="mb-6 text-gray-600">Are you ready to begin the assessment? This will take approximately 15 minutes to complete.</p>
          <div class="flex justify-end space-x-4">
            <button
              @click="showPopup = false"
              class="px-4 py-2 border rounded text-gray-600 hover:bg-gray-100 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-gray-300"
            >
              Cancel
            </button>
            <button
              class="px-4 py-2 bg-[#CA2247] text-white rounded hover:bg-[#A61C39] transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#CA2247]"
            >
              Start
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  import { ChevronRight, Calendar } from 'lucide-vue-next'
  
  const activeTab = ref('overview')
  const showPopup = ref(false)
  </script>
  
  <style scoped>
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.3s ease;
  }
  
  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
  </style>