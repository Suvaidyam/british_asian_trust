<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center p-4">
    <div class="w-full max-w-[1512px] flex flex-col lg:flex-row bg-white  shadow-2xl overflow-hidden">
      <!-- Image Section -->
      <div class="lg:w-1/2 h-64 lg:h-screen relative">
        <img src="/login1.png" alt="Two women in traditional attire" class="object-cover w-full h-full" />
      </div>
      <!-- Registration Completion Form Section -->
      <div class="lg:w-1/2 p-4 sm:p-8 flex flex-col justify-center items-center bg-white">
        <div class="w-full max-w-lg">
          <h2
            class="font-poppins text-[24px] font-semibold leading-[28px] lg:text-[34px] lg:leading-[37.4px] text-[#0D4688] mb-4 sm:mb-6 text-center">
            Complete Your Registration
          </h2>
          <form @submit.prevent="submitRegistration" class="space-y-4">
            <div>
              <label for="organization"
                class="block font-poppins text-[14px] font-normal leading-[18.34px] text-[#2F2F2F] mb-1">Organization</label>
              <div class="relative">
                <input type="text" id="organization" v-model="formData.organization"
                  :readonly="props.user.bat_organization"
                  :value="props.user.bat_organization"
                  class="w-full px-4 h-12 pl-10 border border-gray-300 rounded-md font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#2F2F2F] focus:outline-none focus:ring-2 focus:ring-[#0D4688] focus:border-[#0D4688]"
                  placeholder="Enter your organization" />

                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <BuildingIcon class="h-5 w-5 text-gray-400" />
                </div>
              </div>
            </div>
            <div>
              <label for="designation"
                class="block font-poppins text-[14px] font-normal leading-[18.34px] text-[#2F2F2F] mb-1">Designation</label>
              <div class="relative">
                <select id="designation" v-model="formData.designation" required
                  class="w-full px-4 h-12 pl-10 border border-gray-300 rounded-md font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#2F2F2F] focus:outline-none focus:ring-2 focus:ring-[#0D4688] focus:border-[#0D4688] appearance-none">
                  <option value="">Select a designation</option>
                  <option v-for="designation in designations" :key="designation?.name" :value="designation?.name">
                    {{ designation?.name }}
                  </option>
                </select>
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <UserIcon class="h-5 w-5 text-gray-400" />
                </div>
                <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  <ChevronDownIcon class="h-5 w-5 text-gray-400" />
                </div>
              </div>
            </div>
            <div>
              <button type="submit"
                class="w-full bg-orange-500 text-white h-12 px-4 rounded-full hover:bg-orange-600 transition duration-300 font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">
                Complete Sign Up
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue'
import { useToast } from 'vue-toastification'
import { BuildingIcon, UserIcon, ChevronDownIcon } from 'lucide-vue-next'

const call = inject('$call')

const emit = defineEmits(['registration-complete', 'close-popup'])
const props = defineProps(['user'])
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
    toast.error('Failed to fetch designations. Please try again.', {
      position: "top-right",
      timeout: 5000,
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
    })
  }
}

const submitRegistration = async () => {
  try {
    let response = await call('british_asian_trust.api.complate_registration', {
      organization: props.user.bat_organization || formData.value.organization,
      designation: formData.value.designation,
    })
    if (response.code === 'SUC_200') {
      emit('registration-complete')
      toast.success(response.message, {
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
      })
      emit('close-popup')
    } else {
      toast.error(response.message, {
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
      })
    }
  } catch (error) {
    console.error('Registration error:', error)
    toast.error('Failed to complete registration. Please try again.', {
      position: "top-right",
      timeout: 5000,
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
    })
  }
}

onMounted(() => {
  fetchDesignations()
})
</script>