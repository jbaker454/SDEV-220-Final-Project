<!-- src/pages -->

<script setup lang="ts">
  import Process_Component from '@/components/Process_Component.vue';
</script>

<template>
  <div>
    <h1>Processes Page</h1>
  </div>
  

  <div class="row">
    <div class = process-update-mainframe>
      <h2>update process</h2>
    </div>
    <Process_Component  class="panel" />
  </div>
</template>

<style>
  .row {
    display: flex;          
  }

  .process-update-mainframe {
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