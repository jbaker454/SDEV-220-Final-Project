// src/schemas/resource_form_scema.ts
import { z } from "zod";
import { resourceFormSchema } from "@/schemas/resource_form_schema"

export const shipmentFormSchema = z.object({
  id: z.number().nullable(),
  completed: z.boolean("must be true or false"),
  quantity: z.number().min(1,"quantity is required"),
  resource: z.int().min(1, "a resource id is required").nullable(),
  shipment_type: z.enum(['IN', 'OUT']),
});

export type ShipmentFormData = z.infer<typeof shipmentFormSchema>;