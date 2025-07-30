<!--src/components/Edits/Inventory_Edit.vue-->
<script setup lang="ts">
import { reactive, ref, type Ref } from "vue";
import { useInterface, Resource } from "@/api/useInterface";
const { resources, error, updateResource } = useInterface()
import { z } from "zod";

const errors = ref<Partial<Record<keyof Resource, string[]>>>({});

const resourceSelected : Ref<Boolean> = ref(false)

const form = reactive<Resource>({
  id: 1,
  name: "",
  description: "",
  quantity: 1,
  received_date: "",
  location: null,
  str_representation: "",
});

async function handleUpdate() {
  try {
    const updated = await updateResource(form)
    console.log('Update successful:', updated)
  } catch (error) {
    console.error('Update failed:', error)
  }
}
</script>

<template>
  <div class="inventory-component-frame">
    <h1>edit resource</h1>
    <select v-model="form">
      <option :value="null">Select a resource</option>
      <option
        v-for="resource in resources"
        :key="resource.id"
        :value="resource"
        :resourceSelected="true"
      >
        {{ resource.str_representation }}
      </option>
    </select>
    <form v-if="resourceSelected"  @submit.prevent="handleUpdate">
      <div>
        <label>Name:</label>
        <input v-model="form.name" type="text" />
        <p v-if="errors.name">{{ errors.name }}</p>
      </div>
      <div>
        <label>Description:</label>
        <input v-model="form.description" type="text" />
        <p v-if="errors.description">{{ errors.description }}</p>
      </div>
      <div>
        <label>Quantity:</label>
        <input v-model="form.quantity" type="number" />
        <p v-if="errors.quantity">{{ errors.quantity }}</p>
      </div>
      <div>
        <label>Received Date:</label>
        <input v-model="form.received_date" type="date" />
        <p v-if="errors.received_date">{{ errors.received_date }}</p>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<style scoped>
.inventory-component-frame { border: 1px solid #bbb; }
</style>