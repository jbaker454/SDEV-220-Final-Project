// src/schemas/resource_form_scema.ts
import { z } from "zod";

export const resourceFormSchema = z.object({
  id: z.int().min(1, "a resource id is required").nullable(),
  name: z.string().min(1, "name is required"),
  description: z.string("must be a string"),
  quantity: z.int().min(1, "a quantity is required"),
  location: z.int().min(1, "a location id is required").nullable(),
});

export type ResourceFormData = z.infer<typeof resourceFormSchema>;