<template>
    <div class="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-lg w-full max-w-4xl max-h-[90vh] overflow-y-auto">
        <!-- Header -->
        <div class="flex items-center justify-between p-4 border-b sticky top-0 bg-white">
          <h2 class="font-poppins text-xl font-semibold">Outcome Readiness Report Card</h2>
          <div class="flex items-center gap-2">
            <button class="p-2 text-green-600 hover:bg-green-50 rounded-full">
              <DownloadIcon class="w-5 h-5" />
            </button>
            <button @click="$emit('close')" class="p-2 hover:bg-gray-100 rounded-full">
              <XIcon class="w-5 h-5" />
            </button>
          </div>
        </div>
  
        <!-- Content -->
        <div class="p-6 space-y-6">
          <!-- Organization Details -->
          <div class="space-y-4">
            <div class="flex gap-x-8">
              <span class="font-poppins text-gray-600">Organisation :</span>
              <span class="font-poppins">{{ organizationName }}</span>
            </div>
            <div class="flex gap-x-8">
              <span class="font-poppins text-gray-600">Sector :</span>
              <span class="font-poppins">{{ sector }}</span>
            </div>
            <div class="flex gap-x-8">
              <span class="font-poppins text-gray-600">Date Completed :</span>
              <span class="font-poppins">{{ completionDate }}</span>
            </div>
          </div>
  
          <!-- Readiness Overview -->
          <div>
            <h3 class="font-poppins text-lg font-semibold mb-4">Readiness Overview</h3>
            <div class="grid md:grid-cols-2 gap-4">
              <!-- Organization Level -->
              <div class="border border-green-100 bg-green-50 rounded-lg p-6">
                <h4 class="font-poppins text-base font-medium mb-4">Organization Level Readiness</h4>
                <div class="flex justify-center">
                  <span class="font-poppins text-4xl font-bold text-green-600">{{ organizationReadiness }}</span>
                </div>
              </div>
              
              <!-- Program Level -->
              <div class="border border-yellow-100 bg-yellow-50 rounded-lg p-6">
                <h4 class="font-poppins text-base font-medium mb-4">Program Level Readiness</h4>
                <div class="flex justify-center">
                  <span class="font-poppins text-4xl font-bold text-yellow-500">{{ programReadiness }}</span>
                </div>
              </div>
            </div>
          </div>
  
          <!-- Notes -->
          <div>
            <h4 class="font-poppins text-base font-medium mb-2">A few things to note:</h4>
            <ul class="space-y-2 text-sm font-poppins">
              <li>This report card is a learning and development tool designed to support you in building the essential capabilities and skills required to participate in outcome-based financing projects and fostering an outcomes-oriented mindset within your organization and programs. The ratings are based on your responses and level of understanding, honesty and diligence exercised while answering the questions. This is meant to be a dipstick assessment that indicates your broad direction and is not meant to be a summative validation or exhaustive audit of all your capabilities.</li>
              <li>This report card is not a certification for participation in outcome-based financing projects and actual participation may be influenced by external factors beyond this tool's scope.</li>
              <li>The curated list of resources has been carefully reviewed to ensure they are relevant to the Indian context and non-profits working in the country, guiding you on the pathway to strengthening your outcomes readiness. Given that they are open-sourced and not customized, you should be the judge of how you want to use them.</li>
            </ul>
          </div>
  
          <!-- Readiness Table -->
          <div>
            <h3 class="font-poppins text-lg font-semibold mb-4">Organization Level Readiness</h3>
            <div class="overflow-x-auto">
              <table class="w-full border-collapse">
                <thead>
                  <tr class="bg-gray-50">
                    <th class="font-poppins text-left p-4 border">Section</th>
                    <th class="font-poppins text-left p-4 border">Level of readiness</th>
                    <th class="font-poppins text-left p-4 border">Useful resources</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in readinessData" :key="index">
                    <td class="font-poppins p-4 border">{{ item.section }}</td>
                    <td class="font-poppins p-4 border">
                      <div class="flex items-center gap-2">
                        <span :class="{
                          'text-green-600': item.level === 'High',
                          'text-yellow-500': item.level === 'Medium',
                          'text-red-500': item.level === 'Low'
                        }">{{ item.level }}</span>
                        <span class="text-gray-500">{{ item.details }}</span>
                      </div>
                    </td>
                    <td class="font-poppins p-4 border">{{ item.resources }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { XIcon, DownloadIcon } from 'lucide-vue-next'
  
  defineProps({
    organizationName: {
      type: String,
      required: true
    },
    sector: {
      type: String,
      required: true
    },
    completionDate: {
      type: String,
      required: true
    },
    organizationReadiness: {
      type: String,
      required: true
    },
    programReadiness: {
      type: String,
      required: true
    },
    readinessData: {
      type: Array,
      required: true
    }
  })
  
  defineEmits(['close'])
  </script>
  
  <style scoped>
  /* Add any component-specific styles here */
  </style>