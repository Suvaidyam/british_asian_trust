<template>
  <div class="min-h-screen bg-[#EDE8E5] relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col lg:flex-row min-h-screen">
      <!-- Registration Form Section -->
      <div class="w-full lg:w-1/2 flex items-center justify-center lg:justify-start relative z-10 py-12 lg:py-6">
        <div class="w-full max-w-md bg-white rounded-lg shadow-md p-8">
          <h2 class="text-center font-semibold font-sans text-[#212529] mb-2">
            Welcome to British Asian Trust Portal
          </h2>
          <p class="text-center text-[#212529] mb-6">
            Sign up to empower your organization. Register today and gain access to surveys, personalized
            recommendations, and tools to drive impact.
          </p>

          <!-- Stepper -->
          <div class="flex items-center justify-between mb-4">
            <!-- Step 1 -->
            <div class="flex gap-2 items-center">
              <div
                :class="['w-[24px] h-[24px] rounded-full flex items-center justify-center text-[14px] text-center leading-[18.34px] font-normal', currentStep >= 1 ? 'bg-green-500 text-white' : 'bg-yellow-500 text-white']">
                1
              </div>
              <p :class="['text-[12px] leading-[18.34px]', currentStep >= 1 ? 'text-black' : 'text-gray-500']">
                Organization
              </p>
            </div>

            <!-- Process line -->
            <div :class="['flex-1 h-[2px] mx-2', currentStep >= 2 ? 'bg-green-500' : 'bg-gray-300']"></div>

            <!-- Step 2 -->
            <div class="flex gap-2 items-center">
              <div
                :class="['w-[24px] h-[24px] rounded-full flex items-center justify-center text-[14px] text-center leading-[18.34px] font-normal', currentStep >= 2 ? 'bg-green-500 text-white' : 'bg-gray-300 text-gray-500']">
                2
              </div>
              <p
                :class="['text-[12px] text-center leading-[18.34px]', currentStep >= 2 ? 'text-black' : 'text-gray-500']">
                Admin
              </p>
            </div>
          </div>

          <!-- Form -->
          <form @submit.prevent="nextStep" class="space-y-4">
            <!-- Step 1: Organization Details -->
            <div v-if="currentStep === 1" class="flex flex-col gap-4">
              <div>
                <label for="pan" class="block mb-1">Organization PAN Number</label>
                <input type="text" id="pan" v-model="pan" @input="validateField('pan')"
                  class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                  placeholder="Enter PAN number">
                <p v-if="errors.pan" class="text-red-500 text-sm mt-1">{{ errors.pan }}</p>
              </div>
              <div>
                <label for="organization" class="block mb-1">Organization</label>
                <input type="text" id="organization" v-model="organization" @input="validateField('organization')"
                  class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                  placeholder="Enter your organization name">
                <p v-if="errors.organization" class="text-red-500 text-sm mt-1">{{ errors.organization }}</p>
              </div>
              <div>
                <label for="address" class="block mb-1">Address</label>
                <input type="text" id="address" v-model="address" @input="validateField('address')"
                  class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                  placeholder="Enter your address">
                <p v-if="errors.address" class="text-red-500 text-sm mt-1">{{ errors.address }}</p>
              </div>
            </div>

            <!-- Step 2: Admin Details -->
            <div v-if="currentStep === 2" class="flex flex-col gap-4">
              <div>
                <label for="full-name" class="block text-[14px] leading-[18.34px] font-sans mb-1">Full Name</label>
                <input type="text" id="full-name" v-model="fullName" @input="validateField('fullName')"
                  class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                  placeholder="Enter your full name">
                <p v-if="errors.fullName" class="text-red-500 text-sm mt-1">{{ errors.fullName }}</p>
              </div>
              <div>
                <label for="email" class="block text-[14px] leading-[18.34px] font-sans mb-1">Email Address</label>
                <input type="email" id="email" v-model="email" @input="validateField('email')"
                  class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                  placeholder="Enter your email address">
                <p v-if="errors.email" class="text-red-500 text-sm mt-1">{{ errors.email }}</p>
              </div>
              <div>
                <label for="phone" class="block text-[14px] leading-[18.34px] font-sans mb-1">Phone Number
                  (optional)</label>
                <div class="flex rounded-md shadow-sm">
                  <span class="inline-flex items-center px-3 rounded-l-md border border-gray-300 text-gray-500 text-sm">
                    +91
                  </span>
                  <input type="tel" id="phone" v-model="phone" @input="validateField('phone')"
                    class="flex-1 min-w-0 block w-full px-3 py-2 rounded-none rounded-r-md focus:ring-red-500 focus:border-red-500 border border-gray-300 sm:text-sm"
                    placeholder="Enter your phone number">
                </div>
                <p v-if="errors.phone" class="text-red-500 text-sm mt-1">{{ errors.phone }}</p>
              </div>
              <div>
                <label for="designation" class="block text-[14px] leading-[18.34px] font-sans mb-1">Designation</label>
                <select v-model="selectedDesignation" id="designation" @change="validateField('designation')"
                  class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm">
                  <option value="" disabled>Select a designation</option>
                  <option v-for="d in designations" :key="d.name" :value="d.name">
                    {{ d.name }}
                  </option>
                </select>
                <p v-if="errors.designation" class="text-red-500 text-sm mt-1">{{ errors.designation }}</p>
              </div>
              <div class="flex items-center">
                <input id="terms" type="checkbox" v-model="termsAccepted" @change="validateField('termsAccepted')"
                  class="h-4 w-4 text-red-600 focus:ring-red-500 border-gray-300 rounded">
                <label for="terms" class="ml-2 block text-sm text-gray-900">
                  I agree with <a href="#" class="text-red-600 hover:text-red-500">terms & conditions</a>
                </label>
              </div>
              <p v-if="errors.termsAccepted" class="text-red-500 text-sm mt-1">{{ errors.termsAccepted }}</p>
            </div>

            <!-- Next/Submit button -->
            <div class="flex flex-col justify-center items-center gap-2">
              <button type="submit"
                class="w-full flex uppercase justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#CA2247] hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                {{ currentStep === 1 ? 'Fill admin information' : 'Setup the account' }}
              </button>
              <!-- "Go Back" button (only visible in step 2) -->
              <div v-if="currentStep === 2" @click="goBack" class="cursor-pointer">
                Go Back
              </div>
            </div>
          </form>

          <!-- Popup Modal -->
          <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
            <div class="bg-white bg-thankyou p-6 rounded-lg shadow-lg max-w-md w-full text-center">
              <!-- Icon section -->
              <div class="flex justify-center mb-4">
                <div class="w-[60px] h-[60px] bg-[#E6F5FB] flex items-center justify-center rounded-full">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                    class="w-8 h-8 text-[#CA2247]">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M3 8l7.39 4.03a4 4 0 004.22 0L21 8m-9 4V21" />
                  </svg>
                </div>
              </div>

              <!-- Text section -->
              <h3 class="text-xl font-semibold mb-2">Thank you for submitting your details!</h3>
              <p class="text-gray-600 text-sm mb-6">
                We've sent a verification email to your registered address. Please check your inbox and
                follow the link to verify your email. Once verified, you'll be able to set your password and
                complete your registration.
              </p>

              <!-- Button section -->
              <button @click="closeModal" class="w-full bg-[#CA2247] text-white py-2 px-4 rounded-md hover:bg-red-700">
                Close
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- SVG and Image Section -->
      <div class="hidden lg:block lg:w-1/2 relative">
        <svg class="absolute right-0 bottom-0 w-[400px] h-[400px] lg:w-[700px] lg:h-[600px]" viewBox="0 0 719 681"
          fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd"
            d="M10.6721 358.09C43.7944 290.528 148.486 299.88 203.921 248.991C237.118 218.516 233.243 164.646 260.492 128.755C298.361 78.8762 330.329 2.09349 392.93 0.0381908C454.772 -1.99227 485.461 77.4593 530.486 119.891C565.441 152.832 598.797 184.384 628.553 222.085C662.81 265.488 725.275 303.219 718.489 358.09C711.449 415.017 625.945 426.357 597.155 475.972C568.46 525.423 606.218 613.235 555.318 639.29C503.188 665.974 451.086 573.596 392.93 580.511C321.677 588.984 278.12 686.509 206.596 680.755C139.575 675.363 89.6252 610.766 54.7335 553.303C19.5091 495.292 -19.2021 419.028 10.6721 358.09Z"
            fill="#DBB729" />
        </svg>
        <img src="../../public/register1.png" alt="Two women in traditional attire"
          class="absolute inset-0 w-full h-full object-cover">
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, inject, onMounted } from 'vue'
import { useToast } from 'vue-toastification'

const currentStep = ref(1)
const pan = ref('')
const organization = ref('')
const address = ref('')
const fullName = ref('')
const email = ref('')
const phone = ref('')
const designations = ref([])
const selectedDesignation = ref('')
const termsAccepted = ref(false)
const showModal = ref(false)
const call = inject('$call')
const toast = useToast()

const errors = reactive({
  pan: '',
  organization: '',
  address: '',
  fullName: '',
  email: '',
  phone: '',
  designation: '',
  termsAccepted: ''
})

const validatePAN = (value) => {
  const panRegex = /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/
  return panRegex.test(value)
}

const validateEmail = (value) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(value)
}

const validatePhone = (value) => {
  const phoneRegex = /^[6-9]\d{9}$/
  return phoneRegex.test(value)
}

const validateField = (field) => {
  errors[field] = ''
  switch (field) {
    case 'pan':
      if (!pan.value) errors.pan = 'PAN is required'
      else if (!validatePAN(pan.value)) errors.pan = 'Invalid  PAN format'
      break
    case 'organization':
      if (!organization.value) errors.organization = 'Organization name is required'
      break
    case 'address':
      if (!address.value) errors.address = 'Address is required'
      break
    case 'fullName':
      if (!fullName.value) errors.fullName = 'Full name is required'
      break
    case 'email':
      if (!email.value) errors.email = 'Email is required'
      else if (!validateEmail(email.value)) errors.email = 'Invalid email format'
      break
    case 'phone':
      if (phone.value && !validatePhone(phone.value)) errors.phone = 'Invalid phone number'
      break
    case 'designation':
      if (!selectedDesignation.value) errors.designation = 'Designation is required'
      break
    case 'termsAccepted':
      if (!termsAccepted.value) errors.termsAccepted = 'You must accept the terms and conditions'
      break
  }
}

const validateStep1 = () => {
  validateField('pan')
  validateField('organization')
  validateField('address')
  return !errors.pan && !errors.organization && !errors.address
}

const validateStep2 = () => {
  validateField('fullName')
  validateField('email')
  validateField('phone')
  validateField('designation')
  validateField('termsAccepted')
  return !errors.fullName && !errors.email && !errors.phone && !errors.designation && !errors.termsAccepted
}

const nextStep = async () => {
  if (currentStep.value === 1) {
    if (validateStep1()) {
      currentStep.value = 2;
      toast.success("Step 1 completed successfully!", {
        position: "top-right",
        timeout: 3000,
        closeOnClick: true,
        pauseOnFocusLoss: true,
        pauseOnHover: true,
        draggable: true,
        draggablePercent: 0.6,
        showCloseButtonOnHover: false,
        hideProgressBar: true,
        closeButton: "button",
        icon: true,
        rtl: false
      });
    } else {
      toast.error('Please fill in all required fields correctly.', {
        position: "top-right",
        timeout: 3000,
        closeOnClick: true,
        pauseOnFocusLoss: true,
        pauseOnHover: true,
        draggable: true,
        draggablePercent: 0.6,
        showCloseButtonOnHover: false,
        hideProgressBar: true,
        closeButton: "button",
        icon: true,
        rtl: false
      });
    }
  } else {
    if (validateStep2()) {
      try {
        const result = await call('british_asian_trust.api.register_organization', {
          pan: pan.value,
          organization_name: organization.value,
          organization_address: address.value,
          full_name: fullName.value,
          email: email.value,
          organization_phone: phone.value,
          role_in_organization: selectedDesignation.value,
          termsAccepted: termsAccepted.value,
        });
        showModal.value = true;
        toast.success('Registration successful!', {
          position: "top-right",
          timeout: 3000,
          closeOnClick: true,
          pauseOnFocusLoss: true,
          pauseOnHover: true,
          draggable: true,
          draggablePercent: 0.6,
          showCloseButtonOnHover: false,
          hideProgressBar: true,
          closeButton: "button",
          icon: true,
          rtl: false
        });
        console.log('Success:', result);
      } catch (error) {
        console.error('API Error:', error);
        toast.error('An error occurred during registration. Please try again.', {
          position: "top-right",
          timeout: 3000,
          closeOnClick: true,
          pauseOnFocusLoss: true,
          pauseOnHover: true,
          draggable: true,
          draggablePercent: 0.6,
          showCloseButtonOnHover: false,
          hideProgressBar: true,
          closeButton: "button",
          icon: true,
          rtl: false
        });
      }
    } else {
      toast.error('Please fill in all required fields correctly.', {
        position: "top-right",
        timeout: 3000,
        closeOnClick: true,
        pauseOnFocusLoss: true,
        pauseOnHover: true,
        draggable: true,
        draggablePercent: 0.6,
        showCloseButtonOnHover: false,
        hideProgressBar: true,
        closeButton: "button",
        icon: true,
        rtl: false
      });
    }
  }
};

const fetchDesignations = async () => {
  try {
    const result = await call('british_asian_trust.api.get_designations');
    console.log('Designations:', result);
    designations.value = result;
  } catch (error) {
    console.error('Failed to fetch designations:', error);
    toast.error('Failed to load designations. Please refresh the page.', {
      position: "top-right",
      timeout: 3000,
      closeOnClick: true,
      pauseOnFocusLoss: true,
      pauseOnHover: true,
      draggable: true,
      draggablePercent: 0.6,
      showCloseButtonOnHover: false,
      hideProgressBar: true,
      closeButton: "button",
      icon: true,
      rtl: false
    });
  }
};

onMounted(async () => {
  await fetchDesignations();
});

const goBack = () => {
  currentStep.value = 1
}

const closeModal = () => {
  showModal.value = false
}
</script>

<style scoped>
/* Your component styles */
</style>