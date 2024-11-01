<template>
    <div class="min-h-screen bg-gray-100">
      <div class="max-w-[2048px] mx-auto bg-white shadow-lg flex flex-col lg:flex-row">
        <!-- Sidebar -->
        <div class="lg:w-64 bg-white border-b lg:border-r border-gray-200 lg:h-screen">
          <div class="p-4 border-b border-gray-200 flex justify-between items-center lg:block">
            <h2 class="text-sm font-semibold text-gray-600">SECTIONS</h2>
            <button @click="toggleSidebar" class="lg:hidden">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
              </svg>
            </button>
          </div>
          <nav :class="{ 'hidden': !sidebarOpen, 'block': sidebarOpen, 'lg:block': true }">
            <ul>
              <li v-for="(section, index) in sections" :key="index">
                <button
                  @click="changeSection(index)"
                  :class="[
                    'w-full text-left px-4 py-3 flex items-center',
                    currentSection === index ? 'bg-blue-100 text-blue-600' : 'text-gray-600',
                    section.isLocked ? 'opacity-50 cursor-not-allowed' : 'hover:bg-gray-50'
                  ]"
                  :disabled="section.isLocked"
                >
                  <span class="text-sm">{{ section.name }}</span>
                  <span v-if="section.isCompleted" class="ml-auto text-green-500">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </span>
                  <span v-else-if="section.isLocked" class="ml-auto text-gray-400">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
                    </svg>
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
              <a href="#" class="text-blue-600 hover:underline">Home</a> / 
              <a href="#" class="text-blue-600 hover:underline">Assessment</a>
            </nav>
            <h1 class="text-2xl sm:text-3xl font-bold text-gray-800 mb-6">Assessment Sample Test</h1>
            
            <div v-if="currentSection !== null">
              <div v-for="(question, index) in sections[currentSection].questions" :key="index" class="mb-8">
                <div class="flex items-start">
                  <h3 class="text-base sm:text-lg font-semibold text-gray-800 mb-2 flex-grow">{{ index + 1 }}. {{ question.text }}</h3>
                  <button v-if="question.hasInfo" class="bg-gray-200 text-gray-600 rounded-full w-6 h-6 flex items-center justify-center focus:outline-none" @click="showInfo(question)">
                    <span class="sr-only">More information</span>
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </button>
                </div>
                
                <!-- Dropdown -->
                <select v-if="question.type === 'dropdown'" v-model="question.answer" class="w-full p-2 border rounded mt-2">
                  <option value="">Select</option>
                  <option v-for="option in question.options" :key="option" :value="option">{{ option }}</option>
                </select>
  
                <!-- Radio buttons -->
                <div v-else-if="question.type === 'radio'" class="space-y-2 mt-2">
                  <label v-for="option in question.options" :key="option" class="flex items-center">
                    <input type="radio" :value="option" v-model="question.answer" class="mr-2">
                    <span>{{ option }}</span>
                  </label>
                </div>
  
                <!-- Text input -->
                <input v-else-if="question.type === 'text'" v-model="question.answer" type="text" class="w-full p-2 border rounded mt-2" :placeholder="question.placeholder || 'Enter'">
  
                <!-- Checkboxes -->
                <div v-else-if="question.type === 'checkbox'" class="space-y-2 mt-2">
                  <label v-for="option in question.options" :key="option" class="flex items-center">
                    <input type="checkbox" :value="option" v-model="question.answer" class="mr-2">
                    <span>{{ option }}</span>
                  </label>
                </div>
  
                <!-- File upload -->
                <div v-else-if="question.type === 'file'" class="border-2 border-dashed border-gray-300 rounded-lg p-4 text-center mt-2">
                  <label class="cursor-pointer">
                    <span class="text-orange-500 font-semibold">Click to upload</span> or drag and drop<br>
                    <span class="text-sm text-gray-500">SVG, PNG, JPG or GIF (max. 3MB)</span>
                    <input type="file" class="hidden" @change="handleFileUpload($event, question)">
                  </label>
                </div>
              </div>
  
              <div class="mt-8 flex flex-col sm:flex-row justify-between items-start sm:items-center space-y-4 sm:space-y-0">
                <label class="flex items-center">
                  <input type="checkbox" v-model="agreeToTerms" class="mr-2">
                  <span class="text-sm">I agree with <a href="#" class="text-blue-600 hover:underline">Data Sharing</a> and <a href="#" class="text-blue-600 hover:underline">Privacy Policy</a> agreement</span>
                </label>
                <button @click="submitSection" class="w-full sm:w-auto bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-6 rounded" :disabled="!canSubmit">
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
        { type: 'file', text: 'Lorem Ipsum', answer: null }
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

  ])
  
  const currentSection = ref(0)
  const agreeToTerms = ref(false)
  const sidebarOpen = ref(false)
  
  const isLastSection = computed(() => currentSection.value === sections.value.length - 1)
  
  const canSubmit = computed(() => {
    const currentQuestions = sections.value[currentSection.value].questions
    const allQuestionsAnswered = currentQuestions.every(q => 
      (q.type === 'checkbox' && q.answer.length > 0) || 
      (q.type !== 'checkbox' && q.answer)
    )
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
      // Here you would typically upload the file to a server
      // For this example, we'll just store the file name
      question.answer = file.name
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