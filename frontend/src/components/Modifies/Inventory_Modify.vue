<!-- src/components/Modifies -->
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
  location: string | null
}

const resources = ref<Resource[]>([])
const error = ref<string | null>(null)

async function fetchResources(): Promise<void> {
  try {
    const response = await fetch('http://localhost:8000/api/resources/')
    if (!response.ok) throw new Error('Network response was not ok')
    const data: Resource[] = await response.json()
    resources.value = data
  } catch (err) {
    if (err instanceof Error) {
      error.value = err.message
    } else {
      error.value = String(err)
    }
  }
}

onMounted(() => {
  fetchResources()
})
</script>

<template>
  <div class="inventory-componentframe">
    <h1>edit resource</h1>
    <button class="add">Add</button>
    <div>
      
    </div>
  </div>
</template>

<style scoped>
.inventory-componentframe { border: 1px solid #bbb; }
</style>