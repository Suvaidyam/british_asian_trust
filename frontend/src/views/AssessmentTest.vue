<template>
  <div class="relative min-h-screen font-poppins" :class="{ 'blur-sm': showPopup }">
    <NavBar />
    <div class="absolute bg-effect w-3/4 h-3/4">
      <img src="/effect.png" alt="Background effect">
    </div>
    <div class="max-w-[1920px] mx-auto">
      <FormView :doctype="'Assessment'" :sidebar="true" :section="false" :isRoute="'/assessmentresults'"></FormView>
    </div>
  </div>

  <!-- Organization Profile Popup -->
  <div v-if="showPopup" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-3xl w-full">
      <h2 class="text-[24px] font-semibold leading-[28px] lg:text-[34px] lg:leading-[37.4px] text-[#0D4688] mb-6 text-center">Organization Profile</h2>
      <form @submit.prevent="submitProfile">
        <div v-for="(question, index) in questions" :key="index" class="mb-6">
          <label :for="'question' + index" class="block mb-2 font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-[#2F2F2F]">{{ question.text }}</label>
          <input v-if="question.type === 'text'"
                 :id="'question' + index"
                 v-model="answers[index]"
                 type="text"
                 class="w-full px-4 h-12 border border-gray-300 rounded-md font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#2F2F2F] focus:outline-none focus:ring-2 focus:ring-[#0D4688] focus:border-[#0D4688]"
                 :required="question.required"
                 :aria-required="question.required"
                 :placeholder="question.text">
          <select v-else-if="question.type === 'select'"
                  :id="'question' + index"
                  v-model="answers[index]"
                  class="w-full px-4 h-12 border border-gray-300 rounded-md font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#2F2F2F] focus:outline-none focus:ring-2 focus:ring-[#0D4688] focus:border-[#0D4688]"
                  :required="question.required"
                  :aria-required="question.required">
            <option value="" disabled>Select an option</option>
            <option v-for="option in question.options" :key="option" :value="option">{{ option }}</option>
          </select>
        </div>
        <button type="submit" 
                :disabled="isSubmitting"
                class="w-full bg-orange-500 text-white h-12 px-4 rounded-full hover:bg-orange-600 transition duration-300 font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] flex items-center justify-center disabled:opacity-50 disabled:cursor-not-allowed">
          <span v-if="!isSubmitting">Submit Profile</span>
          <span v-else class="flex items-center">
            <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Processing...
          </span>
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import NavBar from '../components/NavBar.vue';
import { FormView } from '../../../../sva_form_vuejs/form_view';

const showPopup = ref(true);
const isSubmitting = ref(false);
const questions = [
  { text: "Organization Name", type: "text", required: true },
  { text: "Industry", type: "select", options: ["Technology", "Healthcare", "Finance", "Education", "Manufacturing", "Other"], required: true },
  { text: "Number of Employees", type: "select", options: ["1-10", "11-50", "51-200", "201-500", "501-1000", "1000+"], required: true },
  { text: "Founded Year", type: "text", required: false },
  { text: "Primary Focus", type: "select", options: ["B2B", "B2C", "Both"], required: true },
  { text: "Website", type: "text", required: false }
];
const answers = ref(Array(questions.length).fill(''));

const submitProfile = async () => {
  isSubmitting.value = true;
  try {
    console.log('Organization Profile submitted:', answers.value);
    showPopup.value = false;
  } catch (error) {
    console.error('Error submitting profile:', error);
  } finally {
    isSubmitting.value = false;
  }
};

onMounted(() => {
  showPopup.value = true;
});
</script>

<style scoped>
@media (max-width: 640px) {
  .overflow-x-auto {
    -webkit-overflow-scrolling: touch;
  }
}
</style>