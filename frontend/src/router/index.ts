// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home.vue'
import Inventory from '@/pages/Inventory.vue'
import Shipments from '@/pages/Shipments.vue'
import Processes from '@/pages/Processes.vue'
import Orders from '@/pages/Orders.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/Inventory', component: Inventory },
  { path: '/Shipments', component: Shipments },
  { path: '/Processes', component: Processes },
  { path: '/Orders', component: Orders },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router