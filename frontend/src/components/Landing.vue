<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Section -->
    <section class="relative py-12 px-4 sm:px-6 lg:px-8 overflow-hidden">
      <div class="absolute bg-effect w-3/4 h-3/4">
        <img src="../../public/effect.png" alt="">
      </div>
      <div class="max-w-[2048px] mx-auto relative">
        <h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold text-blue-900 text-center mb-4">
          Empowering NGOs to Drive Impact
        </h1>
        <p class="text-md sm:text-lg md:text-xl text-gray-700 text-center mb-8 max-w-3xl mx-auto">
          Register and complete your assessment to unlock resources and support for your cause.
        </p>
        <div class="relative rounded-lg overflow-hidden shadow-xl">
          <img src="../../public/login1.png" alt="Family using laptop"
            class="w-full h-[300px] sm:h-[400px] md:h-[500px] lg:h-[600px] object-cover">
        </div>
      </div>
    </section>

    <!-- About Us Section -->
    <section class="py-16 px-4 sm:px-6 lg:px-8 bg-gray-50">
      <div class="max-w-[2048px] mx-auto">
        <div class="lg:flex lg:items-start lg:justify-between mb-12 lg:mb-16">
          <div class="relative flex-shrink-0 mb-8 lg:mb-0 lg:mr-12">
            <div class="absolute inset-0 bg-blue-100 rounded-full h-16 w-16 sm:h-20 sm:w-20"></div>
            <h2 class="text-2xl sm:text-3xl lg:text-4xl xl:text-5xl font-bold text-blue-900 relative z-10 p-4">About Us
            </h2>
          </div>
          <p class="text-base sm:text-lg lg:text-xl text-gray-700 max-w-2xl lg:max-w-3xl">
            Our portal is designed to streamline the process for NGOs to register, assess their impact,
            and connect with resources. We believe in supporting non-governmental organizations by
            providing them with an easy and transparent way to showcase their work and secure the
            support they need to drive change.
          </p>
        </div>
        <div class="lg:flex lg:space-x-8">
          <!-- Steps Section -->
          <div class="space-y-8 lg:space-y-12 w-full lg:w-1/2 relative mb-8 lg:mb-0">
            <div class="absolute top-0 left-4 sm:left-7 bottom-0 border-l-2 border-dotted border-gray-300"></div>
            <div v-for="(step, index) in steps" :key="index"
              class="relative flex flex-col sm:flex-row items-start sm:items-center gap-4">
              <div
                class="relative bg-white h-12 w-12 sm:h-14 sm:w-14 rounded-full flex items-center justify-center border-2 border-gray-300 z-10">
                <component :is="step.icon" class="w-6 h-6 sm:w-8 sm:h-8 text-blue-600"></component>
              </div>
              <div class="sm:ml-4">
                <h4 class="text-base sm:text-lg lg:text-xl font-semibold mb-1 sm:mb-2">{{ step.title }}</h4>
                <p class="text-sm sm:text-base lg:text-lg text-gray-600">{{ step.description }}</p>
              </div>
            </div>
          </div>
          <!-- Image and Button Section -->
          <div class="lg:w-1/2 relative">
            <img src="../../public/login1.png" alt="Children benefiting from NGO work"
              class="w-full rounded-lg shadow-lg">
            <button
              class="absolute top-4 right-4 bg-teal-500 hover:bg-teal-600 text-white font-bold py-2 px-4 sm:py-3 sm:px-6 rounded-lg transition duration-300 text-sm sm:text-base">
              How It Works
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonial Section with Slider -->
    <section class="py-16 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
      <div class="absolute bg-effect1 w-1/4 h-1/2 ">
        <img src="../../public/effect.png" alt="">
      </div>
      <div class="max-w-[2048px] mx-auto relative">
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-blue-900 text-center mb-12">
          What people say about us
        </h2>
        <div class="relative">
          <div class="overflow-hidden">
            <div class="flex transition-transform duration-300 ease-in-out"
              :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
              <div v-for="(testimonial, index) in testimonials" :key="index" class="w-full flex-shrink-0">
                <div class="flex flex-col sm:flex-row items-center sm:items-start gap-8 max-w-4xl mx-auto">
                  <div class="flex flex-col items-center sm:w-1/3">
                    <img :src="testimonial.image" :alt="testimonial.name"
                      class="w-full h-48 object-cover rounded-lg shadow-md">
                    <h3 class="text-xl font-semibold mt-4">{{ testimonial.name }}</h3>
                    <p class="text-gray-600">{{ testimonial.organization }}</p>
                  </div>
                  <blockquote class="text-lg sm:text-xl md:text-2xl text-gray-700 sm:w-2/3">
                    "{{ testimonial.quote }}"
                  </blockquote>
                </div>
              </div>
            </div>
          </div>
          <button @click="prevSlide"
            class="absolute top-1/2 left-4 transform -translate-y-1/2 bg-white rounded-full p-2 shadow-md">
            <ChevronLeftIcon class="w-6 h-6 text-blue-600" />
          </button>
          <button @click="nextSlide"
            class="absolute top-1/2 right-4 transform -translate-y-1/2 bg-white rounded-full p-2 shadow-md">
            <ChevronRightIcon class="w-6 h-6 text-blue-600" />
          </button>
        </div>
        <div class="flex justify-center mt-6">
          <div v-for="(_, index) in testimonials" :key="index" @click="goToSlide(index)"
            class="w-3 h-3 rounded-full mx-1 cursor-pointer"
            :class="currentSlide === index ? 'bg-blue-600' : 'bg-gray-300'"></div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-16 px-4 sm:px-6 lg:px-8">
      <div class="max-w-[2048px] mx-auto">
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-blue-900 text-center mb-12">FAQs</h2>
        <div class="space-y-4 max-w-3xl mx-auto">
          <div v-for="(faq, index) in faqs" :key="index" class="border border-gray-200 rounded-lg">
            <button @click="toggleFaq(index)" class="flex justify-between items-center w-full p-4 text-left">
              <span class="text-base sm:text-lg md:text-xl font-semibold text-gray-800">{{ faq.question }}</span>
              <PlusIcon v-if="!faq.isOpen" class="w-6 h-6 text-blue-600 flex-shrink-0 ml-4" />
              <MinusIcon v-else class="w-6 h-6 text-blue-600 flex-shrink-0 ml-4" />
            </button>
            <div v-show="faq.isOpen" class="p-4 pt-0">
              <p class="text-sm sm:text-base md:text-lg text-gray-700">{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
  <Footer />
</template>

<script setup>
import { ref } from 'vue'
import { ClipboardIcon, ClipboardCheckIcon, FileTextIcon, PlusIcon, MinusIcon, ChevronLeftIcon, ChevronRightIcon } from 'lucide-vue-next'
import Footer from './Footer.vue';

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
    image: "../../public/user.jpg",
    quote: "This platform made the process of applying for support so easy. We now have more visibility and access to crucial resources."
  },
  {
    name: "Priya Sharma",
    organization: "NGO B",
    image: "../../public/user.jpg",
    quote: "The assessment tool provided valuable insights into our organization's strengths and areas for improvement."
  },
  {
    name: "Rahul Verma",
    organization: "NGO C",
    image: "../../public/user.jpg",
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
    question: 'How can I register my NGO on this platform?',
    answer: 'To register your NGO, simply click on the "Register" button at the top of the page and follow the step-by-step process. You\'ll need to provide basic information about your organization and complete a brief assessment.',
    isOpen: false
  },
  {
    question: 'What kind of resources are available after registration?',
    answer: 'After registration and assessment, you\'ll have access to a variety of resources including funding opportunities, capacity building workshops, networking events, and tools to help measure and report your impact.',
    isOpen: false
  },
  {
    question: 'Is there a fee for using this platform?',
    answer: 'No, our platform is completely free for NGOs. We believe in providing equal access to resources and support for all organizations working towards positive social change.',
    isOpen: false
  },
  {
    question: 'How often should I update my NGO\'s information?',
    answer: 'We recommend updating your information at least once a year or whenever there are significant changes in your organization\'s structure, programs, or impact. Regular updates help ensure that you receive the most relevant resources and opportunities.',
    isOpen: false
  },
  {
    question: 'Can I connect with other NGOs through this platform?',
    answer: 'Yes! Our platform includes features for networking and collaboration. You can search for other NGOs working in similar areas or regions, join discussion forums, and even initiate partnerships through our messaging system.',
    isOpen: false
  }
])

const toggleFaq = (index) => {
  faqs.value[index].isOpen = !faqs.value[index].isOpen
}
</script>