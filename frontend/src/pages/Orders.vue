<!-- src/pages -->

<script setup lang="ts">
  import Order_Component from '@/components/Order_Component.vue';
</script>

<template>
  <div>
    <h1>Orders Page</h1>
  </div>
  

  <div class="row">
    <div class = order-update-mainframe>
      <h2>update order</h2>
    </div>
    <Order_Component    class="panel" />
  </div>
</template>

<style>
  .row {
    display: flex;          
  }

  .order-update-mainframe {
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