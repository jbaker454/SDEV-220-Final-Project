<!-- src/components/Forms/Process_Form.vue -->
<script setup lang="ts">
import { reactive, ref } from "vue";
import { shipmentFormSchema, ShipmentFormData } from "@/schemas/shipment_form_scema";
import { useInterface } from "@/api/useInterface";
const { resources, error, submitShipment } = useInterface()
import { z } from "zod";

const errors = ref<Partial<Record<keyof ShipmentFormData, string[]>>>({});

const form = reactive<ShipmentFormData>({
  completed: false,
  quantity: 1,
  date: "",
  resource: null,
  status: 'Incoming',
});

function handleSubmit() {
  const result = shipmentFormSchema.safeParse(form);
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
  submitShipment(result.data);
}

</script>

<template>
  <div class="inventory-componentframe">
    <h1>add resource</h1>
    <form @submit.prevent="handleSubmit">
      <div>
        <label>Completed:</label>
        <input v-model="form.completed" type="checkbox" />
        <p v-if="errors.completed">{{ errors.completed }}</p>
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
        <input v-model="form.quantity" type="number" />
        <p v-if="errors.quantity">{{ errors.quantity }}</p>
      </div>
      <div>
        <label>Date:</label>
        <input v-model="form.date" type="text" />
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
.inventory-componentframe { border: 1px solid #bbb; }
</style>