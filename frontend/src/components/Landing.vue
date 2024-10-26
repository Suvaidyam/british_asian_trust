<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Section -->
    <section class="relative bg-gradient-to-r from-blue-100 via-green-100 to-teal-100 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-[2048px] mx-auto">
        <h1 class="text-2xl sm:text-3xl md:text-4xl font-bold text-blue-900 text-center mb-4">
          Empowering NGOs to Drive Impact
        </h1>
        <p class="text-md sm:text-lg text-gray-700 text-center  mb-8">
          Register and complete your assessment to unlock resources and support for your cause.
        </p>
        <div class="relative rounded-lg overflow-hidden shadow-xl">
          <img src="/login1.png" alt="Family using laptop" class="w-full h-[300px] sm:h-[400px] md:h-[500px] object-cover">
        </div>
      </div>
    </section>

    <!-- Updated About Us Section -->
    <section class="py-16 px-4 sm:px-6 lg:px-8">
      <div class="max-w-[2048px] mx-auto">
        <div class="lg:flex lg:items-start lg:justify-between">
          <div class="lg:w-1/2 mb-8 lg:mb-0">
            <div class="flex items-center mb-6">
              <div class="bg-blue-100 rounded-full p-4">
                <h2 class="text-3xl sm:text-4xl font-bold text-blue-900">About Us</h2>
              </div>
            </div>
            <p class="text-base sm:text-lg text-gray-700 mb-6">
              Our portal is designed to streamline the process for NGOs to register, assess their impact,
              and connect with resources. We believe in supporting non-governmental organizations by
              providing them with an easy and transparent way to showcase their work and secure the
              support they need to drive change.
            </p>
            <div class="space-y-8">
              <div v-for="(step, index) in steps" :key="index" class="flex items-start">
                <div class="flex-shrink-0 mr-4">
                  <component :is="step.icon" class="w-8 h-8 text-blue-600" />
                </div>
                <div>
                  <h4 class="text-lg sm:text-xl font-semibold mb-2">{{ step.title }}</h4>
                  <p class="text-sm sm:text-base text-gray-600">{{ step.description }}</p>
                </div>
              </div>
            </div>
          </div>
          <div class="lg:w-1/2 lg:pl-8 relative mt-8 lg:mt-0">
            <img src="/login1.png" alt="Children benefiting from NGO work" class="w-full rounded-lg shadow-lg">
            <button class="absolute top-4 right-4 bg-teal-500 hover:bg-teal-600 text-white font-bold py-2 px-4 sm:py-3 sm:px-6 rounded-lg transition duration-300 text-sm sm:text-lg">
              How It Works
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonial Section with Slider -->
    <section class="py-16 px-4 sm:px-6 lg:px-8 bg-gradient-to-r from-blue-100 via-green-100 to-teal-100">
      <div class="max-w-[2048px] mx-auto">
        <h2 class="text-3xl sm:text-4xl font-bold text-blue-900 text-center mb-12">What people say about us</h2>
        <div class="relative">
          <div class="overflow-hidden">
            <div class="flex transition-transform duration-300 ease-in-out" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
              <div v-for="(testimonial, index) in testimonials" :key="index" class="w-full flex-shrink-0">
                <div class="bg-white rounded-lg shadow-lg p-6 sm:p-8 max-w-4xl mx-auto">
                  <div class="flex flex-col sm:flex-row items-center mb-6">
                    <img :src="testimonial.image" :alt="testimonial.name" class="w-20 h-20 rounded-full mb-4 sm:mb-0 sm:mr-4 object-cover">
                    <div class="text-center sm:text-left">
                      <h3 class="text-xl font-semibold">{{ testimonial.name }}</h3>
                      <p class="text-gray-600">{{ testimonial.organization }}</p>
                    </div>
                  </div>
                  <blockquote class="text-lg sm:text-xl text-gray-700 text-center sm:text-left">
                    "{{ testimonial.quote }}"
                  </blockquote>
                </div>
              </div>
            </div>
          </div>
          <button @click="prevSlide" class="absolute top-1/2 left-4 transform -translate-y-1/2 bg-white rounded-full p-2 shadow-md">
            <ChevronLeftIcon class="w-6 h-6 text-blue-600" />
          </button>
          <button @click="nextSlide" class="absolute top-1/2 right-4 transform -translate-y-1/2 bg-white rounded-full p-2 shadow-md">
            <ChevronRightIcon class="w-6 h-6 text-blue-600" />
          </button>
        </div>
        <div class="flex justify-center mt-6">
          <div v-for="(_, index) in testimonials" :key="index" @click="goToSlide(index)" class="w-3 h-3 rounded-full mx-1 cursor-pointer" :class="currentSlide === index ? 'bg-blue-600' : 'bg-gray-300'"></div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-16 px-4 sm:px-6 lg:px-8">
      <div class="max-w-[2048px] mx-auto">
        <h2 class="text-3xl sm:text-4xl font-bold text-blue-900 text-center mb-12">FAQs</h2>
        <div class="space-y-4">
          <div v-for="(faq, index) in faqs" :key="index" class="border border-gray-200 rounded-lg">
            <button 
              @click="toggleFaq(index)" 
              class="flex justify-between items-center w-full p-4 text-left"
            >
              <span class="text-base sm:text-lg font-semibold text-gray-800">{{ faq.question }}</span>
              <PlusIcon v-if="!faq.isOpen" class="w-6 h-6 text-blue-600 flex-shrink-0 ml-4" />
              <MinusIcon v-else class="w-6 h-6 text-blue-600 flex-shrink-0 ml-4" />
            </button>
            <div v-show="faq.isOpen" class="p-4 pt-0">
              <p class="text-sm sm:text-base text-gray-700">{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ClipboardIcon, ClipboardCheckIcon, FileTextIcon, PlusIcon, MinusIcon, ChevronLeftIcon, ChevronRightIcon } from 'lucide-vue-next'

const steps = [
  {
    icon: ClipboardIcon,
    title: "Step 1: Register Your NGO",
    description: "Quickly create an account and fill out basic information."
  },
  {
    icon: ClipboardCheckIcon,
    title: "Step 2: Fill Out the Assessment",
    description: "Complete our simple, yet comprehensive assessment to highlight your organization's impact and goals."
  },
  {
    icon: FileTextIcon,
    title: "Step 3: Submit & Access Resources",
    description: "Once submitted, gain access to tools and support tailored to help you grow."
  }
]

const testimonials = [
  {
    name: "Ayush Kumar",
    organization: "NGO A",
    image: "/login1.png",
    quote: "This platform made the process of applying for support so easy. We now have more visibility and access to crucial resources."
  },
  {
    name: "Priya Sharma",
    organization: "NGO B",
    image: "/login1.png",
    quote: "The assessment tool provided valuable insights into our organization's strengths and areas for improvement."
  },
  {
    name: "Rahul Verma",
    organization: "NGO C",
    image: "/login1.png",
    quote: "Thanks to this portal, we've connected with like-minded organizations and expanded our impact significantly."
  }
]

const currentSlide = ref(0)

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % testimonials.length
}

const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + testimonials.length) % testimonials.length
}

const goToSlide = (index) => {
  currentSlide.value = index
}

const faqs = ref([
  {
    question: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt',
    answer: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    isOpen: false
  },
  {
    question: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis.',
    answer: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    isOpen: false
  },
  {
    question: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt',
    answer: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    isOpen: false
  },
  {
    question: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea',
    answer: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    isOpen: false
  },
  {
    question: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt',
    answer: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    isOpen: false
  }
])

const toggleFaq = (index) => {
  faqs.value[index].isOpen = !faqs.value[index].isOpen
}
</script>