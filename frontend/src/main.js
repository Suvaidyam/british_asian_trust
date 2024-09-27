import { createApp, reactive } from "vue";
import App from "./App.vue";
import './style.css'

import router from './router';
import resourceManager from "./doppio/resourceManager";
import call from "./doppio/controllers/call";
import socket from "./doppio/controllers/socket";
import Auth from "./doppio/controllers/auth";

const app = createApp(App);
const auth = reactive(new Auth());

// Plugins
app.use(router);
app.use(resourceManager);

// Global Properties,
// components can inject this
app.provide("$auth", auth);
app.provide("$call", call);
app.provide("$socket", socket);


// Configure route gaurds
router.beforeEach(async (to, from, next) => {
	if (to.matched.some((record) => !record.meta.isLoginPage)) {
		if (!auth.isLoggedIn) {
			if(to.name !== 'Register') {
				next({ name: 'Login', query: { route: to.path } });
			}else{
				next();
			}
		} else {
			next();
		}
	} else {
		if (auth.isLoggedIn) {
			next({ name: 'Home' });
		} else {
			next();
		}
	}
});

app.mount("#app");
