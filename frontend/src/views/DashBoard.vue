<template>
  <div class="min-h-screen bg-gray-50 font-sans">
    <!-- Main Content -->
    <main class="max-w-[1512px] mx-auto px-4 sm:px-6 md:px-8 lg:px-12 py-8">
      <div class="grid md:grid-cols-[1fr_350px] lg:grid-cols-[1fr_400px] gap-8">
        <!-- Left Content -->
        <div class="space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
            <h1
              class="font-poppins text-2xl sm:text-3xl md:text-[34px] lg:text-[34px] font-semibold leading-tight sm:leading-[37.4px] lg:leading-[37.4px] tracking-[0.0025em] text-center sm:text-left text-[#0D4688]">
              Assessment Sample Test
            </h1>
            <p
              class="font-sans text-xs sm:text-sm md:text-[12px] lg:text-[12px] font-normal leading-tight sm:leading-[13.2px] lg:leading-[13.2px] tracking-[0.004em] text-[#596C8C] mt-2 sm:mt-0">
              Posted on: <span class="font-source-sans">{{ formatDate(new Date()) }}</span>
            </p>
          </div>

          <div class="relative h-48 sm:h-64 md:h-[264px] lg:h-[300px] w-full rounded-lg overflow-hidden">
            <img src="/assessiment.png" alt="Assessment" class="w-full h-full object-cover" />
          </div>

          <div class="prose max-w-none flex flex-col gap-4">
            <p
              class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529]">
              The survey is divided into two sections - organizationalerganisational level and program level. The first
              addresses overarching organizational practices and systems that cover all aspects of your work. The second
              section focuses specifically on one of your chosen program areas, delving deeper into its operations and
              implementation. s key aspects that apply broadly across all areas of your work and the second dives deeper
              into understanding one of your chosen program areas.
            </p>
            <ul
              class="list-disc pl-5 space-y-2 font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529]">
              <li>Provide accurate and candid responses. The survey aims to assess the organization's current capacity
                and identify areas for improvement, so honesty will yield the most valuable insights.</li>
              <li>Focus on your organization's current status, not what you aspire to achieve (unless otherwise asked in
                the question). Answer questions based on existing practices and systems in place, not future
                aspirations, unless otherwise specified in the question.</li>
              <li>We strongly encourage you to conduct an internal exercise before filling this survey.</li>
            </ul>
            <p
              class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529]">
              Consider asking different-team members from various departments ((e.g., finance, program, HR, etc.) to
              provide their inputs. fill out-the survey independently. Include input fr rom multiple departments (e.g.,
              finance. program, M&E, HR, ete.) to capture a holistic view of the organization's capabilities. Engage
              senior leaders for strategic questions and operational teams for implementation-focusseslevel questions
              insights.
            </p>
            <ul
              class="list-disc pl-5 space-y-2 font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529]">
              <li>Focus on your organization's current status, not what you aspire to achieve (unless otherwise asked in
                the question). Answer questions based on existing practices and systems, in place. not future
                aspirations, unless otherwise specified in the question.  If any questions seem unclear, or if you need
                further clarification, please reach out to us. For guidance before completing the survey.</li>
            </ul>
          </div>
        </div>

        <!-- Right Sidebar -->
        <div class="space-y-6">
          <div
            class="bg-gradient-to-r from-[#0D4688] to-[#406EA3] bg-[length:200%] bg-[99.63deg] w-full sm:w-[376px] md:w-[350px] lg:w-[400px] h-auto sm:h-[114px] rounded-lg p-6 text-white">
            <h2
              class="font-poppins text-lg sm:text-xl md:text-[20px] lg:text-[20px] font-semibold leading-tight sm:leading-[22px] lg:leading-[22px] tracking-[0.0015em] text-left mb-4">
              Ready to take the survey?</h2>
            <router-link to="/assessmenttest"
              class="w-full sm:w-[180px] md:w-[200px] lg:w-[180px] h-[36px] font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-semibold leading-[15.4px] tracking-[0.0125em] text-center bg-orange-500 hover:bg-orange-600 text-white py-2 px-4 rounded-full transition-colors duration-300">
              START ASSESSMENT
            </router-link>
          </div>

          <div class="bg-white rounded-lg shadow-sm p-6 w-full sm:w-[376px] md:w-[350px] lg:w-[400px]">
            <div class="flex items-center justify-between mb-6">
              <h2 class="text-lg font-semibold">Users</h2>
              <button v-if="$auth?.user?.bat_role_profile !== 'support'" @click="showModal = true"
                class="p-2 hover:bg-gray-100 rounded-full text-blue-600 transition-colors duration-300">
                <Plus class="w-5 h-5" />
              </button>
            </div>

            <div class="space-y-4">
              <div v-for="user in teamMembers" :key="user.name" class="flex items-center gap-3">
                <img :src="user.user_image" :alt="user.name" class="w-8 h-8 rounded-full" />
                <div>
                  <h3 class="text-sm font-medium">{{ user.full_name }}</h3>
                  <p class="text-xs text-gray-500">{{ user.role_profile }}</p>
                </div>
                <span class="ml-auto text-xs text-gray-500">Joining Date: {{ formatDate(new Date(user.creation))
                  }}</span>
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
                  <div v-for="member in teamMembers" :key="member.name"
                    class="flex items-center justify-between p-2 hover:bg-gray-50 rounded-lg">
                    <div class="flex items-center gap-3">
                      <img :src="member?.user_image" :alt="member.name" class="w-8 h-8 rounded-full" />
                      <div>
                        <h3 class="text-sm font-medium">{{ member.full_name }}</h3>
                        <p class="text-xs text-gray-500">{{ member.name }}</p>
                      </div>
                    </div>
                    <div class="flex items-center gap-2">
                      <select v-model="member.role_profile" @change="handleRoleChange(member)"
                        class="text-sm border rounded-lg px-3 py-1 focus:outline-none focus:ring-2 focus:ring-blue-500">
                        <option value="Support">Support</option>
                        <option value="Primary">Primary</option>
                      </select>
                      <button @click="removeMember(member.name)"
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
  <Footer />
</template>

<script setup>
import { ref, computed, onMounted, watch, inject } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { Bell, Menu, Plus, X, Trash2 } from 'lucide-vue-next'
import RegistrationPopup from './RegistrationPopup.vue'
import Footer from '../components/Footer.vue'

const call = inject('$call')
const $auth = inject('$auth')
const router = useRouter()
const toast = useToast()

const showModal = ref(false)
const inviteEmail = ref('')
const showRegistrationPopup = ref(false)
const userName = ref('User')
const teamMembers = ref([])

const fetchTeamMember = async () => {
  try {
    let response = await call('british_asian_trust.api.get_team_members')
    teamMembers.value = response
  } catch (error) {
    console.error('Failed to fetch team members:', error)
    toast.error('Failed to fetch team members. Please try again.')
  }
}

const isValidEmail = computed(() => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(inviteEmail.value)
})

const inviteUser = async () => {
  if (isValidEmail.value && inviteEmail.value.split('@')[1] === $auth?.user?.bat_organization) {
    try {
      let response = await call('british_asian_trust.api.register_invities_user', {
        email: inviteEmail.value,
        role_profile: 'Support'
      })
      if (response.code === 'SUC_200') {
        toast.success(response.message, { position: "top-right", timeout: 3000 })
        await fetchTeamMember()
        inviteEmail.value = ''
      } else {
        toast.error(response.message, { position: "top-right", timeout: 3000 });
        inviteEmail.value = ''
      }
    } catch (error) {
      inviteEmail.value = ''
      console.error('Registration error:', error)
      toast.error('Failed to invite user. Please try again.')
    }
  } else {
    toast.error('This email does not exist in your organization', { position: "top-right", timeout: 3000 })
  }
}

const handleRoleChange = async (member) => {
  try {
    let response = await call('british_asian_trust.api.update_team_member', {
      email: member.name,
      role_profile: member.role_profile
    })
    if (response.code === 'SUC_200') {
      toast.success(response.message, { position: "top-right", timeout: 3000 })
      await fetchTeamMember()
    } else {
      toast.error(response.message, { position: "top-right", timeout: 3000 });
    }
  } catch (error) {
    console.error('Role update error:', error)
    toast.error('Failed to update role. Please try again.')
  }
}

const removeMember = async (id) => {
  try {
    let response = await call('british_asian_trust.api.remove_team_member', { email: id })
    if (response.code === 'SUC_200') {
      toast.success(response.message, { position: "top-right", timeout: 3000 })
      await fetchTeamMember()
    } else {
      toast.error(response.message, { position: "top-right", timeout: 3000 });
    }
  } catch (error) {
    console.error('Member removal error:', error)
    toast.error('Failed to remove team member. Please try again.')
  }
}

const checkUserRegistration = async () => {
  try {
    const user = await $auth.getSessionUser()
    if (user && user.social_logins && user.social_logins.length > 0) {
      userName.value = user.full_name || 'User'
      showRegistrationPopup.value = !(user?.bat_designation && user?.bat_organization)
    } else {
      showRegistrationPopup.value = false
    }
  } catch (error) {
    console.error('Error checking user registration:', error)
    showRegistrationPopup.value = false
  }
}

const completeRegistration = async () => {
  await $auth.setUserSession($auth?.cookie?.user_id)
  showRegistrationPopup.value = false
  await checkUserRegistration()
}

const formatDate = (date) => {
  return date.toLocaleDateString("en-GB", { day: '2-digit', month: '2-digit', year: 'numeric' })
}

onMounted(() => {
  fetchTeamMember()
  checkUserRegistration()
})
</script>