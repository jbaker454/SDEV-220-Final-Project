// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home_Page.vue'
import Inventory from '@/pages/Inventory_Page.vue'
import Shipments from '@/pages/Shipments_Page.vue'
import Processes from '@/pages/Processes_Page.vue'
import Orders from '@/pages/Orders_Page.vue'

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