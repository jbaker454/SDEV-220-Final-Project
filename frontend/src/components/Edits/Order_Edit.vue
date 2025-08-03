<!--src/components/Edits/Order_Edit.vue-->
<script setup lang="ts">
import { reactive, ref, type Ref, computed, watch } from "vue";
import { orderFormSchema, OrderFormData } from "@/schemas/order_form_schema";
import { useInterface, Order } from "@/api/useInterface";
const { resources, orders, updateOrder } = useInterface()
import { z } from "zod";

const errors = ref<Partial<Record<keyof Order, string[]>>>({});

const orderSelected : Ref<Order | null> = ref(null)

const form = reactive<OrderFormData>({
  id: null,
  quantity: 1,
  resource: 1,
  status: "processing",
});

async function handleUpdate() {
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
  updateOrder(result.data);
}

function makeProxy<K extends keyof OrderFormData>(
  key: K,
  defaultValue: Order[K],
  orderSelected: Ref<Order | null>,
  form: OrderFormData
) {
  return computed<Order[K]>({
    get() {
      return orderSelected.value?.[key] ?? defaultValue;
    },
    set(val) {
      if (orderSelected.value) {
        orderSelected.value[key] = val;
      }
      form[key] = val;
    },
  });
}

const quantity_proxy = makeProxy("quantity", 1, orderSelected, form);
const resource_proxy = makeProxy("resource", null, orderSelected, form);
const status_proxy = makeProxy("status", "processing", orderSelected, form);

watch(orderSelected, (newVal) => {
  if (newVal) {
    form.id = newVal.id;
  }
}, { immediate: true });
</script>

<template>
  <div class="inventory-component-frame">
    <h1>edit orders</h1>
    <select v-model="orderSelected">
      <option :value="null">Select a order</option>
      <option
        v-for="order in orders"
        :key="order.id"
        :value="order"
      >
        {{ order.str_representation }}
      </option>
    </select>
    <form v-if="orderSelected" @submit.prevent="handleUpdate">
      <div>
        <label>Quantity:</label>
        <input v-model="quantity_proxy" type="number" />
        <p v-if="errors.quantity">{{ errors.quantity }}</p>
      </div>
      <div>
        <select v-model="resource_proxy">
          <option :value="null">Select a resource</option>
          <option
            v-for="resource in resources"
            :key="resource.id"
            :value="resource.id"
          >
            {{ resource.name }}
          </option>
        </select>
      </div>
      <div>
        <label>Status:</label>
        <select v-model="status_proxy">
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