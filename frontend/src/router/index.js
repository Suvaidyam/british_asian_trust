import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register.vue";
import Forgot from "../components/ForgotPassword.vue";
import authRoutes from './auth';
import Landing from "../views/Landing.vue";
import AssessmentTest from "../views/AssessmentTest.vue";
import DashBoard from "../views/DashBoard.vue";
import UpdatePassword from "../components/ UpdatePassword.vue";
import AssessmentResults from "../views/ AssessmentResults.vue";

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
    path: "/updatepassword",
    name: "UpdatePassword",
    component: UpdatePassword,
  },
  {
    path: "/forgot",
    name: "Forgot",
    component: Forgot,
  },
  ...authRoutes,
  {
    path: "/dashboard",
    name: "DashBoard",
    component: DashBoard,
  },

  {
    path: "/assessment",
    name: "AssessmentTest",
    component: AssessmentTest,
  },
  {
    path: "/assessmentresults",
    name: "AssessmentResults",
    component: AssessmentResults,
  },
];

const router = createRouter({
  base: "/bat",
  history: createWebHistory('/bat'),
  routes,
});

export default router;
