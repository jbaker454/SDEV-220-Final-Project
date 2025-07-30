// src/schemas/resource_form_scema.ts
import { z } from "zod";
import { resourceFormSchema } from "@/schemas/resource_form_schema"

export const shipmentFormSchema = z.object({
  completed: z.boolean("must be true or false"),
  quantity: z.number().min(1,"quantity is required"),
  date: z.string("date must be a string"),
  resource: resourceFormSchema.nullable(),
  shipment_type: z.enum(['IN', 'OUT','Incoming','Outgoing']),
});

export type ShipmentFormData = z.infer<typeof shipmentFormSchema>;