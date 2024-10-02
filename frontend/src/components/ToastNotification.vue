<template>
  <transition name="toast-fade">
    <div v-if="isVisible" class="fixed bottom-4 right-4 z-50">
      <div :class="[
        'px-4 py-2 rounded-md shadow-lg max-w-sm',
        `bg-${type}-500 text-white`
      ]">
        {{ message }}
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const props = defineProps({
  message: {
    type: String,
    required: true
  },
  duration: {
    type: Number,
    default: 3000
  },
  type: {
    type: String,
    default: 'info',
    validator: (value) => ['info', 'success', 'warning', 'error'].includes(value)
  }
});

const isVisible = ref(false);
let timer = null;

const show = () => {
  isVisible.value = true;
  timer = setTimeout(() => {
    isVisible.value = false;
  }, props.duration);
};

onMounted(() => {
  show();
});

onUnmounted(() => {
  if (timer) clearTimeout(timer);
});
</script>

<style scoped>
.toast-fade-enter-active,
.toast-fade-leave-active {
  transition: opacity 0.5s ease;
}

.toast-fade-enter-from,
.toast-fade-leave-to {
  opacity: 0;
}
</style>