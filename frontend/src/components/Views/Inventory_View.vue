<!-- src/components/Views -->
<script setup lang="ts">
import { onMounted } from 'vue'

import { useInterface } from '@/api/useInterface'

const { resources, error, fetchResources} = useInterface()

onMounted(() => {
  fetchResources()
})
</script>

<template>
  <div class="inventory-componentframe">
    <h1>Current Resources</h1>
    <div v-if="error" style="color:red">Error: {{ error }}</div>
    <ul v-if="resources.length">
      <li v-for="resource in resources" :key="resource.id">
        {{ resource.str_representation }}
      </li>
    </ul>
    <div v-else>No resources found.</div>
  </div>
</template>

<style scoped>
.inventory-componentframe { border: 1px solid #bbb; }
</style>