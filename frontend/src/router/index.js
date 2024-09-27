import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register.vue";
import Assessment from "../components/Assessment.vue";
import Myuser from "../components/MyUser.vue";
import authRoutes from './auth';

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },

  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  ...authRoutes,

  {
    path: "/assessment",
    name: "Assessment",
    component: Assessment,
  },

  {

    path: "/myuser",
    name: "Myuser",
    component: Myuser,
  },
];

const router = createRouter({
  base: "/frontend/",
  history: createWebHistory(),
  routes,
});

export default router;
