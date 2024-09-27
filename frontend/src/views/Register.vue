<template>
    <div class="flex min-h-screen bg-[#EDE8E5] relative overflow-hidden px-16">
        <!-- Login Form Section -->
        <div class="w-full lg:w-1/2 sm:w-full flex items-center lg:justify-normal justify-center relative z-10">
            <div class="w-full max-w-md bg-white rounded-lg shadow-md p-8">
                <h2 class="text-[20px] leading-[26.6px] text-center font-semibold font-sans text-[#212529] mb-2 ">
                    Welcome to British Asian Trust Portal
                </h2>
                <p class="text-[12px] text-center leading-[18.34px] font-normal text-[#212529] mb-6">
                    Sign up to empower your organization. Register today and gain access to surveys, personalized
                    recommendations, and tools to drive impact.
                </p>

                <!-- Stepper -->
                <div class="flex items-center justify-between mb-4">
                    <!-- Step 1 -->
                    <div class="flex gap-2 items-center">
                        <div
                            :class="['w-[24px] h-[24px] rounded-full flex items-center justify-center text-[14px] text-center leading-[18.34px] font-normal', currentStep >= 1 ? 'bg-green-500 text-white' : 'bg-yellow-500 text-white']">
                            1
                        </div>
                        <p
                            :class="['text-[12px]  leading-[18.34px]', currentStep >= 1 ? 'text-black' : 'text-gray-500']">
                            Organization</p>
                    </div>

                    <!-- Process line -->
                    <div :class="['flex-1 h-[2px] mx-2', currentStep >= 2 ? 'bg-green-500' : 'bg-gray-300']"></div>

                    <!-- Step 2 -->
                    <div class="flex gap-2 items-center">
                        <div
                            :class="['w-[24px] h-[24px] rounded-full flex items-center justify-center text-[14px] text-center leading-[18.34px] font-normal', currentStep >= 2 ? 'bg-green-500 text-white' : 'bg-gray-300 text-gray-500']">
                            2
                        </div>
                        <p
                            :class="[' text-[12px] text-center leading-[18.34px]', currentStep >= 2 ? 'text-black' : 'text-gray-500']">
                            Admin</p>
                    </div>
                </div>

                <!-- Form -->
                <form @submit.prevent="nextStep" class="space-y-4">
                    <!-- Step 1: Organization Details -->
                    <div class="flex flex-col gap-4" v-if="currentStep === 1">
                        <div>
                            <label for="pan" class="block text-[14px] leading-[18.34px] font-sans mb-1">Organization PAN
                                Number</label>
                            <input type="text" id="pan" name="pan" v-model="pan"
                                class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                                placeholder="Enter PAN number">
                        </div>
                        <div>
                            <label for="organization"
                                class="block text-[14px] leading-[18.34px] font-sans mb-1">Organization</label>
                            <input type="text" id="organization" name="organization" v-model="organization"
                                class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                                placeholder="Enter your organization name">
                        </div>
                        <div>
                            <label for="address"
                                class="block text-[14px] leading-[18.34px] font-sans mb-1">Address</label>
                            <input type="text" id="address" name="address" v-model="address"
                                class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                                placeholder="Enter your address">
                        </div>
                    </div>

                    <!-- Step 2: Admin Details -->
                    <div class="flex flex-col gap-4" v-if="currentStep === 2">

                        <div>
                            <label for="full-name" class="block text-[14px]  leading-[18.34px] font-sans mb-1">Full
                                Name</label>
                            <input type="text" id="full-name" name="full-name" v-model="fullName"
                                class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                                placeholder="Enter your full name">
                        </div>
                        <div>
                            <label for="email" class="block text-[14px]  leading-[18.34px] font-sans mb-1">Email
                                Address</label>
                            <input type="email" id="email" name="email" v-model="email"
                                class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                                placeholder="Enter your email address">
                        </div>
                        <div>
                            <label for="phone" class="block text-[14px]  leading-[18.34px] font-sans mb-1">Phone Number
                                (optional)</label>
                            <div class="flex rounded-md shadow-sm">
                                <span
                                    class="inline-flex items-center px-3 rounded-l-md border border-gray-300 text-gray-500 text-sm">
                                    +91
                                </span>
                                <input type="tel" id="phone" name="phone" v-model="phone"
                                    class="flex-1 min-w-0 block w-full px-3 py-2 rounded-none rounded-r-md focus:ring-red-500 focus:border-red-500 border border-gray-300 sm:text-sm"
                                    placeholder="Enter your phone number">
                            </div>
                        </div>

                        <div>
                            <label for="role" class="block text-[14px]  leading-[18.34px] font-sans mb-1">Role in
                                Organization</label>
                            <input type="text" id="role" name="role" v-model="role"
                                class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
                                placeholder="Enter your designation">
                        </div>
                        <div class="flex items-center">
                            <input id="terms" name="terms" type="checkbox" v-model="termsAccepted"
                                class="h-4 w-4 text-red-600 focus:ring-red-500 border-gray-300 rounded">
                            <label for="terms" class="ml-2 block text-sm text-gray-900">
                                I agree with <a href="#" class="text-red-600 hover:text-red-500">terms & conditions</a>
                            </label>
                        </div>


                    </div>

                    <!-- Next/Submit button -->
                    <div class="flex flex-col justify-center items-center gap-2">
                        <button type="submit"
                            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#CA2247] hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                            {{ currentStep === 1 ? 'Fill admin information' : 'Submit' }}
                        </button>
                        <!-- "Go Back" button (only visible in step 2) -->
                        <div v-if="currentStep === 2" type="button" @click="goBack"
                            class="cursor-pointer text-[14px] leading-[18.34px] font-sans">
                            Go Back
                        </div>
                    </div>

                </form>

            </div>
        </div>

        <!-- SVG and Image Section -->
        <div class="hidden lg:block lg:w-1/2 relative ">
            <svg class="absolute right-0 bottom-0 w-[400px] h-[400px] lg:w-[700px] lg:h-[700px]" viewBox="0 0 719 681"
                fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M10.6721 358.09C43.7944 290.528 148.486 299.88 203.921 248.991C237.118 218.516 233.243 164.646 260.492 128.755C298.361 78.8762 330.329 2.09349 392.93 0.0381908C454.772 -1.99227 485.461 77.4593 530.486 119.891C565.441 152.832 598.797 184.384 628.553 222.085C662.81 265.488 725.275 303.219 718.489 358.09C711.449 415.017 625.945 426.357 597.155 475.972C568.46 525.423 606.218 613.235 555.318 639.29C503.188 665.974 451.086 573.596 392.93 580.511C321.677 588.984 278.12 686.509 206.596 680.755C139.575 675.363 89.6252 610.766 54.7335 553.303C19.5091 495.292 -19.2021 419.028 10.6721 358.09Z"
                    fill="#DBB729" />
            </svg>
            <img src="../assets/register1.png" alt="Two women in traditional attire"
                class="absolute inset-0 w-full h-full object-cover">
        </div>

    </div>
</template>

<script>
export default {
    data() {
        return {
            pan: null,
            organization: null,
            address: null,
            currentStep: 1,
            fullName: null,
            email: null,
            phone: null,
            role: null,
            termsAccepted: false



        };
    },
    methods: {
        nextStep() {
            if (this.currentStep === 1 && this.pan && this.organization && this.address) {
                // Move to the next step only if all the fields in step 1 are filled
                this.currentStep = 2;
            } else if (this.currentStep === 2) {
                // Submit form or handle final step
                console.log("Admin details submitted");
            }
        },
        goBack() {
            // Set step back to 1
            this.currentStep = 1;
        }
    }
}
</script>
