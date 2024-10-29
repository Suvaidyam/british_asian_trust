<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-100 via-green-100 to-teal-100 p-4 md:p-8">
    <div class="max-w-[2048px] mx-auto bg-white rounded-lg shadow-lg overflow-hidden">
      <div class="p-6 md:p-8">
        <div class="flex flex-col lg:flex-row gap-8">
          <div class="lg:w-3/4">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-4">
              <h1 class="text-3xl md:text-4xl font-bold text-blue-900">Assessment Sample Test</h1>
              <div class="text-sm text-gray-500 mt-2 sm:mt-0">Posted on: September 20, 2024</div>
            </div>
            <img src="../../public/assessiment.png" alt="Person writing on paper"
              class="w-full h-64 md:h-auto object-cover rounded-lg mb-4" />
            <div class="space-y-4 text-gray-700">
              <p>
                The survey is divided into two sections - organizational/erganisational level and program level. The
                first addresses overarching organizational practices and systems that cover all aspects of your work.
                The second section focuses specifically on one of your chosen program areas, delving deeper into its
                operations and implementation. s key aspects that apply broadly across all areas of your work and the
                second dives deeper into understanding one of your chosen program areas.
              </p>
              <ul class="list-disc pl-5 space-y-2">
                <li>Provide accurate and candid responses. The survey is designed to evaluatesurvey-aims to assess the
                  organization's current capacity and identify areas for improvement, so honesty will yield the most
                  valuable insights.</li>
                <li>Focus on your organization's current status, not what you aspire to achieve (unless otherwise asked
                  in the question). Answer questions based on existing practices and systems, in place. not future
                  aspirations, unless otherwise specified in the question.</li>
                <li>We strongly recommendenceurage you to conducting an internal exercise before takingfilling this
                  survey.</li>
              </ul>
              <p>
                Consider asking different-team members from various departments ((e.g., finance, program, HR, etc.) to
                provide their inputs. fill out-the survey independently. Include input fr rom multiple departments
                (e.g., finance, program, M&E, HR, etc.) to capture a holistic view of the organization's capabilities.
                Engage senior leaders for strategic questions and operational teams for implementation-focuseslevel
                questions insights.
              </p>
              <p>
                Focus on your organization's current status, not what you aspire to achieve (unless otherwise asked in
                the question). Answer questions based on existing practices and systems, in place. not future
                aspirations, unless otherwise specified in the question. If any questions seem unclear, or if you need
                further clarification, please reach out to us. For guidance before completing the survey.
              </p>
            </div>
          </div>
          <div class="lg:w-1/4 mt-8 lg:mt-0">
            <div class="bg-blue-900 text-white p-6 rounded-lg mb-6">
              <h2 class="text-xl font-semibold mb-4">Ready to take the survey?</h2>
              <button
                class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded transition duration-300 w-full">
                START ASSESSMENT
              </button>
            </div>
            <div class="bg-white border border-gray-200 rounded-lg p-4">
              <div class="flex justify-between items-center mb-4">
                <h2 class="text-lg font-semibold text-gray-900">Users</h2>
                <button @click="openPopup"
                  class="bg-blue-500 hover:bg-blue-600 text-white rounded-full w-6 h-6 flex items-center justify-center transition duration-300">
                  <span class="text-xl leading-none">+</span>
                </button>
              </div>
              <ul class="space-y-4">
                <li v-for="user in users" :key="user.id" class="flex items-center gap-3">
                  <img :src="user.avatar" :alt="user.name" class="w-10 h-10 rounded-full" />
                  <div>
                    <p class="font-medium text-gray-900">{{ user.name }}</p>
                    <p class="text-sm text-gray-500">{{ user.role }}</p>
                    <p class="text-xs text-gray-400">Joining Date: {{ user.joiningDate }}</p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Popup -->
    <div v-if="isPopupOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-lg shadow-xl w-full max-w-2xl">
        <div class="flex justify-between items-center border-b p-4">
          <h2 class="text-xl font-semibold">Invite User</h2>
          <button @click="closePopup" class="text-gray-500 hover:text-gray-700">
            <span class="sr-only">Close</span>
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        <div class="p-4">
          <div class="flex mb-4">
            <input v-model="inviteInput" type="text" placeholder="Invite others by name or email"
              class="flex-grow border rounded-l-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500" />
            <button :class="[
              'px-4 py-2 rounded-r-lg transition duration-300',
              inviteInput ? 'bg-orange-500 hover:bg-orange-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            ]">
              INVITE
            </button>
          </div>
          <ul class="space-y-3 max-h-80 overflow-y-auto">
            <li v-for="user in inviteUsers" :key="user.id" class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <img :src="user.avatar" :alt="user.name" class="w-10 h-10 rounded-full" />
                <div>
                  <p class="font-medium">{{ user.name }}</p>
                  <p class="text-sm text-gray-500">{{ user.email }}</p>
                </div>
              </div>
              <div class="flex items-center gap-2">
                <select :value="user.role" class="border rounded px-2 py-1 text-sm">
                  <option>Support</option>
                  <option>Primary</option>
                </select>
                <button class="text-gray-500 hover:text-gray-700">
                  <span class="sr-only">Remove</span>
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16">
                    </path>
                  </svg>
                </button>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isPopupOpen = ref(false)
const inviteInput = ref('')

const users = ref([
  { id: 1, name: 'Aayush Kumar', role: 'Associate', avatar: '/placeholder.svg?height=40&width=40', joiningDate: '12/10/2024' },
  { id: 2, name: 'Gitesh', role: 'Associate', avatar: '/placeholder.svg?height=40&width=40', joiningDate: '12/10/2024' },
  { id: 3, name: 'Umesh Sharma', role: 'Associate', avatar: '/placeholder.svg?height=40&width=40', joiningDate: '12/10/2024' },
])

const inviteUsers = ref([
  { id: 1, name: 'Aayush Kumar', email: 'aayush.kumar@xyz.com', avatar: '/placeholder.svg?height=40&width=40', role: 'Support' },
  { id: 2, name: 'Abhinav', email: 'abhinav.tyagi@xyz.com', avatar: '/placeholder.svg?height=40&width=40', role: 'Primary' },
  { id: 3, name: 'Aayush Kumar', email: 'aayush.kumar@xyz.com', avatar: '/placeholder.svg?height=40&width=40', role: 'Support' },
  { id: 4, name: 'Aayush Kumar', email: 'aayush.kumar@xyz.com', avatar: '/placeholder.svg?height=40&width=40', role: 'Support' },
])

const openPopup = () => {
  isPopupOpen.value = true
}

const closePopup = () => {
  isPopupOpen.value = false
  inviteInput.value = ''
}
</script>