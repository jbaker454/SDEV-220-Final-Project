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

interface Process {
  id: number | string
  name: string
  description: string
  items_per_second: number
  date: string
  resource: Resource | null

  status: 'pending' | 'done'
}

const processes = ref<Process[]>([])
const error = ref<string | null>(null)

async function fetchProcesses(): Promise<void> {
  try {
    const response = await fetch('http://localhost:8000/api/processes/')
    if (!response.ok) throw new Error('Network response was not ok')
    const data: Process[] = await response.json()
    processes.value = data
  } catch (err) {
    if (err instanceof Error) {
      error.value = err.message
    } else {
      error.value = String(err)
    }
  }
}

onMounted(() => {
  fetchProcesses()
})
</script>

<template>
  <div class="process-componentframe">
    <h1>Current processes</h1>
    <div v-if="error" style="color:red">Error: {{ error }}</div>
    <ul v-if="processes.length">
      <li v-for="process in processes" :key="process.id">
        {{ process.name }} - {{ process.resource?.name || 'Unknown Resource'}} - {{ process.status }}
      </li>
    </ul>
    <div v-else>No processes found.</div>
  </div>
</template>

<style scoped>
.process-componentframe { border: 1px solid #bbb; }
</style>