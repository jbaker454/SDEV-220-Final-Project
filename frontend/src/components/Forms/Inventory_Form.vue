<!-- src/components/Forms/Inventory_Form.vue -->
<script setup lang="ts">
import { reactive, ref } from "vue";
import { resourceFormSchema, ResourceFormData } from "@/schemas/resource_form_scema";
import { submitResource } from "@/api/useInterface";
import { z } from "zod";

const errors = ref<Partial<Record<keyof ResourceFormData, string[]>>>({});

const form = reactive<ResourceFormData>({
  name: "",
  description: "",
  quantity: 1,
  received_date: "",
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

</script>

<template>
  <div class="inventory-componentframe">
    <h1>add resource</h1>
    <form @submit.prevent="handleSubmit">
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
        <input v-model="form.received_date" type="text" />
        <p v-if="errors.received_date">{{ errors.received_date }}</p>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<style scoped>
.inventory-componentframe { border: 1px solid #bbb; }
</style>