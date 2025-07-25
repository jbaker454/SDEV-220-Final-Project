<!-- src/pages -->

<script setup lang="ts">
  import Inventory_View_Component from '@/components/Views/Inventory_View.vue';
  import Inventory_Modify_Component from '@/components/Modifies/Inventory_Modify.vue';
</script>

<template>
  <div>
    <h1>Inventory Page</h1>
  </div>
  

  <div class="row">
    <Inventory_Modify_Component class="inventory-update-mainframe" />
    <Inventory_View_Component class="panel" />
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