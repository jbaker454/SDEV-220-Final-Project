<!-- src/components/Views -->
<script setup lang="ts">
import { onMounted } from 'vue'

import { useInterface } from '@/api/useInterface'

const { processes, error, fetchProcesses} = useInterface()

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
        {{ process.str_representation }}
      </li>
    </ul>
    <div v-else>No processes found.</div>
  </div>
</template>

<style scoped>
.process-componentframe { border: 1px solid #bbb; }
</style>