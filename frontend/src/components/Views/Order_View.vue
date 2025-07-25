<!-- src/components/Views -->
<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface Location {
  id: number | string
  name: string
}

interface Resource {
  id: number | string
  name: string
  description: string
  quantity: number
  received_date: string
  location: Location | null
}

interface Order {
  id: number | string
  quantity: number
  date: string
  resource: Resource | null

  status: 'processing' | 'completed' | 'cancelled'
}

const orders = ref<Order[]>([])
const error = ref<string | null>(null)

async function fetchOrders(): Promise<void> {
  try {
    const response = await fetch('http://localhost:8000/api/orders/')
    if (!response.ok) throw new Error('Network response was not ok')
    const data: Order[] = await response.json()
    orders.value = data
  } catch (err) {
    if (err instanceof Error) {
      error.value = err.message
    } else {
      error.value = String(err)
    }
  }
}

onMounted(() => {
  fetchOrders()
})
</script>

<template>
  <div class="order-componentframe">
    <h1>Current Resources</h1>
    <div v-if="error" style="color:red">Error: {{ error }}</div>
    <ul v-if="orders.length">
      <li v-for="order in orders" :key="order.id">
        {{ order.id }} - {{ order.resource?.name || 'Unknown Resource'}} - {{ order.quantity }}
      </li>
    </ul>
    <div v-else>No orders found.</div>
  </div>
</template>

<style scoped>
.order-componentframe { border: 1px solid #bbb; }
</style>