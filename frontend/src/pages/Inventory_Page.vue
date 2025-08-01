<!-- src/pages -->

<script setup lang="ts">
<<<<<<< Updated upstream
import {type Ref, ref} from 'vue'
import Inventory_View from '@/components/Views/Inventory_View.vue';
import Inventory_Form from '@/components/Forms/Inventory_Form.vue';
import Inventory_Edit from '@/components/Edits/Inventory_Edit.vue';

const creatingNewResource : Ref<Boolean> = ref(true)
=======
  import Inventory_View_Component from '@/components/Views/Inventory_View.vue';
  // import Inventory_Modify_Component from '@/components/Modifies/Inventory_Modify.vue';
>>>>>>> Stashed changes
</script>

<template>
  <div>
    <h1>Inventory Page</h1>
  </div>
  <div class="row">
    <div>
      <button class="edit-resource" @click="creatingNewResource = !creatingNewResource">{{ creatingNewResource ? 'Edit' : 'Add' }}</button>
      <Inventory_Form v-if="creatingNewResource" class="inventory-update-mainframe" />
      <Inventory_Edit v-if="!creatingNewResource" class="inventory-update-mainframe" />
    </div>
    <Inventory_View class="panel" />
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