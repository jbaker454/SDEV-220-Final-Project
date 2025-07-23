<!-- src/pages -->

<script setup lang="ts">
  import Inventory_Component from '@/components/Views/Inventory_View.vue';
</script>

<template>
  <div>
    <h1>Inventory Page</h1>
  </div>
  

  <div class="row">
    <div class = inventory-update-mainframe>
      <h2>update inventory</h2>
    </div>
    <Inventory_Component class="panel" />
  </div>
</template>

<style>
  .row {
    display: flex;          
  }

  .inventory-update-mainframe {
    flex: 2 1 0;
    border: 2px solid #555; 
    box-sizing: border-box;
    padding: 1rem; 
  }
  .panel {
    flex: 1 1 0;                
    border: 2px solid #555; 
    box-sizing: border-box; 
    padding: 1rem;
  }
</style>