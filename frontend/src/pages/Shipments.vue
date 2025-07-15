<!-- src/pages -->

<script setup lang="ts">
  import Shipment_Component from '@/components/Shipment_Component.vue';
</script>

<template>
  <div>
    <h1>Shipments Page</h1>
  </div>
  

  <div class="row">
    <div class = shipment-update-mainframe>
      <h2>update shipment</h2>
    </div>
    <Shipment_Component class="panel" />
  </div>
</template>

<style>
  .row {
    display: flex;          
  }

  .shipment-update-mainframe {
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