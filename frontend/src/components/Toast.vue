<!-- Toast.vue -->
<template>
  <transition name="toast">
    <div v-if="visible" :class="toastClass" class="fixed top-4 right-4 px-4 py-2 rounded-md shadow-lg text-white" @click="hide">
      {{ message }}
    </div>
  </transition>
</template>

<script setup>
import { computed, ref } from 'vue'

const props = defineProps({
  message: {
    type: String,
    required: true
  },
  type: {
    type: String,
    default: 'info'
  },
  duration: {
    type: Number,
    default: 3000
  }
})

const visible = ref(true)

const toastClass = computed(() => {
  return {
    'bg-green-500': type === 'success',
    'bg-red-500': type === 'error',
    'bg-blue-500': type === 'info'
  }
})

// Automatically hide the toast after the specified duration
setTimeout(() => {
  visible.value = false
}, duration)
</script>

<style scoped>
.toast-enter-active, .toast-leave-active {
  transition: opacity 0.5s;
}
.toast-enter, .toast-leave-to /* .toast-leave-active in <2.1.8 */ {
  opacity: 0;
}
</style>
