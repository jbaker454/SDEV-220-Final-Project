//src/api/use_interface
import { ref } from 'vue'
import { z } from "zod";

import { ResourceFormData } from "@/schemas/resource_form_schema";
import { OrderFormData } from "@/schemas/order_form_schema";
import { ProcessFormData } from "@/schemas/process_form_schema";
import { ShipmentFormData } from "@/schemas/shipment_form_schema";


export interface Location {
  id: number | string
  name: string
}

export interface Resource {
  id: number | string
  name: string
  description: string
  quantity: number
  received_date: string
  location: string | null
  str_representation: string
}

export interface Order {
  id: number | string
  quantity: number
  date: string
  resource: Resource | null
  status: 'processing' | 'completed' | 'cancelled'
  str_representation: string
}

export interface Process {
  id: number | string
  name: string
  description: string
  items_per_second: number
  date: string
  resource: Resource | null
  status: 'pending' | 'done'
  str_representation: string
}

export interface Shipment {
  id: number | string
  completed: boolean
  date: string
  quantity: number
  resource: Resource | null
  shipment_type: 'IN' | 'OUT' | 'Incoming' | 'Outgoing'
  str_representation: string
}

const resources = ref<Resource[]>([])
const orders = ref<Order[]>([])
const processes = ref<Process[]>([])
const shipments = ref<Shipment[]>([])
const error = ref<string | null>(null)

async function fetchResources(): Promise<void> {
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

export async function updateResource(resource: Resource): Promise<Resource> {
  const response = await fetch(`http://localhost:8000/api/resources/${resource.id}/`, {
    method: 'PUT', // or PATCH if partial update
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(resource),
  })

  if (!response.ok) {
    throw new Error(`Failed to update resource ${resource.id}`)
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

export async function updateOrder(order: Order): Promise<Order> {
  const response = await fetch(`http://localhost:8000/api/orders/${order.id}/`, {
    method: 'PUT', // or PATCH if partial update
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(order),
  })

  if (!response.ok) {
    throw new Error(`Failed to update order ${order.id}`)
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

export async function updateProcess(process: Process): Promise<Process> {
  const response = await fetch(`http://localhost:8000/api/processes/${process.id}/`, {
    method: 'PUT', // or PATCH if partial update
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(process),
  })

  if (!response.ok) {
    throw new Error(`Failed to update process ${process.id}`)
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

export async function updateShipment(shipment: Shipment): Promise<Shipment> {
  const response = await fetch(`http://localhost:8000/api/shipments/${shipment.id}/`, {
    method: 'PUT', // or PATCH if partial update
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(shipment),
  })

  if (!response.ok) {
    throw new Error(`Failed to update shipment ${shipment.id}`)
  }

  return await response.json()
}

export function useInterface() {
  return {
    resources,
    orders,
    processes,
    shipments,
    error,
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
