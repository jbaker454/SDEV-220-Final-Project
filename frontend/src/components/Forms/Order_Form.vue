<!-- src/components/Forms/Inventory_Form.vue -->
<script setup lang="ts">
import { reactive, ref } from "vue";
import { orderFormSchema, OrderFormData } from "@/schemas/order_form_schema";
import { useInterface } from "@/api/useInterface";
const { resources, error, submitOrder } = useInterface()
import { z } from "zod";

const errors = ref<Partial<Record<keyof OrderFormData, string[]>>>({});

const form = reactive<OrderFormData>({
  quantity: 1,
  date: "",
  resource: null,
  status: "processing",
});

function handleSubmit() {
  const result = orderFormSchema.safeParse(form);
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
  submitOrder(result.data);
}

</script>

<template>
  <div class="inventory-component-frame">
    <h1>add resource</h1>
    <form @submit.prevent="handleSubmit">
      <div>
        <label>Quantity:</label>
        <input v-model="form.quantity" type="number" />
        <p v-if="errors.quantity">{{ errors.quantity }}</p>
      </div>
      <div>
        <label>Date:</label>
        <input v-model="form.date" type="date" />
        <p v-if="errors.date">{{ errors.date }}</p>
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
        <label>Status:</label>
        <select v-model="form.status">
          <option value="processing">Processing</option>
          <option value="completed">Completed</option>
          <option value="cancelled">Cancelled</option>
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