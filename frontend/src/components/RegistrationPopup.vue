<template>
    <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg p-8 max-w-md w-full">
        <h2 class="text-2xl font-bold mb-4">Complete Your Registration</h2>
        <form @submit.prevent="submitRegistration">
          <div class="mb-4">
            <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
            <input 
              v-model="form.name" 
              id="name" 
              type="text" 
              required 
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-[#CA2247] focus:ring focus:ring-[#CA2247] focus:ring-opacity-50"
              :class="{ 'border-red-500': errors.name }"
            >
            <p v-if="errors.name" class="mt-1 text-sm text-red-600">{{ errors.name }}</p>
          </div>
          <div class="mb-4">
            <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
            <input 
              v-model="form.email" 
              id="email" 
              type="email" 
              required 
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-[#CA2247] focus:ring focus:ring-[#CA2247] focus:ring-opacity-50"
              :class="{ 'border-red-500': errors.email }"
            >
            <p v-if="errors.email" class="mt-1 text-sm text-red-600">{{ errors.email }}</p>
          </div>
          <button 
            type="submit" 
            class="w-full bg-[#CA2247] text-white font-bold py-2 px-4 rounded hover:bg-red-700 transition duration-300 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed"
            :disabled="isSubmitting"
          >
            {{ isSubmitting ? 'Registering...' : 'Complete Registration' }}
          </button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, reactive } from 'vue';
  
  const emit = defineEmits(['registration-complete']);
  
  const form = reactive({
    name: '',
    email: '',
  });
  
  const errors = reactive({
    name: '',
    email: '',
  });
  
  const isSubmitting = ref(false);
  
  const validateForm = () => {
    let isValid = true;
    errors.name = '';
    errors.email = '';
  
    if (!form.name.trim()) {
      errors.name = 'Name is required';
      isValid = false;
    }
  
    if (!form.email.trim()) {
      errors.email = 'Email is required';
      isValid = false;
    } else if (!/\S+@\S+\.\S+/.test(form.email)) {
      errors.email = 'Email is invalid';
      isValid = false;
    }
  
    return isValid;
  };
  
  const submitRegistration = async () => {
    if (!validateForm()) return;
  
    isSubmitting.value = true;
  
    try {
      // Here you would typically send the form data to your backend
      // For this example, we'll just simulate an API call
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Emit an event to notify the parent component that registration is complete
      emit('registration-complete', { name: form.name, email: form.email });
    } catch (error) {
      console.error('Registration failed:', error);
      // Handle error (e.g., show error message to user)
    } finally {
      isSubmitting.value = false;
    }
  };
  </script>
  
  <style scoped>
  input:focus {
    outline: none;
    border-color: #CA2247;
    box-shadow: 0 0 0 1px #CA2247;
  }
  </style>