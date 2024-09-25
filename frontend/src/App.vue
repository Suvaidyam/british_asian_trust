<template>
	<div>
		<NavBar />
		<button v-if="$auth.isLoggedIn" @click="$auth.logout()">Logout</button>
		<router-view />
	</div>
</template>


<script>
import NavBar from './components/NavBar.vue';
export default {
	components: {
		NavBar,
	},
	inject: ['$auth']
};
</script>
