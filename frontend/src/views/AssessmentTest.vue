<template>
  <div class=" relative min-h-screen bg-gray-100 font-poppins">
    <NavBar/>
    <div class="absolute bg-effect w-3/4 h-3/4">
        <img src="/effect.png" alt="Background effect">
      </div>
    <div class="max-w-[1512px] mx-auto bg-white shadow-lg pt-4 flex flex-col lg:flex-row">
      <!-- Sidebar -->
      <div class="lg:w-64 bg-white border-b lg:border-r border-gray-200 lg:h-screen">
        <div class="p-4 border-b border-gray-200 flex justify-between items-center lg:block">
          <h2 class="text-sm font-semibold text-[#0D4688]">SECTIONS</h2>
          <button @click="toggleSidebar" class="lg:hidden text-[#0D4688] focus:outline-none focus:ring-2 focus:ring-[#0D4688] rounded">
            <span class="sr-only">Toggle sidebar</span>
            <MenuIcon class="h-6 w-6" />
          </button>
        </div>
        <nav :class="{ 'hidden': !sidebarOpen, 'block': sidebarOpen, 'lg:block': true }">
          <ul class="overflow-y-auto max-h-[calc(100vh-64px)]">
            <li v-for="(section, index) in sections" :key="index">
              <button
                @click="changeSection(index)"
                :class="[
                  'w-full text-left px-4 py-3 h-[36px] flex items-center',
                  currentSection === index ? 'bg-blue-100 text-[#0D4688] rounded-full' : 'text-[#596C8C] ',
                  section.isLocked ? 'opacity-50 cursor-not-allowed' : 'hover:bg-gray-50'
                ]"
                :disabled="section.isLocked"
              >
                <span class="text-sm">{{ section.name }}</span>
                <span v-if="section.isCompleted" class="ml-auto text-green-500">
                  <CheckIcon class="h-4 w-4" />
                </span>
                <span v-else-if="section.isLocked" class="ml-auto text-gray-400">
                  <LockIcon class="h-4 w-4" />
                </span>
              </button>
            </li>
          </ul>
        </nav>
      </div>

      <!-- Main Content -->
      <div class="flex-1 overflow-y-auto lg:h-screen">
        <div class="p-4 sm:p-6 md:p-8">
          <nav class="text-sm mb-4">
            <a href="#" class="text-[#0D4688] hover:underline">Home</a> / 
            <a href="#" class="text-[#0D4688] hover:underline">Assessment</a>
          </nav>
          <h1 class="text-2xl sm:text-3xl font-bold text-[#0D4688] mb-6">Assessment Sample Test</h1>
          
          <div v-if="currentSection !== null">
            <div v-for="(question, index) in sections[currentSection].questions" :key="index" class="mb-8">
              <div class="flex items-start">
                <h3 class="text-base sm:text-lg font-semibold text-[#0D4688] mb-2 flex-grow">{{ index + 1 }}. {{ question.text }}</h3>
                <button v-if="question.hasInfo" class="bg-gray-200 text-[#596C8C] rounded-full w-6 h-6 flex items-center justify-center focus:outline-none focus:ring-2 focus:ring-[#0D4688]" @click="showInfo(question)">
                  <span class="sr-only">More information</span>
                  <InfoIcon class="h-4 w-4" />
                </button>
              </div>
              
              <!-- Dropdown -->
              <select v-if="question.type === 'dropdown'" v-model="question.answer" class="w-full p-2 border rounded mt-2 text-[#212529]">
                <option value="">Select</option>
                <option v-for="option in question.options" :key="option" :value="option">{{ option }}</option>
              </select>

              <!-- Radio buttons -->
              <div v-else-if="question.type === 'radio'" class="space-y-2 mt-2">
                <label v-for="option in question.options" :key="option" class="flex items-center">
                  <input type="radio" :value="option" v-model="question.answer" class="mr-2 text-[#0D4688] focus:ring-[#0D4688]">
                  <span class="text-[#212529]">{{ option }}</span>
                </label>
              </div>

              <!-- Text input -->
              <input v-else-if="question.type === 'text'" v-model="question.answer" type="text" class="w-full p-2 border rounded mt-2 text-[#212529]" :placeholder="question.placeholder || 'Enter'">

              <!-- Checkboxes -->
              <div v-else-if="question.type === 'checkbox'" class="space-y-2 mt-2">
                <label v-for="option in question.options" :key="option" class="flex items-center">
                  <input type="checkbox" :value="option" v-model="question.answer" class="mr-2 text-[#0D4688] focus:ring-[#0D4688]">
                  <span class="text-[#212529]">{{ option }}</span>
                </label>
              </div>

              <!-- File upload -->
              <div v-else-if="question.type === 'file'" class="border-2 border-dashed border-gray-300 rounded-lg p-4 text-center mt-2">
                <label class="cursor-pointer">
                  <span class="text-orange-500 font-semibold">Click to upload</span> or drag and drop<br>
                  <span class="text-sm text-[#596C8C]">SVG, PNG, JPG or GIF (max. 3MB)</span>
                  <input type="file" class="hidden" @change="handleFileUpload($event, question)" accept="image/*">
                </label>
                <div v-if="question.answer" class="mt-2">
                  <img :src="question.answer" alt="Uploaded file" class="max-w-full h-auto max-h-40 mx-auto">
                </div>
              </div>

              <!-- Matrix question -->
              <div v-else-if="question.type === 'matrix'" class="mt-2 overflow-x-auto">
                <table class="w-full border-collapse">
                  <thead>
                    <tr>
                      <th class="border p-2"></th>
                      <th v-for="option in question.options" :key="option" class="border p-2 text-[#0D4688]">{{ option }}</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="row in question.rows" :key="row">
                      <td class="border p-2 text-[#212529]">{{ row }}</td>
                      <td v-for="option in question.options" :key="option" class="border p-2">
                        <input 
                          type="radio" 
                          :name="`${question.id}-${row}`" 
                          :value="option" 
                          v-model="question.answer[row]" 
                          class="text-[#0D4688] focus:ring-[#0D4688]"
                        >
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <div class="mt-8 flex flex-col sm:flex-row justify-between items-start sm:items-center space-y-4 sm:space-y-0">
              <label class="flex items-center">
                <input type="checkbox" v-model="agreeToTerms" class="mr-2 text-[#0D4688] focus:ring-[#0D4688]">
                <span class="text-sm text-[#212529]">I agree with <a href="#" class="text-[#0D4688] hover:underline">Data Sharing</a> and <a href="#" class="text-[#0D4688] hover:underline">Privacy Policy</a> agreement</span>
              </label>
              <button @click="submitSection" class="h-[40px] w-[160px] rounded-full sm:w-auto bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-6 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:ring-opacity-50" :disabled="!canSubmit">
                {{ isLastSection ? 'SUBMIT' : 'NEXT' }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { MenuIcon, CheckIcon, LockIcon, InfoIcon } from 'lucide-vue-next'
import NavBar from '../components/NavBar.vue';

const sections = ref([
  {
    name: 'Section A',
    isCompleted: false,
    isLocked: false,
    questions: [
      { type: 'dropdown', text: 'Lorem Ipsum', options: ['Option 1', 'Option 2', 'Option 3'], answer: '', hasInfo: true },
      { type: 'radio', text: 'Select the option that suits the best', options: ['This is option 1', 'This is option 2', 'This is option 3', 'This is option 4'], answer: '', hasInfo: true },
      { type: 'text', text: 'Lorem Ipsum', answer: '', placeholder: 'Enter' },
      { type: 'checkbox', text: 'Select all the options that suit the best', options: ['This is option 1', 'This is option 2', 'This is option 3', 'This is option 4'], answer: [], hasInfo: true },
      { type: 'file', text: 'Lorem Ipsum', answer: null },
      // { 
      //   id: 'matrix1',
      //   type: 'matrix', 
      //   text: 'Rate the following aspects', 
      //   options: ['Poor', 'Fair', 'Good', 'Excellent'],
      //   rows: ['Quality', 'Price', 'Service', 'Overall'],
      //   answer: {},
      //   hasInfo: true
      // }
    ]
  },
  { name: 'Section B', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section C', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section D', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section E', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section F', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section G', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section H', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section I', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section J', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section K', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section L', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section M', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section N', isCompleted: false, isLocked: true, questions: [] },
  { name: 'Section O', isCompleted: false, isLocked: true, questions: [] },
])

const currentSection = ref(0)
const agreeToTerms = ref(false)
const sidebarOpen = ref(false)

const isLastSection = computed(() => currentSection.value === sections.value.length - 1)

const canSubmit = computed(() => {
  const currentQuestions = sections.value[currentSection.value].questions
  const allQuestionsAnswered = currentQuestions.every(q => {
    if (q.type === 'checkbox') return q.answer.length > 0
    if (q.type === 'matrix') return Object.keys(q.answer).length === q.rows.length
    return !!q.answer
  })
  return allQuestionsAnswered && agreeToTerms.value
})

const changeSection = (index) => {
  if (!sections.value[index].isLocked) {
    currentSection.value = index
    sidebarOpen.value = false
  }
}

const handleFileUpload = (event, question) => {
  const file = event.target.files[0]
  if (file) {
    if (file.size > 3 * 1024 * 1024) {
      alert('File size exceeds 3MB limit.')
      return
    }
    const reader = new FileReader()
    reader.onload = (e) => {
      question.answer = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

const submitSection = () => {
  sections.value[currentSection.value].isCompleted = true
  if (!isLastSection.value) {
    currentSection.value++
    sections.value[currentSection.value].isLocked = false
  } else {
    // Handle final submission
    alert('Assessment completed!')
  }
}

const showInfo = (question) => {
  // Implement the logic to show more information about the question
  alert(`More information about: ${question.text}`)
}

const toggleSidebar = () => {
  sidebarOpen.value = !sidebarOpen.value
}

// Initialize: Lock all sections except the first one
sections.value.forEach((section, index) => {
  section.isLocked = index !== 0
})
</script>

<style scoped>
/* Add any component-specific styles here */
@media (max-width: 640px) {
  .overflow-x-auto {
    -webkit-overflow-scrolling: touch;
  }
}
</style>