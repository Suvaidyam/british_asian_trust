<template>
  <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg p-8 max-w-md w-full">
      <h2 class="text-2xl font-bold mb-4">Change Password</h2>
      <form @submit.prevent="changePassword">
        <div class="mb-4">
          <label for="newPassword" class="block text-sm font-medium text-gray-700">New Password</label>
          <input type="password" id="newPassword" v-model="newPassword" required
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
        </div>
        <div class="mb-4">
          <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Confirm New Password</label>
          <input type="password" id="confirmPassword" v-model="confirmPassword" required
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
        </div>
        <div class="flex justify-end">
          <button type="button" @click="$emit('close')"
            class="mr-2 px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300">Cancel</button>
          <button type="submit"
            class="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700">Change
            Password</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits, inject } from 'vue'
import { useToast } from 'vue-toastification'


const toast = useToast()
const call = inject('$call')
const $auth = inject('$auth')
const props = defineProps({
  isOpen: Boolean
})

const emit = defineEmits(['close'])

const newPassword = ref('')
const confirmPassword = ref('')

const changePassword = async () => {
  if (newPassword.value !== confirmPassword.value) {
    toast.info("Conform passwords do not match", {
      position: "top-right",
      timeout: 3000,
    })
    return
  }
  try {
    let user = await call('frappe.desk.form.load.getdoc', {
      doctype: 'User',
      name: $auth.user.name
    })
    if (user.docs) {
      user.docs[0].new_password = newPassword.value
      let response = await call('frappe.desk.form.save.savedocs', {
        doc: JSON.stringify(user.docs[0]),
        action: 'Save'
      })
      console.log(response, 'Response')
      if (response) {
        toast.success("Password changed successfully", {
          position: "top-right",
          timeout: 3000,
        })
        emit('close')
      }
    }

  } catch (error) {
    console.error(error, 'Error in change password')
  }
}
</script>