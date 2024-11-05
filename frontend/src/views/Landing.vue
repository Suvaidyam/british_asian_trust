<template>
  <div class="min-h-screen bg-white">
    <!-- Main container -->
    <div class="max-w-[1920px] mx-auto">
      <!-- Hero Section -->
      <section class="relative pb-12 px-4 sm:px-6 lg:px-8 overflow-hidden">
        <NavBar />
        <div class="absolute bg-effect w-3/4 h-3/4">
          <img src="/effect.png" alt="Background effect">
        </div>
        <div class="max-w-[1920px] mx-auto relative">
          <div class="mx-4 sm:mx-8 md:mx-12 lg:mx-28">
            <h1
              class="font-poppins text-3xl sm:text-4xl md:text-[40px] font-bold leading-tight sm:leading-[44px] text-center text-[#0D4688] mb-4">
              Empowering NGOs to Drive Impact
            </h1>
            <p
              class="font-poppins text-base sm:text-lg md:text-[19px] font-normal leading-snug sm:leading-[20.9px] tracking-[0.5px] text-[#212529] text-center mb-8 max-w-[750px] mx-auto">
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
      <section class="py-12 sm:py-16 px-4 sm:px-6 lg:px-8 bg-[#F4F4F4]">
        <div class="max-w-[1920px] mx-auto">
          <div class="md:flex md:items-start md:justify-between mb-8 md:mb-12 lg:mb-16">
            <div class="relative flex-shrink-0 mb-6 md:mb-0 md:mr-8 lg:mr-12">
              <div class="absolute inset-0 bg-[#BBCDE3] rounded-full h-14 w-14 sm:h-16 sm:w-16 md:h-20 md:w-20"></div>
              <h2
                class="font-poppins text-3xl sm:text-4xl md:text-[48px] font-bold leading-tight sm:leading-[52.8px] text-left text-[#0D4688] relative z-10 p-3 sm:p-4">
                About Us
              </h2>
            </div>
            <p
              class="font-poppins text-base sm:text-lg md:text-[20px] font-normal leading-relaxed sm:leading-[30px] md:leading-[40px] text-justify text-[#212529] max-w-2xl md:max-w-3xl lg:max-w-4xl">
              Our portal is designed to streamline the process for NGOs to register, assess their impact,
              and connect with resources. We believe in supporting non-governmental organizations by
              providing them with an easy and transparent way to showcase their work and secure the
              support they need to drive change.
            </p>
          </div>
          <div class="md:flex md:space-x-8">
            <!-- Steps Section -->
            <div class="w-full md:w-1/2 relative mb-8 lg:my-14">
              <div
                class="absolute left-5 sm:left-7 md:left-8 lg:left-10 top-10 bottom-10 border-l-2 border-dashed border-orange-400">
              </div>
              <div class="space-y-12 sm:space-y-16 md:space-y-20 lg:space-y-24 h-full flex flex-col justify-between">
                <div v-for="(step, index) in steps" :key="index"
                  class="relative flex flex-col sm:flex-row items-start sm:items-center gap-4 sm:gap-6">
                  <div
                    class="relative bg-white h-10 w-10 sm:h-14 sm:w-14 md:h-16 md:w-16 lg:h-20 lg:w-20 flex items-center justify-center z-10 rounded-full shadow-md">
                    <component :is="step.icon"
                      class="w-5 h-5 sm:w-6 sm:h-6 md:w-8 md:h-8 lg:w-10 lg:h-10 text-[#0D4688]">
                    </component>
                  </div>
                  <div class="sm:ml-4 flex-grow">
                    <p
                      class="font-poppins text-xs sm:text-sm md:text-base lg:text-[15px] font-normal leading-tight sm:leading-[21px] text-left text-[#808080]">
                      {{ step.title }}
                    </p>
                    <h4
                      class="font-poppins text-[18px] sm:text-[19px] md:text-[20px] font-medium leading-[24px] sm:leading-[26px] md:leading-[28px] text-left lg:text-[20px] lg:leading-[28px]">
                      {{ step.label }}
                    </h4>
                    <p
                      class="font-poppins text-[10px] sm:text-[11px] md:text-[12px] font-normal leading-[14px] sm:leading-[15.4px] md:leading-[16.8px] text-left sm:text-left md:text-justify lg:text-[12px] lg:leading-[16.8px] lg:text-justify text-gray-600">
                      {{ step.description }}
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <!-- Image and Button Section -->
            <div class="md:w-1/2 relative mt-8 md:mt-0">
              <div class="relative w-full md:w-4/5 mx-auto">
                <button
                  class="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2 top-0 z-10 bg-[#06A0A0] text-white py-2 px-4 sm:py-3 sm:px-6 md:px-8 lg:px-12 rounded-lg transition duration-300 font-poppins text-xl sm:text-2xl md:text-3xl font-normal leading-tight sm:leading-[40px] md:leading-[50.4px] text-center h-[50px] sm:h-[60px] md:h-[65px] w-4/5 max-w-[400px]">
                  How It Works
                </button>
                <img src="/about.png" alt="Children benefiting from NGO work"
                  class="w-full h-[300px] sm:h-[400px] md:h-[500px] lg:h-[600px] object-cover rounded-lg shadow-lg mt-8 sm:mt-12">
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- FAQ Section -->
      <section class="py-12 sm:py-16 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
        <div class="absolute bg-effect1 w-1/4 h-1/2">
          <img src="/effect.png" alt="Background effect">
        </div>
        <div class="max-w-[1920px] mx-auto relative">
          <div
            class="space-y-4 h-[587px] w-full md:w-[1060px] bg-white border-gray-[#DBDBDB] rounded-lg p-5 border mx-auto">
            <h2
              class="font-poppins text-[36px] lg:text-[48px] font-extrabold leading-[42px] lg:leading-[52.8px] text-center text-[#0D4688]">
              FAQs
            </h2>
            <div v-for="(faq, index) in faqs" :key="index" class="border-b-[1px] border-gray-[#DBDBDB]">
              <button @click="toggleFaq(index)" class="flex justify-between items-center w-full p-4 text-left">
                <span
                  class="font-poppins text-[14px] font-medium leading-[16px] tracking-[0.0025em] text-left lg:text-[16px] lg:leading-[17.6px] text-[#0E1116]">
                  {{ faq.question }}
                </span>
                <PlusIcon v-if="!faq.isOpen" class="w-5 h-5 sm:w-6 sm:h-6 text-[#0D4688] flex-shrink-0 ml-4" />
                <MinusIcon v-else class="w-5 h-5 sm:w-6 sm:h-6 text-[#0D4688] flex-shrink-0 ml-4" />
              </button>
              <div v-show="faq.isOpen" class="p-4 pt-0">
                <p
                  class="font-poppins text-sm font-normal leading-snug sm:leading-[18.12px] tracking-[0.004em] text-justify text-gray-700">
                  {{ faq.answer }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
  <Footer />
</template>

<script setup>
import { ref, inject, onMounted } from 'vue'
import { ClipboardIcon, ClipboardCheckIcon, FileTextIcon, PlusIcon, MinusIcon } from 'lucide-vue-next'
import Footer from '../components/Footer.vue'
import NavBar from '../components/NavBar.vue'

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

const faqs = ref([])

const getFaqs = async () => {
  try {
    const response = await call('british_asian_trust.api.get_faqs')
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

<style scoped>
/* Add any additional styles here if needed */
</style>