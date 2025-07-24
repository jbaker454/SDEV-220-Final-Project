<!-- src/components -->
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

interface Shipment {
  id: number | string
  completed: boolean
  date: string
  quantity: number
  resource: Resource | null

  shipment_type: 'IN' | 'OUT' | 'Incoming' | 'Outgoing'
}

const shipments = ref<Shipment[]>([])
const error = ref<string | null>(null)

async function fetchShipments(): Promise<void> {
  try {
    const response = await fetch('http://localhost:8000/api/shipments/')
    if (!response.ok) throw new Error('Network response was not ok')
    const data: Shipment[] = await response.json()
    shipments.value = data
  } catch (err) {
    if (err instanceof Error) {
      error.value = err.message
    } else {
      error.value = String(err)
    }
  }
}

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
        {{ shipment.id }} - {{ shipment.resource?.name || 'Unknown Resource'}} - {{ shipment.completed }}
      </li>
    </ul>
    <div v-else>No shipments found.</div>
  </div>
</template>

<style scoped>
.process-componentframe { border: 1px solid #bbb; }
</style>