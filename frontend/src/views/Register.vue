
<template>
  <div class="flex justify-center min-h-screen bg-gray-100 p-4 sm:p-0">
    <div class="w-full max-w-[2048px] flex flex-col lg:flex-row shadow-2xl">
      <!-- Image Section -->
      <div class="lg:w-1/2 h-64 lg:h-auto">
        <img
          src="../../public/login1.png"
          alt="Two women in traditional attire"
          class="object-cover w-full h-full"
        />
      </div>
      <!-- Registration Form Section -->
      <div class="lg:w-1/2 p-4 sm:p-8 flex flex-col justify-center items-center bg-white">
        <div class="w-full max-w-md">
          <h1 class="text-xl sm:text-2xl font-bold text-blue-900 mb-4 sm:mb-6 text-center">
            Welcome to British Asian Trust Portal
          </h1>
          <p class="text-sm sm:text-base text-gray-600 mb-6 sm:mb-8 text-center">
            Sign up to empower your organization. Register today and gain access to surveys,
            personalized recommendations, and tools to drive impact.
          </p>
 
          <!-- Stepper -->
          <div class="flex items-center justify-between mb-4">
            <div class="flex gap-2 items-center">
              <div
                :class="['w-[24px] h-[24px] rounded-full flex items-center justify-center text-[14px] text-center leading-[18.34px] font-normal', currentStep >= 1 ? 'bg-green-500 text-white' : 'bg-yellow-500 text-white']">
                1
              </div>
              <p :class="['text-[12px] leading-[18.34px]', currentStep >= 1 ? 'text-black' : 'text-gray-500']">
                Organization
              </p>
            </div>
            <div :class="['flex-1 h-[2px] mx-2', currentStep >= 2 ? 'bg-green-500' : 'bg-gray-300']"></div>
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
            <div v-if="currentStep === 1" class="space-y-4">
              <div>
                <label for="pan" class="sr-only">Organization PAN Number</label>
                <input type="text" id="pan" v-model="pan" @input="validateField('pan')"
                  class="w-full px-4 py-2 border border-gray-300 rounded-full"
                  placeholder="Organization PAN Number">
                <p v-if="errors.pan" class="text-red-500 text-xs mt-1">{{ errors.pan }}</p>
              </div>
              <div>
                <label for="organization" class="sr-only">Organization</label>
                <input type="text" id="organization" v-model="organization" @input="validateField('organization')"
                  class="w-full px-4 py-2 border border-gray-300 rounded-full"
                  placeholder="Organization Name">
                <p v-if="errors.organization" class="text-red-500 text-xs mt-1">{{ errors.organization }}</p>
              </div>
              <div>
                <label for="address" class="sr-only">Address</label>
                <input type="text" id="address" v-model="address" @input="validateField('address')"
                  class="w-full px-4 py-2 border border-gray-300 rounded-full"
                  placeholder="Address">
                <p v-if="errors.address" class="text-red-500 text-xs mt-1">{{ errors.address }}</p>
              </div>
            </div>
 
            <!-- Step 2: Admin Details -->
            <div v-if="currentStep === 2" class="space-y-4">
              <div>
                <label for="full-name" class="sr-only">Full Name</label>
                <input type="text" id="full-name" v-model="fullName" @input="validateField('fullName')"
                  class="w-full px-4 py-2 border border-gray-300 rounded-full"
                  placeholder="Full Name">
                <p v-if="errors.fullName" class="text-red-500 text-xs mt-1">{{ errors.fullName }}</p>
              </div>
              <div>
                <label for="email" class="sr-only">Email Address</label>
                <input type="email" id="email" v-model="email" @input="validateField('email')"
                  class="w-full px-4 py-2 border border-gray-300 rounded-full"
                  placeholder="Email Address">
                <p v-if="errors.email" class="text-red-500 text-xs mt-1">{{ errors.email }}</p>
              </div>
              <div>
                <label for="phone" class="sr-only">Phone Number (optional)</label>
                <div class="flex rounded-full overflow-hidden border border-gray-300">
                  <span class="inline-flex items-center px-3 bg-gray-100 text-gray-500 text-sm">
                    +91
                  </span>
                  <input type="tel" id="phone" v-model="phone" @input="validateField('phone')"
                    class="flex-1 px-4 py-2 focus:outline-none"
                    placeholder="Phone Number (optional)">
                </div>
                <p v-if="errors.phone" class="text-red-500 text-xs mt-1">{{ errors.phone }}</p>
              </div>
              <div>
                <label for="designation" class="sr-only">Designation</label>
                <select v-model="selectedDesignation" id="designation" @change="validateField('designation')"
                  class="w-full px-4 py-2 border border-gray-300 rounded-full appearance-none bg-white">
                  <option value="" disabled selected>Select a designation</option>
                  <option v-for="d in designations" :key="d.name" :value="d.name">
                    {{ d.name }}
                  </option>
                </select>
                <p v-if="errors.designation" class="text-red-500 text-xs mt-1">{{ errors.designation }}</p>
              </div>
              <div class="flex items-center">
                <input id="terms" type="checkbox" v-model="termsAccepted" @change="validateField('termsAccepted')"
                  class="h-4 w-4 text-orange-600 focus:ring-orange-500 border-gray-300 rounded">
                <label for="terms" class="ml-2 block text-sm text-gray-900">
                  I agree with <a href="#" class="text-orange-600 hover:text-orange-500">terms & conditions</a>
                </label>
              </div>
              <p v-if="errors.termsAccepted" class="text-red-500 text-xs mt-1">{{ errors.termsAccepted }}</p>
            </div>
 
            <!-- Next/Submit button -->
            <div class="flex flex-col justify-center items-center gap-2">
              <button type="submit"
                class="w-full bg-orange-500 text-white py-2 px-4 rounded-full hover:bg-orange-600 transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
                :disabled="!isFormValid">
                {{ currentStep === 1 ? 'Next' : 'Register' }}
              </button>
              <div v-if="currentStep === 2" @click="goBack" class="text-sm text-blue-600 hover:underline cursor-pointer">
                Go Back
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
 
  <!-- Popup Modal -->
  <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
    <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full text-center">
      <div class="flex justify-center mb-4">
        <div class="w-[60px] h-[60px] bg-[#E6F5FB] flex items-center justify-center rounded-full">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
            class="w-8 h-8 text-orange-500">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M3 8l7.39 4.03a4 4 0 004.22 0L21 8m-9 4V21" />
          </svg>
        </div>
      </div>
      <h3 class="text-xl font-semibold mb-2">Thank you for submitting your details!</h3>
      <p class="text-gray-600 text-sm mb-6">
        We've sent a verification email to your registered address. Please check your inbox and
        follow the link to verify your email. Once verified, you'll be able to set your password and
        complete your registration.
      </p>
      <button @click="closeModal" class="w-full bg-orange-500 text-white py-2 px-4 rounded-full hover:bg-orange-600">
        Close
      </button>
    </div>
  </div>
</template>
 
<script setup>
import { ref, reactive, computed, inject, onMounted } from 'vue'
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
const call = inject('$call')  // Ensure this function is injected in the parent component
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

// Validation functions
const validatePAN = (value) => /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/.test(value)
const validateEmail = (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)
const validatePhone = (value) => /^[6-9]\d{9}$/.test(value)

const validateField = (field) => {
  errors[field] = ''
  switch (field) {
    case 'pan':
      if (!pan.value) errors.pan = 'PAN is required'
      else if (!validatePAN(pan.value)) errors.pan = 'Invalid PAN format'
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

const isFormValid = computed(() => {
  if (currentStep.value === 1) {
    return pan.value && organization.value && address.value &&
           !errors.pan && !errors.organization && !errors.address
  } else {
    return fullName.value && email.value && selectedDesignation.value && termsAccepted.value &&
           !errors.fullName && !errors.email && !errors.phone && !errors.designation && !errors.termsAccepted
  }
})

const nextStep = async () => {
  if (currentStep.value === 1) {
    if (isFormValid.value) {
      currentStep.value = 2
      toast.success("Step 1 completed successfully!", { position: "top-right", timeout: 3000 })
    } else {
      toast.error('Please fill in all required fields correctly.', { position: "top-right", timeout: 3000 })
    }
  } else {
    if (isFormValid.value) {
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
        })
        showModal.value = true
        toast.success('Registration successful!', { position: "top-right", timeout: 3000 })
        console.log('Success:', result)
      } catch (error) {
        console.error('API Error:', error)
        toast.error('An error occurred during registration. Please try again.', { position: "top-right", timeout: 3000 })
      }
    } else {
      toast.error('Please fill in all required fields correctly.', { position: "top-right", timeout: 3000 })
    }
  }
}

const fetchDesignations = async () => {
  try {
    const result = await call('british_asian_trust.api.get_designations')
    designations.value = result
  } catch (error) {
    console.error('Failed to fetch designations:', error)
    toast.error('Failed to load designations. Please refresh the page.', { position: "top-right", timeout: 3000 })
  }
}

onMounted(async () => {
  await fetchDesignations()
})

const goBack = () => {
  currentStep.value = 1
}

const closeModal = () => {
  showModal.value = false
}
</script>
