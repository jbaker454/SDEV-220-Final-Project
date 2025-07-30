<!-- src/pages -->

<script setup lang="ts">
import {type Ref, ref} from 'vue'
import Shipment_Component from '@/components/Views/Shipment_View.vue';
import Shipment_Form from '@/components/Forms/Shipment_Form.vue';
import Shipment_Edit from '@/components/Edits/Shipment_Edit.vue';

const creatingNewShipment : Ref<Boolean> = ref(true)
</script>

<template>
  <div>
    <h1>Shipments Page</h1>
  </div>
  

  <div class="row">
    <div>
      <button class="edit-resource" @click="creatingNewShipment = !creatingNewShipment">{{ creatingNewShipment ? 'Edit' : 'Add' }}</button>
      <Shipment_Form v-if="creatingNewShipment" class="shipment-update-mainframe" />
      <Shipment_Edit v-if="!creatingNewShipment" class="shipment-update-mainframe" />
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