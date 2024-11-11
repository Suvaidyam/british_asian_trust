<template>
  <div class="relative min-h-screen  font-poppins">
    <NavBar />
    <div class="absolute bg-effect w-3/4 h-3/4">
      <img src="/effect.png" alt="Background effect">
    </div>
    <div class="max-w-[1920px] mx-auto ">
      
        <FormView :doctype="'Assessment'"></FormView>
      
    </div>
  </div>
</template>

<script setup>

import NavBar from '../components/NavBar.vue'
import FormView from '../components/sva_form_ui/FormView.vue';


</script>

<style scoped>
@media (max-width: 640px) {
  .overflow-x-auto {
    -webkit-overflow-scrolling: touch;
  }
}
</style>