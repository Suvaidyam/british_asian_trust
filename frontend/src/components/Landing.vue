<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Hero Section -->
    <section class="relative bg-gradient-to-r from-blue-500 to-teal-400 text-white">
      <div class="container mx-auto px-4 py-16 md:py-24">
        <div class="max-w-3xl mx-auto text-center">
          <h1 class="text-4xl md:text-5xl font-bold mb-4">Empowering NGOs to Drive Impact</h1>
          <p class="text-xl mb-8">Register and complete your assessment to unlock resources and support for your cause.</p>
          <button class="bg-white text-blue-600 font-semibold py-2 px-6 rounded-full hover:bg-blue-100 transition duration-300">
            Get Started
          </button>
        </div>
      </div>
      <div class="absolute bottom-0 left-0 right-0">
        <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M0 0L60 10C120 20 240 40 360 46.7C480 53 600 47 720 43.3C840 40 960 40 1080 46.7C1200 53 1320 67 1380 73.3L1440 80V120H1380C1320 120 1200 120 1080 120C960 120 840 120 720 120C600 120 480 120 360 120C240 120 120 120 60 120H0V0Z" fill="currentColor"/>
        </svg>
      </div>
    </section>

    <!-- About Us Section -->
    <section class="py-16 md:py-24">
      <div class="container mx-auto px-4">
        <div class="flex flex-col md:flex-row items-center">
          <div class="md:w-1/2 mb-8 md:mb-0">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-4">About Us</h2>
            <p class="text-gray-600 mb-6">
              Our portal is designed to streamline the process for NGOs to register, assess their impact, and connect with resources. We believe in supporting non-governmental organizations by providing them with an easy and transparent way to showcase their work and secure the support they need to drive change.
            </p>
            <button class="bg-teal-500 text-white font-semibold py-2 px-6 rounded-full hover:bg-teal-600 transition duration-300">
              How It Works
            </button>
          </div>
          <div class="md:w-1/2">
            <img src="../../public/login1.png" alt="How It Works" class="rounded-lg shadow-lg" />
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works Section -->
    <section class="bg-gray-100 py-16 md:py-24">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-12 text-center">How It Works</h2>
        <div class="flex flex-col md:flex-row justify-between items-start">
          <div class="flex-1 mb-8 md:mb-0">
            <div class="bg-white rounded-lg shadow-md p-6">
              <div class="text-3xl font-bold text-blue-500 mb-4">1</div>
              <h3 class="text-xl font-semibold mb-2">Register Your NGO</h3>
              <p class="text-gray-600">Quickly create an account and fill out basic information.</p>
            </div>
          </div>
          <div class="flex-1 mb-8 md:mb-0 md:mx-4">
            <div class="bg-white rounded-lg shadow-md p-6">
              <div class="text-3xl font-bold text-blue-500 mb-4">2</div>
              <h3 class="text-xl font-semibold mb-2">Fill Out the Assessment</h3>
              <p class="text-gray-600">Complete our simple, yet comprehensive assessment to highlight your organization's impact and goals.</p>
            </div>
          </div>
          <div class="flex-1">
            <div class="bg-white rounded-lg shadow-md p-6">
              <div class="text-3xl font-bold text-blue-500 mb-4">3</div>
              <h3 class="text-xl font-semibold mb-2">Submit & Access Resources</h3>
              <p class="text-gray-600">Once submitted, gain access to tools and support tailored to help you grow.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section class="py-16 md:py-24">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-12 text-center">What people say about us</h2>
        <div class="max-w-4xl mx-auto">
          <div class="bg-white rounded-lg shadow-lg p-8 relative">
            <img src="../../public/login1.png" alt="Ayush Kumar" class="w-20 h-20 rounded-full absolute -top-10 left-1/2 transform -translate-x-1/2 border-4 border-white" />
            <div class="text-center mt-8">
              <p class="text-xl text-gray-600 mb-4">"This platform made the process of applying for support so easy. We now have more visibility and access to crucial resources."</p>
              <p class="font-semibold text-gray-800">Ayush Kumar</p>
              <p class="text-gray-500">NGO A</p>
            </div>
            <button class="absolute top-1/2 left-4 transform -translate-y-1/2 bg-white rounded-full p-2 shadow-md hover:bg-gray-100">
              <ChevronLeftIcon class="w-6 h-6 text-gray-600" />
            </button>
            <button class="absolute top-1/2 right-4 transform -translate-y-1/2 bg-white rounded-full p-2 shadow-md hover:bg-gray-100">
              <ChevronRightIcon class="w-6 h-6 text-gray-600" />
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="bg-gray-100 py-16 md:py-24">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-12 text-center">FAQs</h2>
        <div class="max-w-3xl mx-auto">
          <div v-for="(faq, index) in faqs" :key="index" class="mb-4">
            <button
              @click="toggleFaq(index)"
              class="flex justify-between items-center w-full bg-white p-4 rounded-lg shadow-md hover:bg-gray-50 transition duration-300"
            >
              <span class="font-semibold text-gray-800">{{ faq.question }}</span>
              <ChevronDownIcon
                :class="['w-5 h-5 text-gray-600 transition-transform duration-300', { 'transform rotate-180': faq.isOpen }]"
              />
            </button>
            <div
              v-show="faq.isOpen"
              class="bg-white mt-2 p-4 rounded-lg shadow-md"
            >
              <p class="text-gray-600">{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ChevronLeftIcon, ChevronRightIcon, ChevronDownIcon } from 'lucide-vue-next'

const faqs = ref([
  {
    question: 'What types of NGOs can register on this platform?',
    answer: 'Our platform is open to all types of non-governmental organizations working towards social impact. This includes but is not limited to organizations focused on education, healthcare, environment, human rights, and community development.',
    isOpen: false
  },
  {
    question: 'How long does the registration process take?',
    answer: 'The initial registration process typically takes about 15-20 minutes. However, completing the full assessment may require additional time depending on the complexity of your organization and the information you have readily available.',
    isOpen: false
  },
  {
    question: 'Is there a fee to use this platform?',
    answer: 'No, our platform is free for NGOs to use. Our goal is to provide accessible support and resources to organizations driving social impact.',
    isOpen: false
  },
  {
    question: 'Is there a fee to use this platform?',
    answer: 'No, our platform is free for NGOs to use. Our goal is to provide accessible support and resources to organizations driving social impact.',
    isOpen: false
  }
])

const toggleFaq = (index) => {
  faqs.value[index].isOpen = !faqs.value[index].isOpen
}
</script>