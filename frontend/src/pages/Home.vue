<!-- src/pages -->
<script setup lang="ts">
  import Component_Display from '@/components/Component_Display.vue';
</script>

<template>
  <div class="page-name">
    <h1>Home Page</h1>
  </div>
  <div class="row">
    <Component_Display class="panel"/>
    <Component_Display class="panel"/>
    <Component_Display class="panel"/>
  </div>
</template>

<script setup lang="ts">

</script>

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