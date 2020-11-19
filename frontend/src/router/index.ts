import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home.vue'
import Classification from '@/views/Classification.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Classification',
    name: 'Classification',
    component: Classification
  },
]

const router = new VueRouter({
  routes
})

export default router
