<!--src/components/Edits/Shipment_Edit.vue-->
<script setup lang="ts">
import { reactive, ref, type Ref } from "vue";
import { useInterface, Shipment } from "@/api/useInterface";
const { resources, shipments, error, updateShipment } = useInterface()
import { z } from "zod";

const errors = ref<Partial<Record<keyof Shipment, string[]>>>({});

const shipmentSelected : Ref<Boolean> = ref(false)

const form = reactive<Shipment>({
  id: 0,
  completed: false,
  date: "",
  quantity: 1,
  resource: null,
  shipment_type: 'Incoming',
  str_representation: "",
});

async function handleUpdate() {
  try {
    const updated = await updateShipment(form)
    console.log('Update successful:', updated)
  } catch (error) {
    console.error('Update failed:', error)
  }
}
</script>

<template>
  <div class="inventory-component-frame">
    <h1>edit shipments</h1>
    <select v-model="form">
      <option :value="null">Select a shipment</option>
      <option
        v-for="shipment in shipments"
        :key="shipment.id"
        :value="shipment"
        :shipmentSelected="true"
      >
        {{ shipment.str_representation }}
      </option>
    </select>
    <form v-if="shipmentSelected" @submit.prevent="handleUpdate">
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
        <input v-model="form.date" type="date" />
        <p v-if="errors.date">{{ errors.date }}</p>
      </div>
      <div>
        <label>shipment_type:</label>
        <select v-model="form.shipment_type">
          <option value="pending">Pending</option>
          <option value="done">Done</option>
        </select>
        <p v-if="errors.shipment_type">{{ errors.shipment_type }}</p>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<style scoped>
.inventory-component-frame { border: 1px solid #bbb; }
</style>