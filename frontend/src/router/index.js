import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register.vue";
import Assessment from "../components/Assessment.vue";
import Myuser from "../components/MyUser.vue";
import Forget from "../components/ForgetPassword.vue";
import authRoutes from './auth';
import Landing from "../components/Landing.vue";

const routes = [
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
{
  path: "/",
  name: "Landing",
  component: Landing,
},
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/forgot",
    name: "Forgot",
    component: Forget,
  },
  ...authRoutes,

  {
    path: "/assessment",
    name: "Assessment",
    component: Assessment,
  },

  {

    path: "/myuser",
    name: "MyUser",
    component: Myuser,
  },
];

const router = createRouter({
  base: "/bat",
  history: createWebHistory('/bat'),
  routes,
});

export default router;
