<script setup lang="ts">
import { ref } from 'vue'
import { ChevronRight, Calendar, XIcon } from 'lucide-vue-next'

const activeTab = ref('overview')
const showPopup = ref(false)
const currentSection = ref('A')

// Define questions for each section
const questions = {
  A: ['What is your opinion on topic A1?', 'What is your opinion on topic A2?'],
  B: ['What is your opinion on topic B1?', 'What is your opinion on topic B2?'],
  C: ['What is your opinion on topic C1?', 'What is your opinion on topic C2?'],
  D: ['What is your opinion on topic D1?', 'What is your opinion on topic D2?'],
  E: ['What is your opinion on topic E1?', 'What is your opinion on topic E2?'],
}

// Define sections data
const sections = [
  {
    title: 'Section A',
    badge: 'Community Champion',
    description: "You've earned the Community Champion badge for demonstrating exceptional impact on your community. Your programs and initiatives are making a meaningful difference in the lives of those you serve.",
    nextSteps: "Continue your efforts to engage with the community and scale your impact. Explore new ways to measure your programs' long-term effectiveness.",
    recommendations: [
      'Lorem ipsum dolor sit amet, consectetur',
      'Lorem ipsum dolor sit amet, consectetur',
      'Lorem ipsum dolor sit amet, consectetur',
      'Lorem ipsum dolor sit amet, consectetur',
      'Lorem ipsum dolor sit amet, consectetur',
    ],
    isExpanded: true
  },
  {
    title: 'Section B',
    badge: 'Community Champion',
    description: "You've earned the Community Champion badge for demonstrating exceptional impact on your community. Your programs and initiatives are making a meaningful difference in the lives of those you serve.",
    nextSteps: "Continue your efforts to engage with the community and scale your impact. Explore new ways to measure your programs' long-term effectiveness.",
    recommendations: [
      'Lorem ipsum dolor sit amet, consectetur',
      'Lorem ipsum dolor sit amet, consectetur',
      'Lorem ipsum dolor sit amet, consectetur',
      'Lorem ipsum dolor sit amet, consectetur',
      'Lorem ipsum dolor sit amet, consectetur',
    ],
    isExpanded: false
  }
]
</script>

<template>
  <div class="min-h-screen bg-gray-100 py-8">
    <div class="px-4 sm:px-6 lg:px-8  max-w-7xl mx-auto">
      <div class="flex flex-col lg:flex-row gap-8">
        <!-- Main Content -->
        <div class="flex-1 bg-white rounded-lg shadow-lg overflow-hidden">
          <div class="p-4 sm:p-6 md:p-8">
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

            <img src="../assets/assessiment.png" alt="Person writing on paper"
              class="w-full h-48 sm:h-64 object-cover rounded-lg mb-6" />

            <div class="mb-6">
              <div class="flex border-b border-gray-200">
                <button v-for="tab in ['overview', 'sections']" :key="tab" @click="activeTab = tab" :class="[
                  'px-4 py-2 text-sm font-medium focus:outline-none transition-colors duration-200',
                  activeTab === tab
                    ? 'border-b-2 border-[#CA2247] text-[#CA2247]'
                    : 'text-gray-500 hover:text-gray-700'
                ]">
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
              <div v-for="(section, index) in sections" :key="index"
                class="bg-white rounded-lg shadow-sm p-4 sm:p-6 space-y-4 mt-5">
                <div class="flex justify-between items-center">
                  <h2 class="text-lg font-semibold text-gray-700">{{ section.title }}</h2>
                  <button @click="section.isExpanded = !section.isExpanded" class="text-gray-400">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd"
                        d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                        clip-rule="evenodd" />
                    </svg>
                  </button>
                </div>

                <div v-if="section.isExpanded" class="space-y-4">
                  <div class="flex items-center space-x-2">
                    <span class="text-sm font-medium text-gray-700">{{ section.badge }}</span>
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-yellow-400" viewBox="0 0 20 20"
                      fill="currentColor">
                      <path fill-rule="evenodd"
                        d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                        clip-rule="evenodd" />
                    </svg>
                  </div>

                  <p class="text-sm text-gray-600">{{ section.description }}</p>

                  <div>
                    <h3 class="text-sm font-medium text-gray-700">Next steps</h3>
                    <p class="text-sm text-gray-600">{{ section.nextSteps }}</p>
                  </div>

                  <div>
                    <h3 class="text-sm font-medium text-gray-700">Recommendations</h3>
                    <ul class="list-disc list-inside space-y-1">
                      <li v-for="(recommendation, recIndex) in section.recommendations" :key="recIndex"
                        class="text-sm text-yellow-600">
                        {{ recommendation }}
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- Sidebar -->
        <div class="lg:w-1/4 space-y-6">
          <div class="bg-[#CA2247] text-white p-6 rounded-lg shadow-md">
            <h2 class="text-xl font-bold mb-4">Ready to take the survey?</h2>
            <button @click="showPopup = true"
              class="w-full bg-white text-[#CA2247] font-semibold py-2 px-4 rounded hover:bg-gray-100 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-[#CA2247] focus:ring-white">
              START ASSESSMENT
            </button>
          </div>
          <div class="bg-white shadow-lg rounded-lg overflow-hidden">
            <div class="bg-red-600 text-white p-4">
              <h2 class="text-xl font-bold mb-2">Check your score here</h2>
              <button class="bg-white text-red-600 px-4 py-2 rounded font-semibold hover:bg-red-100 transition-colors">
                DOWNLOAD REPORT CARD
              </button>
            </div>
            <div class="p-4">
              <h3 class="text-lg font-semibold mb-2">Achievements</h3>
              <div class="flex items-center mb-4">
                <div class="bg-yellow-400 rounded-full p-2 mr-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                  </svg>
                </div>
                <span class="font-semibold">Impact Innovator</span>
              </div>
              <p class="text-sm text-gray-600 mb-4">
                As an Impact Innovator, you've demonstrated exceptional skills in driving positive change and
                innovation.
              </p>
              <h3 class="text-lg font-semibold mb-2">Recommendations</h3>
              <ul class="space-y-2">
                <li v-for="i in 5" :key="i" class="flex items-start">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400 mr-2 mt-0.5" fill="none"
                    viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                  </svg>
                  <span class="text-sm text-gray-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Popup -->
    <Transition name="fade">
      <div v-if="showPopup"
        class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center z-50">
        <div class="bg-white p-4 sm:p-6 md:p-8 rounded-lg shadow-xl w-full max-w-2xl m-4">
          <div class="flex justify-between items-center mb-6">
            <h2 class="text-xl font-bold text-gray-800">Assessment Sample Test</h2>
            <button @click="showPopup = false" class="text-gray-500 hover:text-gray-700 focus:outline-none">
              <XIcon class="h-6 w-6" />
            </button>
          </div>

          <div class="mb-6">
            <div class="flex space-x-2 mb-4 overflow-x-auto pb-2">
              <button v-for="section in ['A', 'B', 'C', 'D', 'E']" :key="section" @click="currentSection = section"
                :class="[
                  'px-3 py-1 rounded text-sm font-medium focus:outline-none transition-colors duration-200',
                  currentSection === section ? 'bg-[#CA2247] text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                ]">
                Section {{ section }}
              </button>
            </div>

            <div v-for="(question, index) in questions[currentSection]" :key="index" class="mb-4">
              <label :for="`question-${index}`" class="block text-gray-700 text-sm font-bold mb-2">{{ question
                }}</label>
              <select :id="`question-${index}`"
                class="block appearance-none w-full bg-white border border-gray-300 hover:border-gray-400 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:ring-2 focus:ring-[#CA2247]">
                <option value="">Select an option</option>
                <option value="1">Option 1</option>
                <option value="2">Option 2</option>
                <option value="3">Option 3</option>
              </select>
            </div>
          </div>

          <div class="flex flex-col sm:flex-row justify-end space-y-2 sm:space-y-0 sm:space-x-4">
            <button
              class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-gray-500">
              SAVE AS DRAFT
            </button>
            <button
              class="bg-[#CA2247] hover:bg-[#A61C39] text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-[#CA2247]">
              SAVE & NEXT
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>