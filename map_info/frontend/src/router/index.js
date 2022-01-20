import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Maps from "../views/Maps"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/maps",
    name: "maps",
    component: Maps,
    props: true
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
