<!-- src/pages -->

<script setup lang="ts">
import {type Ref, ref} from 'vue'
import Order_Component from '@/components/Views/Order_View.vue';
import Order_Form from '@/components/Forms/Order_Form.vue';
import Order_Edit from '@/components/Edits/Order_Edit.vue';

const creatingNewOrder : Ref<Boolean> = ref(true)
</script>

<template>
  <div>
    <h1>Orders Page</h1>
  </div>
  

  <div class="row">
    <div>
      <button class="edit-order" @click="creatingNewOrder = !creatingNewOrder">{{ creatingNewOrder ? 'Edit' : 'Add' }}</button>
      <Order_Form v-if="creatingNewOrder" class="order-update-mainframe" />
      <Order_Edit v-if="!creatingNewOrder" class="order-update-mainframe" />
    </div>
    <Order_Component class="panel" />
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