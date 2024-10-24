<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
    <div class="bg-white rounded-lg shadow-lg p-6 w-full max-w-md">
      <h2 class="text-2xl font-bold mb-4 text-center">Complete Your Registration</h2>
      <form @submit.prevent="submitRegistration" class="space-y-4">
        <div>
          <label for="fullName" class="block text-sm font-medium text-gray-700">Full Name</label>
          <input type="text" id="fullName" v-model="formData.fullName" required
                 class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm">
        </div>
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input type="email" id="email" v-model="formData.email" required
                 class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm">
        </div>
        <div>
          <label for="phone" class="block text-sm font-medium text-gray-700">Phone Number</label>
          <input type="tel" id="phone" v-model="formData.phone" required
                 class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm">
        </div>
        <div>
          <label for="organization" class="block text-sm font-medium text-gray-700">Organization</label>
          <input type="text" id="organization" v-model="formData.organization" required
                 class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm">
        </div>
        <div>
          <label for="designation" class="block text-sm font-medium text-gray-700">Designation</label>
          <select id="designation" v-model="formData.designation" required
                  class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm">
            <option value="">Select a designation</option>
            <option v-for="designation in designations" :key="designation" :value="designation">
              {{ designation }}
            </option>
          </select>
        </div>
        <div class="flex items-center">
          <input id="terms" type="checkbox" v-model="formData.termsAccepted" required
                 class="h-4 w-4 text-red-600 focus:ring-red-500 border-gray-300 rounded">
          <label for="terms" class="ml-2 block text-sm text-gray-900">
            I agree to the <a href="#" class="text-red-600 hover:text-red-500">terms and conditions</a>
          </label>
        </div>
        <div class="flex justify-between items-center">
          <button type="submit"
                  class="w-full bg-[#CA2247] text-white py-2 px-4 rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
            Complete Registration
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useToast } from 'vue-toastification'

const emit = defineEmits(['registration-complete'])
const toast = useToast()

const formData = ref({
  fullName: '',
  email: '',
  phone: '',
  organization: '',
  designation: '',
  termsAccepted: false
})

const designations = ref([])

const fetchDesignations = async () => {
  try {
    // Replace this with your actual API call
    const response = await fetch('/api/designations')
    designations.value = await response.json()
  } catch (error) {
    console.error('Failed to fetch designations:', error)
    toast.error('Failed to load designations. Please try again.')
  }
}

const submitRegistration = async () => {
  try {
    // Replace this with your actual API call
    const response = await fetch('/api/complete-registration', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData.value),
    })

    if (response.ok) {
      toast.success('Registration completed successfully!')
      emit('registration-complete')
    } else {
      throw new Error('Registration failed')
    }
  } catch (error) {
    console.error('Registration error:', error)
    toast.error('Failed to complete registration. Please try again.')
  }
}

onMounted(() => {
  fetchDesignations()
})
</script>