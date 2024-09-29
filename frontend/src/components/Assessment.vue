<template>
  <div class="min-h-screen bg-gray-100 py-8">
    <div class="px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      <div class="flex flex-col lg:flex-row gap-8">
        <!-- Main Content -->
        <div class="flex-1 bg-white rounded-lg shadow-lg overflow-hidden">
          <div class="p-6 sm:p-8">
            <nav class="text-sm mb-6">
              <a href="#" class="text-gray-500 hover:text-gray-700">Home</a>
              <ChevronRight class="inline-block w-4 h-4 text-gray-500 mx-1" />
              <span class="text-gray-700">Assessment</span>
            </nav>
            <div class="flex justify-between items-center mb-6 flex-col sm:flex-row">
              <h1 class="text-2xl font-semibold text-gray-800">Assessment Sample Test</h1>
              <p class="text-sm text-gray-600 mt-2 sm:mt-0 flex items-center">
                <Calendar class="w-4 h-4 mr-1" />
                Posted on: September 20, 2024
              </p>
            </div>

            <img src="/assessiment.png" alt="Person writing on paper"
              class="w-full h-48 sm:h-64 object-cover rounded-lg mb-8" />

            <div class="mb-8">
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

            <div v-if="activeTab === 'overview'" class="text-sm text-gray-600 space-y-6">
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
              <h2 class=" text-sm text-gray-800 mt-8 mb-4">
                Survey Impact: Why Your Participation Matters
              </h2>
              <ol class="list-decimal pl-5 space-y-4">
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

            <div v-else-if="activeTab === 'sections'" class="space-y-6">
              <div v-for="(section, index) in sections" :key="index"
                class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
                <div class="p-6 space-y-4">
                  <div class="flex justify-between items-center">
                    <h2 class="text-xl font-semibold text-gray-800">{{ section.title }}</h2>
                    <button @click="section.isExpanded = !section.isExpanded" class="text-gray-400 hover:text-gray-600">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" :class="{ 'transform rotate-180': section.isExpanded }" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd"
                          d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                          clip-rule="evenodd" />
                      </svg>
                    </button>
                  </div>

                  <div v-if="section.isExpanded" class="space-y-4">
                    <div class="flex items-center space-x-2">
                      <span class="text-sm font-medium text-gray-700 bg-yellow-100 px-2 py-1 rounded-full">{{ section.badge }}</span>
                    </div>

                    <p class="text-sm text-gray-600">{{ section.description }}</p>

                    <div>
                      <h3 class="text-sm font-medium text-gray-700 mb-2">Next steps</h3>
                      <p class="text-sm text-gray-600">{{ section.nextSteps }}</p>
                    </div>

                    <div>
                      <h3 class="text-sm font-medium text-gray-700 mb-2">Recommendations</h3>
                      <ul class="list-disc list-inside space-y-1">
                        <li v-for="(recommendation, recIndex) in section.recommendations" :key="recIndex"
                          class="text-sm text-gray-600">
                          {{ recommendation }}
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- Sidebar -->
        <div class="lg:w-1/4 space-y-6">
          <div class="bg-gradient-to-r from-[#CA2247] to-[#FF4D6D] bg-assessment text-white p-6 rounded-lg shadow-md">
            <h2 class=" mb-4">Ready to take the survey?</h2>
            <button @click="showPopup = true"
              class="bg-white text-[#CA2247]  text-sm py-2 px-4 rounded hover:bg-gray-100 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-[#CA2247] focus:ring-white">
              START ASSESSMENT
            </button>
          </div>
          
          <div class="bg-gradient-to-r from-[#CA2247] to-[#FF4D6D] bg-assessment text-white p-6 rounded-lg shadow-md">
            <h2 class=" mb-4">Check your score here</h2>
            <button @click="showReportCardPopup = true"
              class="bg-white text-[#CA2247] text-sm py-2 px-4 rounded hover:bg-gray-100 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-[#CA2247] focus:ring-white">
              DOWNLOAD REPORT CARD
            </button>
          </div>

          <div class="bg-white shadow-lg rounded-lg overflow-hidden p-6">
            <h3 class=" mb-4">Achievements</h3>
            <div class="flex items-center justify-center mb-6">
              <div class="bg-gradient-to-r from-yellow-400 to-yellow-300 rounded-full p-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 text-white" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                </svg>
              </div>
            </div>
            <h3 class=" text-center mb-2">Impact Innovator</h3>
            <p class="text-sm text-gray-600 text-center">
              As an Impact Innovator, you've demonstrated exceptional skills in driving positive change and
              innovation.
            </p>
          </div>
          
          <div class="bg-white shadow-lg rounded-lg overflow-hidden p-6">
            <h3 class=" mb-4">Recommendations</h3>
            <ul class="space-y-3">
              <li v-for="i in 5" :key="i" class="flex items-start">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-[#CA2247] mr-2 mt-0.5" fill="none"
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

    <!-- Assessment Popup -->
    <Transition name="fade">
      <div v-if="showPopup"
        class="fixed inset-0 bg-black bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center z-50">
        <div class="bg-white p-6 rounded-lg shadow-xl w-full max-w-2xl m-4">
          <div class="flex justify-between items-center mb-6">
            <h2 class="text-2xl font-semibold text-gray-800">Assessment Sample Test</h2>
            <button @click="showPopup = false" class="text-gray-500 hover:text-gray-700 focus:outline-none">
              <XIcon class="h-6 w-6" />
            </button>
          </div>

          <div class="mb-6">
            <div class="flex space-x-2 mb-6  border-b overflow-x-auto ">
              <button v-for="section in ['A', 'B', 'C', 'D', 'E']" :key="section" @click="currentSection = section"
                :class="[
                  'px-4 py-2 text-sm font-medium focus:outline-none transition-colors duration-200',
                  currentSection === section ? ' border-b-2  border-[#CA2247] text-gray-900' : 'text-gray-500 hover:text-gray-700'
                ]">
                Section {{ section }}
              </button>
            </div>

            <div v-for="(question, index) in questions[currentSection]" :key="index" class="mb-6">
              <label :for="`question-${index}`" class="block text-gray-700 text-sm font-bold mb-2">{{ question }}</label>
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
              class="bg-white border text-sm border-gray-300 hover:bg-gray-100 text-gray-800 py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-gray-500">
              SAVE AS DRAFT
            </button>
            <button
              class="bg-[#CA2247] text-sm hover:bg-[#A61C39] text-white  py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-[#CA2247]">
              SAVE & NEXT
            </button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Report Card Download Popup -->
    <Transition name="fade">
      <div v-if="showReportCardPopup" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
        <div class="bg-white rounded-lg shadow-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
          <div class="flex justify-between items-center p-6 border-b">
            <h2 class="text-2xl font-semibold text-gray-800">Report Card</h2>
            <button @click="showReportCardPopup = false" class="text-gray-500 hover:text-gray-700">
              <XIcon class="h-6 w-6" />
            </button>
          </div>
          <div class="p-6">
            <div class="grid grid-cols-2 gap-4 mb-6">
              <div>
                <p class="text-sm text-gray-600">Name:</p>
                <p class="font-semibold">Abhinav Tyagi</p>
              </div>
              <div>
                <p class="text-sm text-gray-600">Assessment:</p>
                <p class="font-semibold">Assessment A</p>
              </div>
              <div>
                <p class="text-sm text-gray-600">Date Completed:</p>
                <p class="font-semibold">September 22, 2024</p>
              </div>
            </div>
            <div class="mb-6">
              <h3 class="text-md font-semibold mb-2">Overall Rating</h3>
              <div class="flex items-center bg-yellow-100 p-4 rounded-lg">
                <svg class="w-8 h-8 text-yellow-400 mr-3" fill="currentColor" viewBox="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z">
                  </path>
                </svg>
                <div>
                  <p class=" text-lg">Impact Innovator</p>
                  <p class="text-sm text-gray-600">You've earned the Impact Innovator badge for demonstrating
                    exceptional skills across various areas. Keep innovating and pushing boundaries to drive more
                    impact!</p>
                </div>
              </div>
            </div>
            <div class="mb-6">
              <h3 class="text-lg font-semibold mb-2">Section Breakdown</h3>
              <div class="bg-gray-100 p-4 rounded-lg mb-4">
                <h4 class="font-semibold mb-2">Section A</h4>
                <div class="flex items-start">
                  <svg class="w-6 h-6 text-green-500 mr-3 mt-1" fill="currentColor" viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clip-rule="evenodd"></path>
                  </svg>
                  <div>
                    <p class="font-semibold">Community Champion</p>
                    <p class="text-sm text-gray-600">You've earned the Community Champion badge for demonstrating
                      exceptional efforts in benefiting the community. Your initiatives have made a significant positive
                      impact!</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="bg-blue-100 p-4 rounded-lg">
              <h3 class="text-lg font-semibold mb-2">Recommendations</h3>
              <ul class="list-disc list-inside text-sm text-gray-700">
                <li>Explore advanced community engagement strategies.</li>
                <li>Strengthen partnerships within the community to sustain long-term success.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ChevronRight, Calendar, XIcon } from 'lucide-vue-next'

const activeTab = ref('overview')
const showPopup = ref(false)
const currentSection = ref('A')
const showReportCardPopup = ref(false)

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

const downloadReportCard = () => {
  // Simulating download process
  console.log('Downloading report card...')
  // You can implement the actual download logic here
  showReportCardPopup.value = false
}
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