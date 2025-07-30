<!--src/components/Edits/Process_Edit.vue-->
<script setup lang="ts">
import { reactive, ref, type Ref } from "vue";
import { useInterface, Process } from "@/api/useInterface";
const { resources, processes, error, updateProcess } = useInterface()
import { z } from "zod";

const errors = ref<Partial<Record<keyof Process, string[]>>>({});

const processSelected : Ref<Boolean> = ref(false)

const form = reactive<Process>({
  id: 0,
  name: "",
  description: "",
  items_per_second: 0,
  date: "",
  resource: null,
  status: 'pending',
  str_representation: "",
});

async function handleUpdate() {
  try {
    const updated = await updateProcess(form)
    console.log('Update successful:', updated)
  } catch (error) {
    console.error('Update failed:', error)
  }
}
</script>

<template>
  <div class="inventory-component-frame">
    <h1>edit processes</h1>
    <select v-model="form">
      <option :value="null">Select a process</option>
      <option
        v-for="process in processes"
        :key="process.id"
        :value="process"
        :processSelected="true"
      >
        {{ process.str_representation }}
      </option>
    </select>
    <form v-if="processSelected" @submit.prevent="handleUpdate">
      <div>
        <label>Name:</label>
        <input v-model="form.name" type="text" />
        <p v-if="errors.name">{{ errors.name }}</p>
      </div>
      <div>
        <select v-model="form.resource">
          <option :value="null">Select a resource</option>
          <option
            v-for="resource in resources"
            :key="resource.id"
            :value="resource"
          >
            {{ resource.name }}
          </option>
        </select>
      </div>
      <div>
        <label>Quantity:</label>
        <input v-model="form.items_per_second" type="number" />
        <p v-if="errors.items_per_second">{{ errors.items_per_second }}</p>
      </div>
      <div>
        <label>Date:</label>
        <input v-model="form.date" type="date" />
        <p v-if="errors.date">{{ errors.date }}</p>
      </div>
      <div>
        <label>Status:</label>
        <select v-model="form.status">
          <option value="pending">Pending</option>
          <option value="done">Done</option>
        </select>
        <p v-if="errors.status">{{ errors.status }}</p>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<style scoped>
.inventory-component-frame { border: 1px solid #bbb; }
</style>