<!-- src/components/Views -->
<script setup lang="ts">
import { onMounted } from 'vue'

import { useInterface } from '@/api/useInterface'

const { orders, error, fetchOrders} = useInterface()

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
        {{ order.str_representation }}
      </li>
    </ul>
    <div v-else>No orders found.</div>
  </div>
</template>

<style scoped>
.order-componentframe { border: 1px solid #bbb; }
</style>