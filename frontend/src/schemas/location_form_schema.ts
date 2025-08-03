// src/schemas/location_form_scema.ts
import { z } from "zod";

export const locationFormScema = z.object({
  name: z.string().min(1, "name is required"),
});

export type LocationFormData = z.infer<typeof locationFormScema>;