<template>
  <div class="flex justify-center min-h-screen bg-gray-100 p-4 sm:p-0">
    <div class="w-full max-w-[2048px] flex flex-col lg:flex-row shadow-2xl">
      <!-- Image Section -->
      <div class="lg:w-1/2 h-64 lg:h-auto">
        <img src="../../public/login1.png" alt="Two women in traditional attire" class="object-cover w-full h-full" />
      </div>
      <!-- Registration Form Section -->
      <div class="lg:w-1/2 p-4 sm:p-8 flex flex-col justify-center items-center bg-white">
        <div class="w-full max-w-md">
          <h1 class="text-xl sm:text-2xl font-bold text-blue-900 mb-4 sm:mb-6 text-center">
            Join Outcome Readiness
          </h1>
          <p class="text-sm sm:text-base text-gray-600 mb-6 sm:mb-8 text-center">
            Sign up to empower your organization. Register today and gain access to surveys,
            personalized recommendations, and tools to drive impact.
          </p>

          <!-- Form -->
          <form @submit.prevent="handleSubmit" class="space-y-4">
            <div>
              <label for="full-name" class="sr-only">Full Name</label>
              <input type="text" id="full-name" v-model="fullName" @input="validateField('fullName')"
                class="w-full px-4 py-2 border border-gray-300 rounded-md" placeholder="Full Name">
              <p v-if="errors.fullName" class="text-red-500 text-xs mt-1">{{ errors.fullName }}</p>
            </div>
            <div>
              <label for="email" class="sr-only">Email Address</label>
              <input type="email" id="email" v-model="email" @input="validateField('email')"
                class="w-full px-4 py-2 border border-gray-300 rounded-md" placeholder="Email Address">
              <p v-if="errors.email" class="text-red-500 text-xs mt-1">{{ errors.email }}</p>
              <p class="text-gray-600 text-xs mt-1">Use only your work email for registration. Personal emails are not
                allowed.</p>
            </div>

            <div>
              <label for="organization" class="sr-only">Organization</label>
              <input type="text" id="organization" v-model="organization" @input="validateField('organization')"
                class="w-full px-4 py-2 border border-gray-300 rounded-md" placeholder="Organization Name">
              <p v-if="errors.organization" class="text-red-500 text-xs mt-1">{{ errors.organization }}</p>
            </div>

            <div>
              <label for="designation" class="sr-only">Designation</label>
              <select v-model="selectedDesignation" id="designation" @change="validateField('designation')"
                class="w-full px-4 py-2 border border-gray-300 rounded-md appearance-none bg-white">
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

            <button type="submit"
              class="w-full bg-orange-500 text-white py-2 px-4 rounded-full hover:bg-orange-600 transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
              :disabled="!isFormValid">
              Sign Up
            </button>
          </form>
          <div class="mt-4 text-center">
            <router-link to="/login" class="text-sm text-blue-600 hover:underline">
              Already have an account? Log in
            </router-link>
          </div>
          <div class="mt-6 flex items-center">
            <div class="flex-grow border-t border-gray-300"></div>
            <span class="flex-shrink mx-4 text-gray-600">OR</span>
            <div class="flex-grow border-t border-gray-300"></div>
          </div>
          <div class="mt-6 space-y-2">
            <button @click="handleGoogleLogin"
              class="w-full border border-gray-300 text-gray-700 py-2 px-4 rounded-full hover:bg-gray-50 transition duration-300 flex items-center justify-center">
              <svg class="h-5 w-5 mr-2" viewBox="0 0 24 24">
                <path fill="#4285F4"
                  d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
                <path fill="#34A853"
                  d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
                <path fill="#FBBC05"
                  d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" />
                <path fill="#EA4335"
                  d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
                <path fill="none" d="M1 1h22v22H1z" />
              </svg>
              Continue with Google
            </button>
            <button @click="handleMicrosoftLogin"
              class="w-full border border-gray-300 text-gray-700 py-2 px-4 rounded-full hover:bg-gray-50 transition duration-300 flex items-center justify-center">
              <svg class="h-5 w-5 mr-2" viewBox="0 0 23 23">
                <path fill="#f3f3f3" d="M0 0h23v23H0z" />
                <path fill="#f35325" d="M1 1h10v10H1z" />
                <path fill="#81bc06" d="M12 1h10v10H12z" />
                <path fill="#05a6f0" d="M1 12h10v10H1z" />
                <path fill="#ffba08" d="M12 12h10v10H12z" />
              </svg>
              Continue with Microsoft
            </button>
          </div>
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

const organization = ref('')
const fullName = ref('')
const email = ref('')
const designations = ref([])
const selectedDesignation = ref('')
const termsAccepted = ref(false)
const showModal = ref(false)
const call = inject('$call')
const toast = useToast()

const errors = reactive({
  organization: '',
  fullName: '',
  email: '',
  designation: '',
  termsAccepted: ''
})

const validateEmail = (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)

const validateField = (field) => {
  errors[field] = ''
  switch (field) {
    case 'organization':
      if (!organization.value) errors.organization = 'Organization name is required'
      break
    case 'fullName':
      if (!fullName.value) errors.fullName = 'Full name is required'
      break
    case 'email':
      if (!email.value) errors.email = 'Email is required'
      else if (!validateEmail(email.value)) errors.email = 'Invalid email format'
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
  return organization.value && fullName.value &&
    email.value && selectedDesignation.value && termsAccepted.value &&
    !errors.organization && !errors.fullName &&
    !errors.email && !errors.designation && !errors.termsAccepted
})

const handleSubmit = async () => {
  Object.keys(errors).forEach(validateField)

  if (isFormValid.value) {
    try {
      let result = await call('british_asian_trust.api.register_organization', {
        organization_name: organization.value,
        full_name: fullName.value,
        email: email.value,
        designation_in_organization: selectedDesignation.value,
        termsAccepted: termsAccepted.value,
      });

      if (result.code == 'SUC_200') {
        showModal.value = true;
        toast.success(result.message, { position: "top-right", timeout: 3000 });
      } else {
        toast.error(result.message, { position: "top-right", timeout: 3000 });
      }
    } catch (error) {
      console.error('API Error:', error);
    }
  } else {
    toast.error('Please fill in all required fields correctly.', { position: "top-right", timeout: 3000 })
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

const handleGoogleLogin = () => {
  window.location.href =
    "https://accounts.google.com/o/oauth2/auth?redirect_uri=https%3A%2F%2Fbtasian.suvaidyam.com%2Fapi%2Fmethod%2Fbritish_asian_trust.api.my_login_via_google&state=eyJzaXRlIjogImh0dHA6Ly9idGFzaWFuLnN1dmFpZHlhbS5jb20iLCAidG9rZW4iOiAiMjg1YjVhYmQ1YTY2Y2RiNGU3NTZkZmFmNmZiNWNhODc0ZDI3ZTY4M2U3NzU4NTQwZTgwMmRmZjkiLCAicmVkaXJlY3RfdG8iOiAiL2FwcC9idWlsZCJ9&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&response_type=code&client_id=720319117261-1kuhqoutuq2j8ud0b8dsp1oen4glmruq.apps.googleusercontent.com"
}

const handleMicrosoftLogin = () => {
  window.location.href =
    "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?redirect_uri=https%3A%2F%2Fbtasian.suvaidyam.com%2Fapi%2Fmethod%2Ffrappe.integrations.oauth2_logins.login_via_office365&state=eyJzaXRlIjogImh0dHA6Ly9idGFzaWFuLnN1dmFpZHlhbS5jb20iLCAidG9rZW4iOiAiZWI2Y2I3ZTVkZDY0N2QwMDVjNzQ5Y2Q3NDc2N2U4OTM3YmJkYmYwZTc5MWQyMGQ1NDUwMjkwYWYiLCAicmVkaXJlY3RfdG8iOiAiL2FwcC9idWlsZCJ9&response_type=code&scope=openid+email+profile&client_id=c28ed05b-846a-414e-b8df-bbb602316b22"
}

const closeModal = () => {
  showModal.value = false
}

onMounted(async () => {
  await fetchDesignations()
})
</script>