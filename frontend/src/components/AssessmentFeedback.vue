<template>
    <div class="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-lg w-full max-w-2xl p-6">
        <div class="flex items-center justify-between mb-6">
          <h2 class="font-poppins text-[20px] sm:text-[22px] md:text-[24px] font-semibold leading-[24px] sm:leading-[25.2px] md:leading-[26.4px] text-left lg:text-[24px] lg:leading-[26.4px]">Assessment Feedback</h2>
          <button @click="$emit('close')" class="text-gray-500 hover:text-gray-700 transition-colors duration-300">
            <XIcon class="w-5 h-5" />
          </button>
        </div>
  
        <p class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-[#212529] mb-6">
          We value your insights! Please take a moment to share your thoughts.
        </p>
  
        <div class="space-y-6">
          <!-- First Rating Question -->
          <div>
            <p class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-[#212529] mb-3">How easy was it for you to go through all the questions within the survey?</p>
            <div class="flex gap-2">
              <button
                v-for="n in 10"
                :key="n"
                @click="rating1 = n"
                :class="[
                  'w-10 h-10 rounded-full flex items-center justify-center border transition-colors duration-200',
                  rating1 === n 
                    ? 'bg-[#FF8A00] text-white border-[#FF8A00]' 
                    : 'border-gray-300 hover:border-[#FF8A00]'
                ]"
              >
                {{ n }}
              </button>
            </div>
          </div>
  
          <!-- Second Rating Question -->
          <div>
            <p class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-[#212529] mb-3">How relevant was the survey related to your NGO's domain and use case?</p>
            <div class="flex gap-2">
              <button
                v-for="n in 10"
                :key="n"
                @click="rating2 = n"
                :class="[
                  'w-10 h-10 rounded-full flex items-center justify-center border transition-colors duration-200',
                  rating2 === n 
                    ? 'bg-[#FF8A00] text-white border-[#FF8A00]' 
                    : 'border-gray-300 hover:border-[#FF8A00]'
                ]"
              >
                {{ n }}
              </button>
            </div>
          </div>
  
          <!-- Additional Feedback -->
          <div>
            <p class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-[#212529] mb-3">Please share any other thoughts or feedback you have regarding the assessment.</p>
            <textarea
              v-model="additionalFeedback"
              rows="4"
              placeholder="Enter your thoughts here (optional)"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0D4688] font-poppins text-sm"
            ></textarea>
          </div>
  
          <!-- Submit Button -->
          <div class="flex justify-end">
            <button
              @click="submitFeedback"
              class="w-[140px] h-[40px] px-4 py-2 rounded-full transition duration-300 flex items-center justify-center font-poppins text-[14px] sm:text-[15px] md:text-[16px] font-semibold leading-[20px] sm:leading-[20.5px] md:leading-[20.96px] tracking-[0.0025em] text-left lg:text-[16px] lg:leading-[20.96px] bg-[#FF8A00] hover:bg-[#ff9d00] text-white"
            >
              SUBMIT
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { XIcon } from 'lucide-vue-next'
  
  const rating1 = ref(0)
  const rating2 = ref(0)
  const additionalFeedback = ref('')
  
  const submitFeedback = () => {
    const feedback = {
      surveyEase: rating1.value,
      relevance: rating2.value,
      additionalFeedback: additionalFeedback.value
    }
    
    // Emit the feedback data to parent
    emit('submit', feedback)
  }
  
  // Define emits
  const emit = defineEmits(['close', 'submit'])
  </script>
  
  <style scoped>
  /* Add any component-specific styles here */
  </style>