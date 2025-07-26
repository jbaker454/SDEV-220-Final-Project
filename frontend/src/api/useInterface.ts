//src/api/use_interface
import { ref } from 'vue'

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

interface Shipment {
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

async function fetchOrders(): Promise<void> {
  try {
    const response = await fetch('http://localhost:8000/api/orders/')
    if (!response.ok) throw new Error('Failed to fetch orders')
    orders.value = await response.json()
  } catch (err) {
    error.value = err instanceof Error ? err.message : String(err)
  }
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

async function fetchShipments(): Promise<void> {
  try {
    const response = await fetch('http://localhost:8000/api/shipments/')
    if (!response.ok) throw new Error('Network response was not ok')
    const data: Shipment[] = await response.json()
    shipments.value = data
  } catch (err) {
    error.value = err instanceof Error ? err.message : String(err)
  }
}

export function useInterface() {
  return {
    resources,
    orders,
    processes,
    shipments,
    error,
    fetchResources,
    fetchOrders,
    fetchProcesses,
    fetchShipments,
  }
}
