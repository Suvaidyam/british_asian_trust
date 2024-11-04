<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Section -->
    <section class="relative py-12 px-4 sm:px-6 lg:px-8 overflow-hidden">
      <div class="absolute bg-effect w-3/4 h-3/4">
        <img src="/effect.png" alt="Background effect">
      </div>
      <div class="max-w-[1512px] mx-auto relative">
        <div class="mx-6 sm:mx-12 lg:mx-28">
          <h1 class="font-poppins text-4xl font-bold leading-[44px] text-center lg:text-[40px] text-[#0D4688] mb-4">
            Empowering NGOs to Drive Impact
          </h1>
          <p
            class="font-poppins text-[19px] font-normal leading-[20.9px] tracking-[0.5px] text-[#212529] text-center mb-8 max-w-[750px] mx-auto">
            Register and complete your assessment to unlock resources and support for your cause.
          </p>
          <div class="relative rounded-lg overflow-hidden shadow-xl">
            <img src="/login1.png" alt="Family using laptop"
              class="w-full h-[200px] sm:h-[300px] md:h-[400px] lg:h-[550px] object-cover">
          </div>
        </div>
      </div>
    </section>

    <!-- About Us Section -->
    <section class="py-16 px-4 sm:px-6 lg:px-8 bg-[#F4F4F4]">
      <div class="max-w-[1512px] mx-auto">
        <div class="lg:flex lg:items-start lg:justify-between mb-12 lg:mb-16">
          <div class="relative flex-shrink-0 mb-8 lg:mb-0 lg:mr-12">
            <div class="absolute inset-0 bg-[#BBCDE3] rounded-full h-16 w-16 sm:h-20 sm:w-20"></div>
            <h2 class="font-poppins text-[48px] font-bold leading-[52.8px] text-left text-[#0D4688] relative z-10 p-4">
              About Us</h2>
          </div>
          <p
            class="font-poppins text-[20px] font-normal leading-[40px] text-justify text-[#212529] max-w-2xl lg:max-w-4xl">
            Our portal is designed to streamline the process for NGOs to register, assess their impact,
            and connect with resources. We believe in supporting non-governmental organizations by
            providing them with an easy and transparent way to showcase their work and secure the
            support they need to drive change.
          </p>
        </div>
        <div class="lg:flex lg:space-x-8">
          <!-- Steps Section -->
          <div class="space-y-24 w-full lg:w-1/2 relative mb-8 lg:mb-0">
            <div
              class="absolute top-[calc(6rem+1.75rem)] left-7 sm:left-10 bottom-16 border-l-2 border-dashed  border-orange-400">
            </div>
            <div v-for="(step, index) in steps" :key="index"
              class="relative flex flex-col sm:flex-row items-start sm:items-center gap-6">
              <div
                class="relative bg-white h-14 w-14 sm:h-20 sm:w-20 flex items-center justify-center z-10 rounded-full shadow-md">
                <component :is="step.icon" class="w-8 h-8 sm:w-10 sm:h-10 text-[#0D4688]"></component>
              </div>
              <div class="sm:ml-4">
                <p class="font-poppins text-[15px] font-normal leading-[21px] text-left text-[#808080]">{{ step.title }}
                </p>
                <h4 class="font-poppins text-lg font-medium leading-7 text-left mb-1 sm:mb-2">{{ step.label }}</h4>
                <p class="font-poppins text-sm font-normal leading-[16.8px] text-justify text-gray-600">{{
                  step.description }}</p>
              </div>
            </div>
          </div>
          <!-- Image and Button Section -->
          <div class="lg:w-1/2 relative">
            <img src="/about.png" alt="Children benefiting from NGO work"
              class="w-full h-[600px] object-cover rounded-lg shadow-lg">
            <button
              class="absolute top-[-30px]  right-[-110px] transform -translate-x-1/2 bg-[#06A0A0] text-white py-2 px-4 sm:py-3 sm:px-8 md:px-16 lg:px-36 rounded-lg transition duration-300 font-poppins text-3xl font-normal leading-[50.4px]  text-center  h-[65px]">
              How It Works
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonial Section with Slider -->
    <section class="py-16 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
      <div class="absolute bg-effect1 w-1/4 h-1/2 ">
        <img src="/effect.png" alt="Background effect">
      </div>
      <div class="max-w-[1512px] mx-auto relative">
        <h2 class="font-poppins text-4xl font-bold leading-[52.8px] text-center text-[#0D4688] mb-12">
          What people say about us
        </h2>
        <div class="relative">
          <div class="overflow-hidden">
            <div class="flex transition-transform duration-300 ease-in-out"
              :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
              <div v-for="(testimonial, index) in testimonials" :key="index" class="w-full flex-shrink-0">
                <div class="flex flex-col sm:flex-row items-center sm:items-start gap-8 max-w-4xl mx-auto">
                  <div class="flex flex-col items-center sm:w-1/3">
                    <img src="/user.png" :alt="testimonial.name"
                      class="w-full h-[271px] object-cover rounded-lg shadow-md">
                    <h3 class="font-poppins text-lg font-medium leading-[17.6px] py-1 text-center text-[#0D4688] mt-4">
                      {{ testimonial.name }}</h3>
                    <p class="font-poppins text-sm font-normal leading-[13.2px]  text-center text-[#808080]">{{
                      testimonial.organization }}</p>
                  </div>
                  <blockquote class="font-poppins text-xl mt-24 font-medium leading-[35.07px] text-left sm:w-2/3">
                    <span class="text-[85px] "><svg width="67" height="52" viewBox="0 0 67 52" fill="none"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                          d="M0.713851 36.931C0.714387 40.1793 1.77815 43.338 3.74266 45.9249C5.70717 48.5117 8.46443 50.3844 11.5933 51.2569C14.7221 52.1294 18.0506 51.9538 21.0702 50.7568C24.0899 49.5598 26.6347 47.4074 28.3161 44.6281C29.9974 41.8489 30.7228 38.5957 30.3815 35.3655C30.0402 32.1352 28.6508 29.1055 26.4258 26.739C24.2007 24.3726 21.2622 22.7995 18.059 22.2601C14.8559 21.7207 11.5643 22.2446 8.68685 23.7518C9.68135 20.0628 11.0838 16.973 12.7626 14.508C16.1201 9.56953 20.5188 7.18103 25.1513 7.18103C25.9967 7.18103 26.8075 6.84521 27.4052 6.24743C28.003 5.64966 28.3388 4.83891 28.3388 3.99353C28.3388 3.14816 28.003 2.3374 27.4052 1.73963C26.8075 1.14186 25.9967 0.806031 25.1513 0.806031C18.0496 0.806031 11.8191 4.55878 7.48835 10.921C3.19585 17.2365 0.71385 26.1488 0.713851 36.931Z"
                          fill="#0D4688" />
                        <path
                          d="M37.1426 36.931C37.1431 40.1793 38.2069 43.338 40.1714 45.9249C42.1359 48.5117 44.8931 50.3844 48.022 51.2569C51.1509 52.1294 54.4793 51.9538 57.499 50.7568C60.5186 49.5598 63.0635 47.4074 64.7448 44.6281C66.4261 41.8489 67.1515 38.5957 66.8102 35.3655C66.4689 32.1352 65.0796 29.1055 62.8545 26.739C60.6294 24.3726 57.6909 22.7995 54.4877 22.2601C51.2846 21.7207 47.993 22.2446 45.1156 23.7518C46.1101 20.0628 47.5126 16.973 49.1913 14.508C52.5488 9.56953 56.9476 7.18103 61.5801 7.18103C62.4254 7.18103 63.2362 6.84521 63.834 6.24743C64.4317 5.64966 64.7676 4.83891 64.7676 3.99353C64.7676 3.14816 64.4317 2.3374 63.834 1.73963C63.2362 1.14186 62.4254 0.806031 61.5801 0.806031C54.4783 0.806031 48.2478 4.55878 43.9171 10.921C39.6246 17.2365 37.1426 26.1488 37.1426 36.931Z"
                          fill="#0D4688" />
                      </svg>
                    </span>{{ testimonial.quote }}
                  </blockquote>
                </div>
              </div>
            </div>
          </div>
          <button @click="prevSlide"
            class="absolute top-1/2 left-4 transform -translate-y-1/2 bg-white rounded-full p-2 shadow-md">
            <ChevronLeftIcon class="w-[61px] h-[61px] text-[#FF8A00]" />
          </button>
          <button @click="nextSlide"
            class="absolute top-1/2 right-4 transform -translate-y-1/2 bg-white rounded-full p-2 shadow-md">
            <ChevronRightIcon class="w-[61px] h-[61px] text-[#FF8A00]" />
          </button>
        </div>
        <div class="flex justify-center mt-6">
          <div v-for="(_, index) in testimonials" :key="index" @click="goToSlide(index)"
            class="w-3 h-3 rounded-full mx-1 cursor-pointer"
            :class="currentSlide === index ? 'bg-[#FF8A00]' : 'bg-gray-300'"></div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-16 px-4 sm:px-6 lg:px-8">
      <div class="max-w-[1512px] mx-auto">
        <h2 class="font-poppins text-4xl font-bold leading-[52.8px] text-[#0D4688] text-center mb-12">
          FAQs</h2>
        <div class="space-y-4 max-w-3xl mx-auto">
          <div v-for="(faq, index) in faqs" :key="index" class="border-2 border-gray-100 rounded-lg">
            <button @click="toggleFaq(index)" class="flex justify-between items-center w-full p-4 text-left">
              <span
                class="font-poppins text-lg font-medium leading-[17.6px] tracking-[0.0025em] text-left text-[#0E1116]">{{
                  faq.question }}</span>
              <PlusIcon v-if="!faq.isOpen" class="w-6 h-6 text-[#0D4688] flex-shrink-0 ml-4" />
              <MinusIcon v-else class="w-6 h-6 text-[#0D4688] flex-shrink-0 ml-4" />
            </button>
            <div v-show="faq.is_open" class="p-4 pt-0">
              <p
                class="font-poppins text-sm font-normal leading-[18.12px] tracking-[0.004em] text-justify text-gray-700">
                {{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
  <Footer />
</template>

<script setup>
import { ref , inject,onMounted} from 'vue'
import { ClipboardIcon, ClipboardCheckIcon, FileTextIcon, PlusIcon, MinusIcon, ChevronLeftIcon, ChevronRightIcon } from 'lucide-vue-next'
import Footer from '../components/Footer.vue'


const call = inject('$call')
const steps = [
  {
    icon: ClipboardIcon,
    title: "Step 1",
    label: "Register Your NGO",
    description: "Quickly create an account and fill out basic information."
  },
  {
    icon: ClipboardCheckIcon,
    title: "Step 2",
    label: "Fill Out the Assessment",
    description: "Complete our simple, yet comprehensive assessment to highlight your organization's impact and goals."
  },
  {
    icon: FileTextIcon,
    title: "Step 3",
    label: "Submit & Access Resources",
    description: "Once submitted, gain access to tools and support tailored to help you grow."
  }
]

const testimonials = [
  {
    name: "Ayush Kumar",
    organization: "NGO A",
    image: "../public/user.jpg",
    quote: "This platform made the process of applying for support so easy. We now have more visibility and access to crucial resources."
  },
  {
    name: "Priya Sharma",
    organization: "NGO B",
    image: "../public/user.jpg",
    quote: "The assessment tool provided valuable insights into our organization's strengths and areas for improvement."
  },
  {
    name: "Rahul Verma",
    organization: "NGO C",
    image: "../public/user.jpg",
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

const faqs = ref([])

const getFaqs = async () => {
  try {
    const response = await call( 'british_asian_trust.api.get_faqs')
    faqs.value = response
  } catch (error) {
    console.error(error)
  }
}

onMounted(() => {
  getFaqs()
})

const toggleFaq = (index) => {
  faqs.value[index].isOpen = !faqs.value[index].isOpen
}
</script>