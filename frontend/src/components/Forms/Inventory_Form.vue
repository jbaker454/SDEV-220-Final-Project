<!-- src/components/Forms/Inventory_Form.vue -->
<script setup lang="ts">
import { reactive, ref, onMounted } from "vue";
import { resourceFormSchema, ResourceFormData } from "@/schemas/resource_form_schema";
import { useInterface } from "@/api/useInterface";
const { locations, submitResource, fetchLocations } = useInterface()
import { z } from "zod";

const errors = ref<Partial<Record<keyof ResourceFormData, string[]>>>({});

const form = reactive<ResourceFormData>({
  id: null,
  name: "",
  description: "",
  quantity: 1,
  location: null,
});

function handleSubmit() {
  const result = resourceFormSchema.safeParse(form);
  if (!result.success) {
    const fieldErrors: Record<string, string[]> = {};

    for (const issue of result.error.issues) {
      const path = issue.path.join(".");
      fieldErrors[path] = fieldErrors[path] || [];
      fieldErrors[path].push(issue.message);
    }

    errors.value = fieldErrors;
    return;
  }

  errors.value = {};
  submitResource(result.data);
}
onMounted(() => {
  fetchLocations()
})
</script>

<template>
  <div class="inventory-component-frame">
    <h1>add resource</h1>
    <form @submit.prevent="handleSubmit">
      <div>
        <label>Name:</label>
        <input v-model="form.name" type="text" />
        <p v-if="errors.name">{{ errors.name }}</p>
      </div>
      <div>
        <select v-model="form.location">
          <option :value="null">Select a location</option>
          <option
            v-for="location in locations"
            :key="location.id"
            :value="location.id"
          >
            {{ location.name }}
          </option>
        </select>
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
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<style scoped>
.inventory-component-frame { border: 1px solid #bbb; }
</style>