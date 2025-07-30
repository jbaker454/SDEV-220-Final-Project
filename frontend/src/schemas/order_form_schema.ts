// src/schemas/resource_form_scema.ts
import { z } from "zod";
import { resourceFormSchema } from "@/schemas/resource_form_schema"

export const orderFormSchema = z.object({
  quantity: z.number().min(1,"quantity is required"),
  date: z.string("date must be a string"),
  resource: resourceFormSchema.nullable(),
  status: z.enum(['processing', 'completed', 'cancelled']),
});

export type OrderFormData = z.infer<typeof orderFormSchema>;