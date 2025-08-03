<!--src/components/Edits/Process_Edit.vue-->
<script setup lang="ts">
import { reactive, ref, type Ref, computed, watch } from "vue";
import { processFormSchema, ProcessFormData } from "@/schemas/process_form_schema";
import { useInterface, Process } from "@/api/useInterface";
const { resources, processes, updateProcess } = useInterface()
import { z } from "zod";

const errors = ref<Partial<Record<keyof Process, string[]>>>({});

const processSelected : Ref<Process | null> = ref(null)

const form = reactive<ProcessFormData>({
  id: null,
  name: "",
  items_per_second: 1,
  resource: null,
  status: 'pending',
});

async function handleUpdate() {
  const result = processFormSchema.safeParse(form);
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
  updateProcess(result.data);
}

function makeProxy<K extends keyof ProcessFormData>(
  key: K,
  defaultValue: Process[K],
  processSelected: Ref<Process | null>,
  form: ProcessFormData
) {
  return computed<Process[K]>({
    get() {
      return processSelected.value?.[key] ?? defaultValue;
    },
    set(val) {
      if (processSelected.value) {
        processSelected.value[key] = val;
      }
      form[key] = val;
    },
  });
}

const name_proxy = makeProxy("name", "", processSelected, form);
const items_per_second_proxy = makeProxy("items_per_second", 1, processSelected, form);
const resource_proxy = makeProxy("resource", null, processSelected, form);
const status_proxy = makeProxy("status", "pending", processSelected, form);

watch(processSelected, (newVal) => {
  if (newVal) {
    form.id = newVal.id;
  }
}, { immediate: true });
</script>

<template>
  <div class="inventory-component-frame">
    <h1>edit processes</h1>
    <select v-model="processSelected">
      <option :value="null">Select a process</option>
      <option
        v-for="process in processes"
        :key="process.id"
        :value="process"
      >
        {{ process.str_representation }}
      </option>
    </select>
    <form v-if="processSelected" @submit.prevent="handleUpdate">
      <div>
        <label>Name:</label>
        <input v-model="name_proxy" type="text" />
        <p v-if="errors.name">{{ errors.name }}</p>
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
        <label>items_per_second:</label>
        <input v-model="items_per_second_proxy" type="number" />
        <p v-if="errors.items_per_second">{{ errors.items_per_second }}</p>
      </div>
      <div>
        <label>Status:</label>
        <select v-model="status_proxy">
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