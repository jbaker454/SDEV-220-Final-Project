<!-- src/pages -->

<script setup lang="ts">
import {type Ref, ref} from 'vue'
import Process_Component from '@/components/Views/Process_View.vue';
import Process_Form from '@/components/Forms/Process_Form.vue';
import Process_Edit from '@/components/Edits/Process_Edit.vue';

const creatingNewProcess : Ref<Boolean> = ref(true)
</script>

<template>
  <div>
    <h1>Processes Page</h1>
  </div>
  

  <div class="row">
    <div>
      <button class="edit-resource" @click="creatingNewProcess = !creatingNewProcess">{{ creatingNewProcess ? 'Edit' : 'Add' }}</button>
      <Process_Form v-if="creatingNewProcess" class="process-update-mainframe" />
      <Process_Edit v-if="!creatingNewProcess" class="process-update-mainframe" />
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