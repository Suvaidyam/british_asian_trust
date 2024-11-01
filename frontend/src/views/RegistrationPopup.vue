<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
    <div class="bg-white rounded-lg shadow-lg p-6 w-full max-w-md">
      <h2 class="text-2xl font-bold mb-4 text-center">Complete Your Registration</h2>
      <form @submit.prevent="submitRegistration" class="space-y-4">

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
            <option v-for="designation in designations" :key="designation?.name" :value="designation?.name">
              {{ designation?.name }}
            </option>
          </select>
        </div>
        <div class="flex justify-between items-center">
          <button type="submit"
            class="w-full bg-[#CA2247] text-white py-2 px-4 rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
            Complete Sign Up
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue'
import { useToast } from 'vue-toastification'
const call = inject('$call')

const emit = defineEmits(['registration-complete'])
const toast = useToast()

const formData = ref({
  organization: '',
  designation: '',
})

const designations = ref([])

const fetchDesignations = async () => {
  try {
    let response = await call('british_asian_trust.api.get_designations')
    designations.value = response
  } catch (error) {
    console.error('Failed to fetch designations:', error)
    toast.error('Failed to fetch designations. Please try again.')
  }
}

const submitRegistration = async () => {
  try {
    let response = await call('british_asian_trust.api.complate_registration', {
      organization: formData.value.organization,
      designation: formData.value.designation,
    })
    if (response.code == 'SUC_200') {
      emit('registration-complete')
      toast.success(response.message, { position: "top-right", timeout: 3000 })
    } else {
      toast.error(response.message, { position: "top-right", timeout: 3000 });
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