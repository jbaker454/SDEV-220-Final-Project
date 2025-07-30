<!-- src/components/Views -->
<script setup lang="ts">
import { onMounted } from 'vue'

import { useInterface } from '@/api/useInterface'

const { shipments, error, fetchShipments} = useInterface()

onMounted(() => {
  fetchShipments()
})
</script>

<template>
  <div class="process-componentframe">
    <h1>Current shipments</h1>
    <div v-if="error" style="color:red">Error: {{ error }}</div>
    <ul v-if="shipments.length">
      <li v-for="shipment in shipments" :key="shipment.id">
        {{ shipment.str_representation }}
      </li>
    </ul>
    <div v-else>No shipments found.</div>
  </div>
</template>

<style scoped>
.process-componentframe { border: 1px solid #bbb; }
</style>