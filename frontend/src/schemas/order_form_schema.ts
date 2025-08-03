// src/schemas/resource_form_scema.ts
import { z } from "zod";
import { resourceFormSchema } from "@/schemas/resource_form_schema"

export const orderFormSchema = z.object({
  id: z.number().nullable(),
  quantity: z.number().min(1,"quantity is required"),
  resource: z.int().min(1, "a resource id is required").nullable(),
  status: z.enum(['processing', 'completed', 'cancelled']),
});

export type OrderFormData = z.infer<typeof orderFormSchema>;