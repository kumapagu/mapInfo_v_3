import Vue from "vue"
import VueRouter from "vue-router"
import Maps from "../views/Maps"
import InfoEditor from "../views/InfoEditor"
import Park from "../views/Park"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "maps",
    component: Maps,
    props: true
  },
  {
    path: "/info", 
    name: "info",
    component: InfoEditor,
    props: true
  },
  {
    path: "/park/:id", 
    name: "park",
    component: Park,
    props: true,
  },
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router
