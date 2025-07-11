<!-- src/pages/Home.vue -->

<script setup lang="ts">
  //import Resource_Component from '@/components/Resource_Component.vue';
  import Shipment_Component from '@/components/Shipment_Component.vue';
  import Process_Component from '@/components/Process_Component.vue';
  import Order_Component from '@/components/Order_Component.vue';
</script>

<template>
  <div>
    <h1>Inventory Page</h1>
  </div>
  

  <div class="row">
    <Shipment_Component class="panel" />
    <Process_Component  class="panel" />
    <Order_Component    class="panel" />
  </div>
</template>

<style>
    .row {
      display: flex;
    }

    .panel {
      flex: 1;
      border: 2px solid #555;
      box-sizing: border-box;
      padding: 1rem;
    }
  </style>