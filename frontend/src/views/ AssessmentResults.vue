<template>
    <div class="min-h-screen bg-gray-50 ">
        <NavBar />
        <main class="relative max-w-[1920px] mx-auto px-4 sm:px-6 md:px-8 lg:px-12 pb-8 overflow-hidden">
            <!-- Breadcrumb -->
            <nav class="py-2">
                <div class="flex items-center gap-1 text-sm text-gray-600">
                    <router-link to="/" class="hover:text-[#0D4688]">Home</router-link>
                    <span>/</span>
                    <span>Assessment</span>
                </div>
            </nav>

            <!-- Header -->
            <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between mb-8">
                <h1
                    class="font-poppins text-[#0D4688] text-2xl sm:text-3xl md:text-[34px] lg:text-[34px] font-semibold leading-tight sm:leading-[37.4px] lg:leading-[37.4px] tracking-[0.0025em] mb-4 lg:mb-0">
                    Assessment Sample Test
                </h1>
                <div
                    class="bg-gradient-to-r from-[#0D4688] to-[#406EA3] bg-[length:200%] bg-[99.63deg] w-full sm:w-[376px] md:w-[350px] lg:w-[400px] h-auto sm:h-[114px] rounded-lg p-6 text-white">
                    <h2
                        class="font-poppins text-lg sm:text-xl md:text-[20px] lg:text-[20px] font-semibold leading-tight sm:leading-[22px] lg:leading-[22px] tracking-[0.0015em] text-left mb-4">
                        Check you score here
                    </h2>
                    <button @click="showReportCard = true"
                        class="w-full sm:w-[280px] md:w-[280px] lg:w-[280px] h-[36px] font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-semibold leading-[15.4px] tracking-[0.0125em] text-center bg-orange-500 hover:bg-orange-600 text-white py-2 px-4 rounded-full transition-colors duration-300">
                        DOWNLOAD REPORT CARD
                    </button>
                </div>
            </div>

            <!-- Main Content -->
            <div class="bg-white rounded-lg shadow-sm p-8">
                <div class="flex items-center gap-2 mb-6">
                    <h2 class="font-poppins text-2xl font-bold">Congratulations, Help India!</h2>
                    <span class="text-2xl">🏅</span>
                </div>

                <p
                    class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529] mb-6">
                    You have successfully completed the Outcome Readiness Survey. This survey evaluates key aspects of
                    your organisation's and program's preparedness to manage and execute outcome-based projects. Below
                    is a summary of your current readiness.
                </p>

                <p
                    class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529] mb-8">
                    This assessment is designed to help you identify both strengths and areas for improvement as you
                    work toward achieving greater effectiveness and efficiency in outcome-driven initiatives.
                </p>

                <h3 class="font-poppins text-xl font-bold mb-6">Readiness Overview</h3>

                <div class="grid md:grid-cols-2 gap-6 mb-8">
                    <!-- Organization Level Card -->
                    <div class="border border-green-100 bg-green-50 rounded-lg p-6">
                        <h4 class="font-poppins text-lg font-semibold mb-4">Organization Level Readiness</h4>
                        <div class="flex justify-center">
                            <span class="font-poppins text-4xl font-bold text-green-600">High</span>
                        </div>
                    </div>

                    <!-- Program Level Card -->
                    <div class="border border-yellow-100 bg-yellow-50 rounded-lg p-6">
                        <h4 class="font-poppins text-lg font-semibold mb-4">Program Level Readiness</h4>
                        <div class="flex justify-center">
                            <span class="font-poppins text-4xl font-bold text-yellow-500">Medium</span>
                        </div>
                    </div>
                </div>

                <div class="space-y-4">
                    <p
                        class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529]">
                        <strong>Download your detailed report</strong> for more in-depth analysis and curated resources
                        tailored to help your organization improve in specific areas. Please note that this report card
                        is based on your latest survey responses and does not reflect your older performance (in case
                        you have taken this assessment before). Your older report card would have been sent to you in an
                        email on the day you completed the older assessment.
                    </p>

                    <h4 class="font-poppins font-bold">A few things to note:</h4>
                    <ul class="list-disc pl-5 space-y-2">
                        <li
                            class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529]">
                            This report card is a learning and development tool designed to support you in building the
                            essential capabilities and skills required to participate in outcome-based financing
                            projects and fostering an outcomes-oriented mindset within your organization and programs.
                            The ratings are based on your responses and level of understanding, honesty and diligence
                            exercised while answering the questions. This is meant to be a quicklook assessment that
                            indicates your broad direction and is not meant to be a summative validation or exhaustive
                            audit of all your capabilities.
                        </li>
                        <li
                            class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529]">
                            This report card is not a certification for participation in outcome-based financing
                            projects and actual participation may be influenced by external factors beyond this tool's
                            scope.
                        </li>
                        <li
                            class="font-poppins text-sm sm:text-base md:text-[14px] lg:text-[14px] font-normal leading-relaxed sm:leading-[19.6px] lg:leading-[19.6px] tracking-[0.0025em] text-justify text-[#212529]">
                            The curated list of resources has been carefully reviewed to ensure they are relevant to the
                            Indian context and non-profits working in the country, guiding you on the pathway to
                            strengthening your outcomes readiness. Given that they are open-sourced and not customized,
                            you should be the judge of how you want to use them.
                        </li>
                    </ul>
                </div>
            </div>
        </main>

        <!-- Report Card Popup -->
        <ReportCardPopup v-if="showReportCard" :organization-name="'Help India'" :sector="'Health'"
            :completion-date="'September 22, 2024'" :organization-readiness="'High'" :program-readiness="'Medium'"
            :readiness-data="readinessData" @close="showReportCard = false" />

        <!-- Feedback Popup -->
        <AssessmentFeedback v-if="showFeedback" @close="showFeedback = false" @submit="handleFeedbackSubmit" />
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ReportCardPopup from '../components/ReportCardPopup.vue'
import AssessmentFeedback from '../components/AssessmentFeedback.vue'
import NavBar from '../components/NavBar.vue';

const showReportCard = ref(false)
const showFeedback = ref(true)

const readinessData = ref([
    {
        section: 'Clarity and Coherence about',
        level: 'Low',
        details: 'Lorem ipsum dolor sit ametigh',
        resources: 'We have put together a few se.'
    },
    {
        section: 'Board Management',
        level: 'Medium',
        details: 'Lorem ipsum dolor sit ametigh',
        resources: 'We have put together a few se.'
    },
    {
        section: 'Leadership and decision maki',
        level: 'Medium',
        details: 'Lorem ipsum dolor sit ametigh',
        resources: 'We have put together a few se.'
    }
])

const handleFeedbackSubmit = (feedback) => {
    console.log('Feedback submitted:', feedback)
    showFeedback.value = false
}

onMounted(() => {
    showFeedback.value = true
})
</script>

<style scoped>
/* Add any component-specific styles here */
</style>