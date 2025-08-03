<!--src/components/Edits/Inventory_Edit.vue-->
<script setup lang="ts">
import { reactive, ref, type Ref, computed, watch } from "vue";
import { resourceFormSchema, ResourceFormData } from "@/schemas/resource_form_schema";
import { useInterface, Resource } from "@/api/useInterface";
const { resources, locations, updateResource } = useInterface()
import { z } from "zod";

const errors = ref<Partial<Record<keyof Resource, string[]>>>({});

const resourceSelected : Ref<Resource | null> = ref(null)

const form = reactive<ResourceFormData>({
  id: null,
  name: "",
  description: "",
  quantity: 1,
  location: null,
});

async function handleUpdate() {
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
  updateResource(result.data);
}

function makeProxy<K extends keyof ResourceFormData>(
  key: K,
  defaultValue: Resource[K],
  resourceSelected: Ref<Resource | null>,
  form: ResourceFormData
) {
  return computed<Resource[K]>({
    get() {
      return resourceSelected.value?.[key] ?? defaultValue;
    },
    set(val) {
      if (resourceSelected.value) {
        resourceSelected.value[key] = val;
      }
      form[key] = val;
    },
  });
}

const name_proxy = makeProxy("name", "", resourceSelected, form);
const description_proxy = makeProxy("description", "", resourceSelected, form);
const location_proxy = makeProxy("location", null, resourceSelected, form);
const quantity_proxy = makeProxy("quantity", 1, resourceSelected, form);

watch(resourceSelected, (newVal) => {
  if (newVal) {
    form.id = newVal.id;
  }
}, { immediate: true });
</script>

<template>
  <div class="inventory-component-frame">
    <h1>edit resource</h1>
    <select v-model="resourceSelected">
      <option :value="null">Select a resource</option>
      <option
        v-for="resource in resources"
        :key="resource.id"
        :value="resource"
      >
        {{ resource.str_representation }}
      </option>
    </select>
    <form v-if="resourceSelected"  @submit.prevent="handleUpdate">
      <div>
        <label>Name:</label>
        <input v-model="name_proxy" type="text" />
        <p v-if="errors.name">{{ errors.name }}</p>
      </div>
      <div>
        <label>Description:</label>
        <input v-model="description_proxy" type="text" />
        <p v-if="errors.description">{{ errors.description }}</p>
      </div>
      <div>
        <select v-model="location_proxy">
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
        <label>Quantity:</label>
        <input v-model="quantity_proxy" type="number" />
        <p v-if="errors.quantity">{{ errors.quantity }}</p>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<style scoped>
.inventory-component-frame { border: 1px solid #bbb; }
</style>