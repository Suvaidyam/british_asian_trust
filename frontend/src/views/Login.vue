<template>
	<div class="flex min-h-screen bg-[#EDE8E5] relative overflow-hidden px-16">

		<!-- Login Form Section -->
		<div class="w-full lg:w-1/2 sm:w-full flex items-center lg:justify-normal  justify-center  relative z-10">
			<div class="w-full max-w-md bg-white rounded-lg shadow-md p-8">
				<h2 class="text-[20px] leading-[26.6px] text-center font-semibold font-sans text-[#212529] mb-2 ">
					Welcome to British Asian Trust Portal
				</h2>
				<p class="text-[12px] text-center leading-[18.34px] font-normal text-[#212529] mb-6">
					Login to access your dashboard, complete surveys, earn points, and get personalized recommendations
					to support your wellness.
				</p>
				<form @submit.prevent="login" class="space-y-4">
					<div>
						<label for="email" class="block  text-[14px]  leading-[18.34px] font-sans mb-1">Email</label>
						<input type="text" id="email" name="email" v-model="email"
							class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
							placeholder="Enter your email address">
					</div>
					<div>
						<label for="password" class="block text-[14px]  leading-[18.34px] font-sans mb-1">Password</label>
						<input type="password" id="password" name="password" v-model="password"
							class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm"
							placeholder="Enter your password">
					</div>
					<div>
						<button type="submit"
							class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#CA2247] hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
							LOGIN
						</button>
					</div>
				</form>
				<div class="mt-4 text-center">
					<a href="#" class="text-sm text-gray-600 hover:text-gray-900">Forgot Password?</a>
				</div>
			</div>
		</div>

		<div class="hidden lg:block lg:w-1/2 relative ">
			<!-- Image of Two Women -->

			<!-- SVG Element positioned absolutely over the image -->
			<svg class="absolute right-0 bottom-0 w-[300px] h-[300px] lg:w-[700px] lg:h-[700px]" viewBox="0 0 719 681"
				fill="none" xmlns="http://www.w3.org/2000/svg">
				<path fill-rule="evenodd" clip-rule="evenodd"
					d="M10.6721 358.09C43.7944 290.528 148.486 299.88 203.921 248.991C237.118 218.516 233.243 164.646 260.492 128.755C298.361 78.8762 330.329 2.09349 392.93 0.0381908C454.772 -1.99227 485.461 77.4593 530.486 119.891C565.441 152.832 598.797 184.384 628.553 222.085C662.81 265.488 725.275 303.219 718.489 358.09C711.449 415.017 625.945 426.357 597.155 475.972C568.46 525.423 606.218 613.235 555.318 639.29C503.188 665.974 451.086 573.596 392.93 580.511C321.677 588.984 278.12 686.509 206.596 680.755C139.575 675.363 89.6252 610.766 54.7335 553.303C19.5091 495.292 -19.2021 419.028 10.6721 358.09Z"
					fill="#DBB729" />
			</svg>
			<img src="../assets/login_banner.png" alt="Two women in traditional attire"
				class="absolute inset-0 w-full h-full object-cover">
		</div>

	</div>
</template>

<script>
export default {
	data() {
		return {
			email: null,
			password: null,
		};
	},
	inject: ["$auth"],
	async mounted() {
		if (this.$route?.query?.route) {
			this.redirect_route = this.$route.query.route;
			this.$router.replace({ query: null });
		}
	},
	methods: {
		async login() {
			if (this.email && this.password) {
				let res = await this.$auth.login(this.email, this.password);
				if (res) {
					this.$router.push({ name: "Home" });
				}
			}
		},
	},
};
</script>