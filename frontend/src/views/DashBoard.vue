<template>
  <div class="min-h-screen bg-gray-50 font-sans">
    <!-- Main Content -->
    <main class="max-w-[1920px] mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="grid lg:grid-cols-[1fr_350px] gap-8">
        <!-- Left Content -->
        <div class="space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
            <h1 class="text-2xl sm:text-3xl font-bold text-gray-900">Assessment Sample Test</h1>
            <span class="text-sm text-gray-500 mt-2 sm:mt-0">Posted on: September 20, 2024</span>
          </div>

          <div class="relative h-[200px] sm:h-[300px] lg:h-[400px] rounded-lg overflow-hidden">
            <img src="/assessiment.png" alt="Assessment" class="w-full h-full object-cover" />
          </div>

          <div class="prose max-w-none">
            <p class="text-base sm:text-lg text-gray-700">
              The survey is divided into two sections - organizational level and program level. The
              first addresses overarching organizational practices and systems that cover all aspects of your work.
              The second section focuses specifically on one of your chosen program areas, delving deeper into its
              operations and implementation.
            </p>
            <ul class="list-disc pl-5 space-y-2 text-base sm:text-lg text-gray-700">
              <li>Provide accurate and candid responses. The survey aims to assess the
                organization's current capacity and identify areas for improvement, so honesty will yield the most
                valuable insights.</li>
              <li>Focus on your organization's current status, not what you aspire to achieve (unless otherwise asked
                in the question). Answer questions based on existing practices and systems in place.</li>
              <li>We strongly encourage you to conduct an internal exercise before filling this
                survey.</li>
            </ul>
            <p class="text-base sm:text-lg text-gray-700">
              Consider asking team members from various departments (e.g., finance, program, HR, etc.) to
              provide their inputs. Include input from multiple departments to capture a holistic view of the
              organization's capabilities.
              Engage senior leaders for strategic questions and operational teams for implementation-level
              insights.
            </p>
            <p class="text-base sm:text-lg text-gray-700">
              If any questions seem unclear, or if you need further clarification, please reach out to us for guidance
              before completing the survey.
            </p>
          </div>
        </div>

        <!-- Right Sidebar -->
        <div class="space-y-6">
          <div class="bg-[#0D4688] rounded-lg p-6 text-white">
            <h2 class="text-xl font-semibold mb-4">Ready to take the survey?</h2>
            <button
              class="w-full bg-orange-500 hover:bg-orange-600 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-300">
              START ASSESSMENT
            </button>
          </div>

          <div class="bg-white rounded-lg shadow-sm p-6">
            <div class="flex items-center justify-between mb-6">
              <h2 class="text-lg font-semibold">Users</h2>
              <button @click="showModal = true"
                class="p-2 hover:bg-gray-100 rounded-full text-blue-600 transition-colors duration-300">
                <Plus class="w-5 h-5" />
              </button>
            </div>

            <div class="space-y-4">
              <div v-for="user in users" :key="user.id" class="flex items-center gap-3">
                <img :src="user.avatar" :alt="user.name" class="w-8 h-8 rounded-full" />
                <div>
                  <h3 class="text-sm font-medium">{{ user.name }}</h3>
                  <p class="text-xs text-gray-500">{{ user.role }}</p>
                </div>
                <span class="ml-auto text-xs text-gray-500">Joining Date: {{ user.joinDate }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Invite Modal -->
    <Teleport to="body">
      <Transition name="fade">
        <div v-if="showModal" class="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
          <div class="bg-white rounded-lg w-full max-w-lg">
            <div class="p-6">
              <div class="flex items-center justify-between mb-6">
                <h2 class="text-xl font-semibold">Invite User</h2>
                <button @click="showModal = false"
                  class="text-gray-500 hover:text-gray-700 transition-colors duration-300">
                  <X class="w-5 h-5" />
                </button>
              </div>

              <div class="space-y-4">
                <div class="flex gap-2">
                  <input v-model="inviteEmail" type="email" placeholder="Invite others by name or email"
                    class="flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" />
                  <button @click="inviteUser" :disabled="!isValidEmail" :class="[
                    'px-4 py-2 rounded-lg transition duration-300',
                    isValidEmail ? 'bg-orange-500 hover:bg-orange-600 text-white' : 'bg-gray-200 text-gray-700 cursor-not-allowed'
                  ]">
                    INVITE
                  </button>
                </div>

                <div class="space-y-3">
                  <div v-for="member in teamMembers" :key="member.id"
                    class="flex items-center justify-between p-2 hover:bg-gray-50 rounded-lg">
                    <div class="flex items-center gap-3">
                      <img :src="member.avatar" :alt="member.name" class="w-8 h-8 rounded-full" />
                      <div>
                        <h3 class="text-sm font-medium">{{ member.name }}</h3>
                        <p class="text-xs text-gray-500">{{ member.email }}</p>
                      </div>
                    </div>
                    <div class="flex items-center gap-2">
                      <select v-model="member.role"
                        class="text-sm border rounded-lg px-3 py-1 focus:outline-none focus:ring-2 focus:ring-blue-500">
                        <option value="Support">Support</option>
                        <option value="Primary">Primary</option>
                      </select>
                      <button @click="removeMember(member.id)"
                        class="text-gray-400 hover:text-gray-600 transition-colors duration-300">
                        <Trash2 class="w-4 h-4" />
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>

    <!-- Registration Popup -->
    <RegistrationPopup v-if="showRegistrationPopup" @registration-complete="completeRegistration" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch, inject } from 'vue'
import { useRouter } from 'vue-router'
import { Bell, Menu, Plus, X, Trash2 } from 'lucide-vue-next'
import RegistrationPopup from './RegistrationPopup.vue'

const $auth = inject('$auth')
const router = useRouter()

const showModal = ref(false)
const inviteEmail = ref('')
const showRegistrationPopup = ref(false)
const userName = ref('User')

const users = ref([
  {
    id: 1,
    name: 'Aayush Kumar',
    role: 'Associate',
    joinDate: '12/10/2024',
    avatar: '/placeholder.svg?height=32&width=32'
  },
  {
    id: 2,
    name: 'Gitesh',
    role: 'Associate',
    joinDate: '12/10/2024',
    avatar: '/placeholder.svg?height=32&width=32'
  },
  {
    id: 3,
    name: 'Umesh Sharma',
    role: 'Associate',
    joinDate: '12/10/2024',
    avatar: '/placeholder.svg?height=32&width=32'
  }
])

const teamMembers = ref([
  {
    id: 1,
    name: 'Aayush Kumar',
    email: 'aayush.kumar@xyz.com',
    role: 'Support',
    avatar: '/placeholder.svg?height=32&width=32'
  },
  {
    id: 2,
    name: 'Abhinav',
    email: 'abhinav.tyagi@xyz.com',
    role: 'Primary',
    avatar: '/placeholder.svg?height=32&width=32'
  }
])

const isValidEmail = computed(() => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(inviteEmail.value)
})

const inviteUser = () => {
  if (isValidEmail.value) {
    const newMember = {
      id: teamMembers.value.length + 1,
      name: inviteEmail.value.split('@')[0],
      email: inviteEmail.value,
      role: 'Support',
      avatar: '/placeholder.svg?height=32&width=32'
    }
    teamMembers.value.push(newMember)
    inviteEmail.value = ''
  }
}

const removeMember = (id) => {
  teamMembers.value = teamMembers.value.filter(member => member.id !== id)
}

const checkUserRegistration = async () => {
  try {
    const user = await $auth.getSessionUser()
    console.log(user, 'user')
    if (user && user.social_logins && user.social_logins.length > 0) {
      userName.value = user.full_name || 'User'
      if (user?.bat_designation != null || user?.bat_organization != null) {
        showRegistrationPopup.value = false
      } else {
        showRegistrationPopup.value = true
      }
    } else {
      showRegistrationPopup.value = false
    }
  } catch (error) {
    console.error('Error checking user registration:', error)
    showRegistrationPopup.value = false
  }
}

const completeRegistration = async () => {
  showRegistrationPopup.value = false
  await checkUserRegistration()
}

onMounted(async () => {
  await checkUserRegistration()
})

watch(() => router.currentRoute.value, async () => {
  await checkUserRegistration()
})

watch(() => $auth.isLoggedIn, async (newValue) => {
  if (newValue) {
    await $auth.setUserSession($auth?.cookie?.user_id)
  }
}, { deep: true, immediate: true })
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>