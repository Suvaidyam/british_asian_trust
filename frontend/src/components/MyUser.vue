<template>
  <div class="min-h-screen bg-gray-100 px-8 sm:px-16 py-4">
    <div class="max-w-7xl mx-auto bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Header -->
      <div class="p-4 flex flex-col md:flex-row justify-between items-center border-b">
        <h1 class="text-2xl font-semibold text-gray-800 mb-4 md:mb-0">My Users</h1>
        <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4 w-full md:w-auto">
          <input v-model="searchQuery" type="text" placeholder="Search by name"
            class="px-3 py-1.5 placeholder:text-xs border rounded-md focus:outline-none focus:ring-2 focus:ring-pink-500 w-full sm:w-auto" />
          <button @click="openModal"
            class="px-3 py-1.5 text-sm bg-[#CA2247] text-white rounded-md hover:bg-pink-700 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:ring-offset-2 w-full sm:w-auto">
            INVITE NEW USER
          </button>
        </div>
      </div>

      <!-- Top Achiever Section -->
      <div class="relative bg-my-user p-8">
        <div class="absolute inset-0 bg-pink-200 opacity-50 radial-gradient"></div>
        <h2 class="text-center text-xl font-semibold mb-6 relative z-10">Top Achiever</h2>
        <div
          class="flex flex-col sm:flex-row items-center justify-around space-y-8 sm:space-y-0 sm:space-x-8 relative ">
          <div class="text-center">
            <img src="../../public/user.png" alt="Ashok Sharma"
              class="w-20 h-20 rounded-full mx-auto mb-2 border-2 border-white" />
            <p class="font-medium">Ashok Sharma</p>
            <p class="text-sm text-gray-600">Associate</p>
          </div>
          <div class="text-center sm:-mb-4">
            <div class="relative">
              <img src="../../public/user.png" alt="Meena Kumar"
                class="w-24 h-24 rounded-full mx-auto mb-2 border-2 border-white" />
              <span class="absolute top-0 right-0 bg-yellow-400 p-1 rounded-full">
                <AwardIcon class="h-4 w-4 text-white" />
              </span>
            </div>
            <p class="font-medium">Meena Kumar</p>
            <p class="text-sm text-gray-600">Manager</p>
          </div>
          <div class="text-center">
            <img src="../../public/user.png" alt="Jitesh Sharma"
              class="w-20 h-20 rounded-full mx-auto mb-2 border-2 border-white" />
            <p class="font-medium">Jitesh Sharma</p>
            <p class="text-sm text-gray-600">Associate</p>
          </div>
        </div>
      </div>

      <!-- User Listing -->
      <div class="p-4">
        <h3 class="text-lg font-semibold mb-4">Users Listing</h3>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Role</th>
                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Number</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="(user, index) in paginatedUsers" :key="user.id">
                <td class="px-6 py-2 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 h-10 w-10">
                      <img class="h-10 w-10 rounded-full" :src="user.avatar" :alt="user.name" />
                    </div>
                    <div class="ml-4">
                      <div class="text-sm font-medium text-gray-900">{{ user.name }}</div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">{{ user.email }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">{{ user.role }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <span class="text-gray-900">{{ (currentPage - 1) * itemsPerPage + index + 1 }}</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <Pagination :current-page="currentPage" :total-items="filteredUsers.length" :items-per-page="itemsPerPage"
          :max-visible-pages="5" @page-change="onPageChange" />
      </div>
    </div>

    <!-- Invite User Modal -->
    <div v-if="showModal"
      class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center z-20">
      <div class="bg-white p-8 rounded-lg shadow-xl max-w-md w-full m-4">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-semibold">Invite User</h2>
          <button @click="closeModal" class="text-gray-500 hover:text-gray-700">
            <XIcon class="h-6 w-6" />
          </button>
        </div>
        <form @submit.prevent="sendInvitation" class="space-y-4">
          <div>
            <label for="fullName" class="block text-sm font-medium text-gray-700">Full Name</label>
            <input type="text" id="fullName" v-model="newUser.fullName" @input="validateFullName"
              placeholder="Enter user full name"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pink-500 focus:border-pink-500 sm:text-sm"
              :class="{ 'border-red-500': errors.fullName }" required>
            <p v-if="errors.fullName" class="mt-1 text-sm text-red-600">{{ errors.fullName }}</p>
          </div>
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">Email Address</label>
            <input type="email" id="email" v-model="newUser.email" @input="validateEmail"
              placeholder="Enter user email address"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pink-500 focus:border-pink-500 sm:text-sm"
              :class="{ 'border-red-500': errors.email }" required>
            <p v-if="errors.email" class="mt-1 text-sm text-red-600">{{ errors.email }}</p>
          </div>
          <div>
            <label for="designation" class="block text-sm font-medium text-gray-700">Designation</label>
            <select id="designation" v-model="newUser.designation" @change="validateDesignation"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pink-500 focus:border-pink-500 sm:text-sm"
              :class="{ 'border-red-500': errors.designation }" required>
              <option value="">Select designation</option>
              <option v-for="designation in designations" :key="designation" :value="designation">
                {{ designation.name }}
              </option>
            </select>
            <p v-if="errors.designation" class="mt-1 text-sm text-red-600">{{ errors.designation }}</p>
          </div>
          <div>
            <label for="mobile" class="block text-sm font-medium text-gray-700">Mobile Number (Optional)</label>
            <div class="mt-1 flex rounded-md shadow-sm">
              <span
                class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 sm:text-sm">
                +91
              </span>
              <input type="tel" id="mobile" v-model="newUser.mobile" @input="validateMobile"
                placeholder="Enter your phone number"
                class="flex-1 block w-full border border-gray-300 rounded-none rounded-r-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pink-500 focus:border-pink-500 sm:text-sm"
                :class="{ 'border-red-500': errors.mobile }">
            </div>
            <p v-if="errors.mobile" class="mt-1 text-sm text-red-600">{{ errors.mobile }}</p>
          </div>
          <button type="submit"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#CA2247] hover:bg-pink-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pink-500 disabled:opacity-50 disabled:cursor-not-allowed"
            :disabled="!isFormValid">
            SEND INVITATION
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, inject, watch } from 'vue'
import { AwardIcon, XIcon } from 'lucide-vue-next'
import Pagination from '../components/Pagnation.vue'
import { useToast } from 'vue-toastification'

const call = inject('$call')
const toast = useToast()
const users = ref([])
const showModal = ref(false)
const searchQuery = ref('')
const newUser = ref({
  fullName: '',
  email: '',
  designation: '',
  mobile: ''
})
const designations = ref([])
const errors = ref({
  fullName: '',
  email: '',
  designation: '',
  mobile: ''
})

const currentPage = ref(1)
const itemsPerPage = ref(10)
const totalPages = ref(0) 


const filteredUsers = computed(() => {
  return users.value.filter(user =>
    user.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})


const paginatedUsers = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  return filteredUsers.value.slice(start, end)
})

const isFormValid = computed(() => {
  return !errors.value.fullName && !errors.value.email && !errors.value.designation && !errors.value.mobile &&
    newUser.value.fullName && newUser.value.email && newUser.value.designation
})

const openModal = () => {
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
  newUser.value = { fullName: '', email: '', designation: '', mobile: '' }
  errors.value = { fullName: '', email: '', designation: '', mobile: '' }
}

const validateFullName = () => {
  if (!newUser.value.fullName) {
    errors.value.fullName = 'Full name is required'
  } else if (newUser.value.fullName.length < 2) {
    errors.value.fullName = 'Full name must be at least 2 characters long'
  } else {
    errors.value.fullName = ''
  }
}

const validateEmail = () => {
  const emailRegex = /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/
  if (!newUser.value.email) {
    errors.value.email = 'Email is required'
  } else if (!emailRegex.test(newUser.value.email)) {
    errors.value.email = 'Invalid email format'
  } else {
    errors.value.email = ''
  }
}

const validateDesignation = () => {
  if (!newUser.value.designation) {
    errors.value.designation = 'Designation is required'
  } else {
    errors.value.designation = ''
  }
}

const validateMobile = () => {
  const mobileRegex = /^[6-9]\d{9}$/
  if (newUser.value.mobile && !mobileRegex.test(newUser.value.mobile)) {
    errors.value.mobile = 'Invalid mobile number (10 digits starting with 6-9)'
  } else {
    errors.value.mobile = ''
  }
}

const sendInvitation = async () => {
  if (!isFormValid.value) {
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
    })
    return
  }

  try {
    const result = await call('british_asian_trust.api.register_invities_user', {
      full_name: newUser.value.fullName,
      email_address: newUser.value.email,
      mobile_number: newUser.value.mobile,
      designation: newUser.value.designation.name,
    })
    toast.success('User invitation sent successfully!', {
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
    console.log('Success:', result)
    await fetchUsers()
    closeModal()
  } catch (error) {
    console.error('API Error:', error)
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
    })
  }
}

const fetchDesignations = async () => {
  try {
    const result = await call('british_asian_trust.api.get_designations')
    designations.value = result
  } catch (error) {
    console.error('Failed to fetch designations:', error)
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
    })
  }
}

const fetchUsers = async () => {
  try {
    const result = await call('british_asian_trust.api.get_bat_users')
    users.value = result.map(user => ({
      id: user.name,
      name: user.full_name,
      email: user.name,
      role: user.designation,
      avatar: user.avatar || '../../public/user.png'
    }))
    totalPages.value = Math.ceil(users.value.length / itemsPerPage.value)
  } catch (error) {
    console.error('Failed to fetch users:', error)
    toast.error('Failed to load users. Please refresh the page.', {
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
}

const onPageChange = (page) => {
  currentPage.value = page
}

watch(searchQuery, () => {
  currentPage.value = 1
})

onMounted(() => {
  fetchDesignations()
  fetchUsers()
})
</script>

<style scoped>
.radial-gradient {
  background: radial-gradient(circle, rgba(252, 231, 243, 1) 0%, rgba(252, 231, 243, 0) 70%);
}
</style>