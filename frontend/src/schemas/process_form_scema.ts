// src/schemas/resource_form_scema.ts
import { z } from "zod";
import { resourceFormSchema } from "@/schemas/resource_form_scema"

export const processFormSchema = z.object({
  name: z.string().min(1, "name is required"),
  quantity: z.number().min(1,"quantity is required"),
  date: z.string("date must be a string"),
  resource: resourceFormSchema.nullable(),
  status: z.enum(['pending', 'done']),
});

export type ProcessFormData = z.infer<typeof processFormSchema>;