//src/api/use_interface
import { ref } from 'vue'
import { z } from "zod";

import { ResourceFormData } from "@/schemas/resource_form_schema";
import { OrderFormData } from "@/schemas/order_form_schema";
import { ProcessFormData } from "@/schemas/process_form_schema";
import { ShipmentFormData } from "@/schemas/shipment_form_schema";


export interface Location {
  id: number
  name: string
}

export interface Resource {
  id: number
  name: string
  description: string
  quantity: number
  received_date: string
  location: number | null
  str_representation: string
}

export interface Order {
  id: number
  quantity: number
  date: string
  resource: number | null
  status: 'processing' | 'completed' | 'cancelled'
  str_representation: string
}

export interface Process {
  id: number
  name: string
  description: string
  items_per_second: number
  resource: number | null
  status: 'pending' | 'done'
  str_representation: string
}

export interface Shipment {
  id: number
  completed: boolean
  date: string
  quantity: number
  resource: number | null
  shipment_type: 'IN' | 'OUT'
  str_representation: string
}

const locations = ref<Location[]>([])
const resources = ref<Resource[]>([])
const orders = ref<Order[]>([])
const processes = ref<Process[]>([])
const shipments = ref<Shipment[]>([])
const error = ref<string | null>(null)

export async function fetchLocations(): Promise<void> {
  try {
    const response = await fetch('http://localhost:8000/api/locations/')
    if (!response.ok) throw new Error('Failed to fetch locations')
    locations.value = await response.json()
  } catch (err) {
    error.value = err instanceof Error ? err.message : String(err)
  }
}

export async function fetchResources(): Promise<void> {
  try {
    const response = await fetch('http://localhost:8000/api/resources/')
    if (!response.ok) throw new Error('Failed to fetch resources')
    resources.value = await response.json()
  } catch (err) {
    error.value = err instanceof Error ? err.message : String(err)
  }
}

export async function submitResource(data: ResourceFormData) {
  const response = await fetch("http://localhost:8000/api/resources/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) throw new Error("Failed to submit resource");
  const responseData = await response.json();
  return responseData.id;
}

export async function updateResource(data: ResourceFormData) {
  console.log(JSON.stringify(data))
  const response = await fetch(`http://localhost:8000/api/resources/${data.id}/`, {
    method: 'PUT', // or PATCH if partial update
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error(`Failed to update resource ${data}`)
  }

  return await response.json()
}

async function fetchOrders(): Promise<void> {
  try {
    const response = await fetch('http://localhost:8000/api/orders/')
    if (!response.ok) throw new Error('Failed to fetch orders')
    orders.value = await response.json()
  } catch (err) {
    error.value = err instanceof Error ? err.message : String(err)
  }
}

export async function submitOrder(data: OrderFormData) {
  const response = await fetch("http://localhost:8000/api/orders/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) throw new Error("Failed to submit order");
  const responseData = await response.json();
  return responseData.id;
}

export async function updateOrder(data: OrderFormData) {
  const response = await fetch(`http://localhost:8000/api/orders/${data.id}/`, {
    method: 'PUT', // or PATCH if partial update
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error(`Failed to update order ${data}`)
  }

  return await response.json()
}

async function fetchProcesses(): Promise<void> {
  try {
    const response = await fetch('http://localhost:8000/api/processes/')
    if (!response.ok) throw new Error('Failed to fetch processes')
    const data: Process[] = await response.json()
    processes.value = data
  } catch (err) {
    error.value = err instanceof Error ? err.message : String(err)
  }
}

export async function submitProcess(data: ProcessFormData) {
  const response = await fetch("http://localhost:8000/api/processes/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) throw new Error("Failed to submit process");
  const responseData = await response.json();
  return responseData.id;
}

export async function updateProcess(data: ProcessFormData) {
  const response = await fetch(`http://localhost:8000/api/processes/${data.id}/`, {
    method: 'PUT', // or PATCH if partial update
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error(`Failed to update process ${data.id}`)
  }

  return await response.json()
}

async function fetchShipments(): Promise<void> {
  try {
    const response = await fetch('http://localhost:8000/api/shipments/')
    if (!response.ok) throw new Error('Failed to fetch shipments')
    const data: Shipment[] = await response.json()
    shipments.value = data
  } catch (err) {
    error.value = err instanceof Error ? err.message : String(err)
  }
}

export async function submitShipment(data: ShipmentFormData) {
  const response = await fetch("http://localhost:8000/api/shipments/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) throw new Error("Failed to submit shipment");
  const responseData = await response.json();
  return responseData.id;
}

export async function updateShipment(data: ShipmentFormData) {
  const response = await fetch(`http://localhost:8000/api/shipments/${data.id}/`, {
    method: 'PUT', // or PATCH if partial update
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error(`Failed to update shipment ${data}`)
  }

  return await response.json()
}

export function useInterface() {
  return {
    locations,
    resources,
    orders,
    processes,
    shipments,
    error,
    fetchLocations,

    fetchResources,
    submitResource,
    updateResource,

    fetchOrders,
    submitOrder,
    updateOrder,

    fetchProcesses,
    submitProcess,
    updateProcess,

    fetchShipments,
    submitShipment,
    updateShipment,
  }
}
