// src/schemas/resource_form_scema.ts
import { z } from "zod";

export const resourceFormSchema = z.object({
  name: z.string().min(1, "name is required"),
  description: z.string("must be a string"),
  quantity: z.int().min(1, "a quantity is required"),
  received_date: z.string("must be a string"),
});

export type ResourceFormData = z.infer<typeof resourceFormSchema>;