<!--src/components/Edits/Order_Edit.vue-->
<script setup lang="ts">
import { reactive, ref, type Ref } from "vue";
import { useInterface, Order } from "@/api/useInterface";
const { resources, orders, error, updateOrder } = useInterface()
import { z } from "zod";

const errors = ref<Partial<Record<keyof Order, string[]>>>({});

const orderSelected : Ref<Boolean> = ref(false)

const form = reactive<Order>({
  id: 1,
  quantity: 1,
  date: "",
  resource: null,
  status: 'processing',
  str_representation: "",
});

async function handleUpdate() {
  try {
    const updated = await updateOrder(form)
    console.log('Update successful:', updated)
  } catch (error) {
    console.error('Update failed:', error)
  }
}
</script>

<template>
  <div class="inventory-component-frame">
    <h1>edit orders</h1>
    <select v-model="form">
      <option :value="null">Select a order</option>
      <option
        v-for="order in orders"
        :key="order.id"
        :value="order"
        :orderSelected="true"
      >
        {{ order.str_representation }}
      </option>
    </select>
    <form v-if="orderSelected" @submit.prevent="handleUpdate">
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