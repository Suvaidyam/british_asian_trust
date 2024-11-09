<template>
  <div class="min-h-screen bg-gray-50 font-sans">
    <!-- Main Content -->
    <main class="relative max-w-[1920px] mx-auto px-4 sm:px-6 md:px-8 lg:px-12 pb-8 overflow-hidden">
      <NavBar />
      <div class="absolute bg-effect w-3/4 h-3/4">
        <img src="/effect.png" alt="Background effect">
      </div>
      
      <div class="grid md:grid-cols-[1fr_350px] lg:grid-cols-[1fr_400px] gap-8">
        <!-- Left Content -->
        <div class="space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
            <h1 class="font-poppins text-2xl sm:text-3xl md:text-[34px] lg:text-[34px] font-semibold leading-tight sm:leading-[37.4px] lg:leading-[37.4px] tracking-[0.0025em] text-center sm:text-left text-[#0D4688]">
              {{ assessmentInfo.contents[0].heading }}
            </h1>
            <p class="font-sans text-xs sm:text-sm md:text-[12px] lg:text-[12px] font-normal leading-tight sm:leading-[13.2px] lg:leading-[13.2px] tracking-[0.004em] text-[#596C8C] mt-2 sm:mt-0">
              Posted on: <span class="font-source-sans">{{ formatDate(assessmentInfo.modified) }}</span>
            </p>
          </div>

          <div class="space-y-6">
            <template v-for="(content, index) in assessmentInfo.contents" :key="index">
              <div v-if="content.type === 'Image'" class="relative h-48 sm:h-64 md:h-[264px] lg:h-[300px] w-full rounded-lg overflow-hidden">
                <img :src="content.image" :alt="content.name" class="w-full h-full object-cover" />
              </div>
              <div v-else-if="content.type === 'HTML'" class="prose max-w-none flex flex-col gap-4 dynamic-content" v-html="content.html"></div>
            </template>
          </div>
        </div>

        <!-- Right Sidebar -->
        <div class="space-y-6">
          <div class="bg-gradient-to-r from-[#0D4688] to-[#406EA3] bg-[length:200%] bg-[99.63deg] w-full sm:w-[376px] md:w-[350px] lg:w-[400px] h-auto sm:h-[114px] rounded-lg p-6 text-white">
            <h2 class="font-poppins text-lg sm:text-xl md:text-[20px] lg:text-[20px] font-semibold leading-tight sm:leading-[22px] lg:leading-[22px] tracking-[0.0015em] text-left mb-4">
              Ready to take the survey?
            </h2>
            <router-link to="/assessment" class="w-full sm:w-[180px] md:w-[200px] lg:w-[180px] h-[36px] font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-semibold leading-[15.4px] tracking-[0.0125em] text-center bg-orange-500 hover:bg-orange-600 text-white py-2 px-4 rounded-full transition-colors duration-300">
              START ASSESSMENT
            </router-link>
          </div>

          <div class="flex items-center justify-between mb-6">
            <h2 class="font-poppins text-[18px] sm:text-[19px] md:text-[20px] font-medium leading-[20px] sm:leading-[21px] md:leading-[22px] text-left lg:text-[20px] lg:leading-[22px] text-[#0D4688]">
              Users
            </h2>
            <button @click="user_popup" :class="[user?.bat_role_profile != 'Primary' ? 'hidden' : '']" class="p-1 text-white bg-[#0D4688] transition-colors duration-300">
              <Plus class="w-[15px] h-[15px]" />
            </button>
          </div>
          <div class="bg-white rounded-lg shadow-sm p-6 w-full sm:w-[376px] md:w-[350px] lg:w-[400px] border">
            <div class="space-y-4">
              <div v-for="user in teamMembers" :key="user.name" class="flex items-center gap-3 border-b pb-1">
                <img :src="user.user_image" :alt="user.name" class="w-8 h-8 rounded-full" />
                <div>
                  <h3 class="text-sm font-medium">{{ user.full_name }}</h3>
                  <p class="text-xs text-gray-500"><span v-if="user.designation">{{ user.designation }}</span><span v-else>--</span></p>
                </div>
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
          <div class="bg-white rounded-lg w-full max-w-2xl">
            <div class="p-6">
              <div class="flex items-center justify-between mb-6">
                <h2 class="font-poppins text-[20px] sm:text-[22px] md:text-[24px] font-semibold leading-[24px] sm:leading-[25.2px] md:leading-[26.4px] text-left lg:text-[24px] lg:leading-[26.4px]">
                  Invite User
                </h2>
                <button @click="user_popup" class="text-gray-500 hover:text-gray-700 transition-colors duration-300">
                  <X class="w-5 h-5" />
                </button>
              </div>

              <div class="space-y-4">
                <div class="flex gap-2">
                  <input v-model="inviteEmail" type="email" placeholder="Invite others by name or email"
                    @input="validateEmail"
                    class="flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0D4688]" />
                  <button @click="inviteUser" :disabled="!isValidEmail || !isBusinessEmail || isInviting" :class="[
                    'w-[140px] h-[40px] px-4 py-2 rounded-full transition duration-300 flex items-center justify-center font-poppins text-[14px] sm:text-[15px] md:text-[16px] font-semibold leading-[20px] sm:leading-[20.5px] md:leading-[20.96px] tracking-[0.0025em] text-left lg:text-[16px] lg:leading-[20.96px]',
                    isValidEmail && isBusinessEmail && !isInviting ? 'bg-orange-500 hover:bg-orange-600 text-white' : 'bg-gray-200 text-gray-700 cursor-not-allowed'
                  ]">
                    <span v-if="!isInviting">INVITE</span>
                    <span v-else class="flex items-center">
                      <LoaderIcon class="animate-spin h-5 w-5 text-white" />
                    </span>
                  </button>
                </div>
                <p v-if="emailError" class="text-red-500 text-xs mt-1">{{ emailError }}</p>

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
                        :disabled="member.name === user?.name"
                        class="text-sm border rounded-lg px-3 py-1 focus:outline-none focus:ring-2 focus:ring-[#0D4688]">
                        <option value="Support">Support</option>
                        <option value="Primary">Primary</option>
                      </select>
                      <button @click="removeMember(member.name)" 
                        :disabled="member.name === user?.name"
                        :class="[
                          member.name === user?.name ? 'cursor-not-allowed text-gray-400 transition-colors duration-300' : 'text-gray-400 hover:text-gray-600 transition-colors duration-300'
                        ]">
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

    <RegistrationPopup v-if="showRegistrationPopup" @registration-complete="completeRegistration" :user="user" />
  </div>
  <Footer />
</template>

<script setup>
import { ref, computed, onMounted, watch, inject } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { Bell, Menu, Plus, X, Trash2, LoaderIcon } from 'lucide-vue-next'
import RegistrationPopup from './RegistrationPopup.vue'
import Footer from '../components/Footer.vue'
import NavBar from '../components/NavBar.vue'

const call = inject('$call')
const $auth = inject('$auth')
const router = useRouter()
const toast = useToast()
const showModal = ref(false)
const inviteEmail = ref('')
const emailError = ref('')
const showRegistrationPopup = ref(false)
const user = ref(null)
const teamMembers = ref([])
const assessmentInfo = ref({})
const isInviting = ref(false)

const fetchAssessmentInfo = async () => {
  try {
    const response = await call('british_asian_trust.api.get_assessment_information')
    console.log(response, "response");
    assessmentInfo.value = response[0]
  } catch (error) {
    console.error('Failed to fetch assessment information:', error)
    toast.error('Failed to fetch assessment information. Please try again.')
  }
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-GB', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const user_popup = async () => {
  user.value = await $auth.getSessionUser()
  showModal.value = !showModal.value
}

const fetchTeamMember = async () => {
  try {
    let response = await call('british_asian_trust.api.get_team_members')
    teamMembers.value = response
  } catch (error) {
    console.error('Failed to fetch designations:', error)
    toast.error('Failed to fetch designations. Please try again.')
  }
}

const isValidEmail = computed(() => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(inviteEmail.value)
})

const isBusinessEmail = computed(() => {
  if (!isValidEmail.value) return false
  const domain = inviteEmail.value.split('@')[1].toLowerCase()
  const restrictedDomains = ['gmail.com', 'outlook.com', 'hotmail.com', 'yahoo.com']
  return !restrictedDomains.includes(domain)
})

const validateEmail = () => {
  emailError.value = ''
  if (!isValidEmail.value) {
    emailError.value = 'Please enter a valid email address.'
  } else if (!isBusinessEmail.value) {
    emailError.value = 'Please use a business email address. Personal email domains are not allowed.'
  }
}

const inviteUser = async () => {
  if (!isValidEmail.value || !isBusinessEmail.value) {
    validateEmail()
    return
  }
  if (inviteEmail.value.split('@')[1] === $auth?.user?.name.split('@')[1]) {
    try {
      isInviting.value = true
      let response = await call('british_asian_trust.api.register_invities_user', {
        email: inviteEmail.value,
        role_profile: 'Support'
      })
      if (response.code == 'SUC_200') {
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
    } finally {
      isInviting.value = false
    }
  } else {
    emailError.value = 'This email does not exist in your organization'
  }
}

const handleRoleChange = async (member) => {
  try {
    let response = await call('british_asian_trust.api.update_team_member', {
      email: member.name,
      role_profile: member.role_profile
    })
    if (response.code == 'SUC_200') {
      await $auth.setUserSession($auth?.user?.name)
      if (member.role_profile === 'Primary') {
        user_popup()
      }
      toast.success(response.message, { position: "top-right", timeout: 3000 })
      await fetchTeamMember()
    } else {
      toast.error(response.message, { position: "top-right", timeout: 3000 });
    }
  } catch (error) {
    console.error('Registration error:', error)
  }
}

const removeMember = async (id) => {
  try {
    let response = await call('british_asian_trust.api.delete_team_member', {
      email: id
    })
    if (response.code == 'SUC_200') {
      await fetchTeamMember()
      toast.success(response.message, { position: "top-right", timeout: 3000 })
    }
    else {
      toast.error(response.message, { position: "top-right", timeout: 3000 });
    }
  } catch (error) {
    console.error('Failed to remove member:', error)
  }
}

const checkUserRegistration = async () => {
  try {
    user.value = await $auth.getSessionUser()
    fetchTeamMember()
    if (user.value?.bat_designation && user.value?.bat_organization) {
      showRegistrationPopup.value = false
    } else {
      showRegistrationPopup.value = true
    }
  } catch (error) {
    console.error('Error checking user registration:', error)
    showRegistrationPopup.value = false
  }
}

const completeRegistration = async () => {
  await $auth.setUserSession($auth?.user?.name)
  showRegistrationPopup.value = false
  await checkUserRegistration()
}

onMounted(async () => {
  user.value = await $auth.getSessionUser()
  await checkUserRegistration()
  await fetchAssessmentInfo()
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
.dynamic-content {
  font-family: 'Poppins', sans-serif;
}

.dynamic-content :deep(p) {
  @apply font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529];
}

.dynamic-content :deep(ul) {
  @apply list-disc pl-5 space-y-2;
}

.dynamic-content :deep(li) {
  @apply font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529];
}
</style>