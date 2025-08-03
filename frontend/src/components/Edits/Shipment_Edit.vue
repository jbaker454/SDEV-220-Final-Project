<!--src/components/Edits/Shipment_Edit.vue-->
<script setup lang="ts">
import { reactive, ref, type Ref, computed, watch } from "vue";
import { shipmentFormSchema, ShipmentFormData } from "@/schemas/shipment_form_schema";
import { useInterface, Shipment } from "@/api/useInterface";
const { resources, shipments, updateShipment } = useInterface()
import { z } from "zod";

const errors = ref<Partial<Record<keyof Shipment, string[]>>>({});

const shipmentSelected: Ref<Shipment | null> = ref(null);

const form = reactive<ShipmentFormData>({
  id: null,
  completed: false,
  quantity: 1,
  resource: null,
  shipment_type: 'IN',
});

async function handleUpdate() {
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
  updateShipment(result.data);
}

function makeProxy<K extends keyof ShipmentFormData>(
  key: K,
  defaultValue: Shipment[K],
  shipmentSelected: Ref<Shipment | null>,
  form: ShipmentFormData
) {
  return computed<Shipment[K]>({
    get() {
      return shipmentSelected.value?.[key] ?? defaultValue;
    },
    set(val) {
      if (shipmentSelected.value) {
        shipmentSelected.value[key] = val;
      }
      form[key] = val;
    },
  });
}

const completed_proxy = makeProxy("completed", false, shipmentSelected, form);
const quantity_proxy = makeProxy("quantity", 1, shipmentSelected, form);
const resource_proxy = makeProxy("resource", null, shipmentSelected, form);
const shipment_type_proxy = makeProxy("shipment_type", "IN", shipmentSelected, form);

watch(shipmentSelected, (newVal) => {
  if (newVal) {
    form.id = newVal.id;
  }
}, { immediate: true });
</script>



<template>
  <div class="inventory-component-frame">
    <h1>edit shipments</h1>
    <select v-model="shipmentSelected">
      <option :value="null">Select a shipment</option>
      <option
        v-for="shipment in shipments"
        :key="shipment.id"
        :value="shipment"
      >
        {{ shipment.str_representation }}
      </option>
    </select>
    <form v-if="shipmentSelected" @submit.prevent="handleUpdate">
      <div>
        <label>
          Completed:
          <input
            type="checkbox"
            v-model="completed_proxy"
            :disabled="!shipmentSelected"
          />
        </label>
        <p v-if="errors.completed">{{ errors.completed }}</p>
      </div>
      <div>
        <select v-model="resource_proxy">
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
        <input v-model="quantity_proxy" type="number" />
        <p v-if="errors.quantity">{{ errors.quantity }}</p>
      </div>
      <div>
        <label>shipment_type:</label>
        <select v-model="shipment_type_proxy">
          <option value="IN">IN</option>
          <option value="OUT">OUT</option>
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