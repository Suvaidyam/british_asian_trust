import { createApp, reactive } from "vue";
import App from "./App.vue";
import './style.css'

import router from './router';
import resourceManager from "./doppio/resourceManager";
import call from "./doppio/controllers/call";
import socket from "./doppio/controllers/socket";
import Auth from "./doppio/controllers/auth";
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

const app = createApp(App);
const auth = reactive(new Auth());

// Plugins
app.use(router);
app.use(Toast)
app.use(resourceManager);

// Global Properties,
// components can inject this
app.provide("$auth", auth);
app.provide("$call", call);
app.provide("$socket", socket);


router.beforeEach(async (to, from, next) => {
    if (!auth.isLoggedIn) {
        // Redirect to Landing page if the user is not logged in and tries to access a protected page
        if (!['Register', 'Forgot', 'Login', 'Landing'].includes(to.name)) {
            next({ name: 'Landing', query: { route: to.path } });
        } else {
            next();
        }
    } else {
        // If logged in, restrict access to authentication pages and redirect to Home
        if (['Register', 'Forgot', 'Login'].includes(to.name)) {
            next({ name: 'Home' });
        } else {
            next();
        }
    }
});


app.mount("#app");
