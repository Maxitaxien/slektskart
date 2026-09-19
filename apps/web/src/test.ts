import { api } from "@/api/client";

const result = await api<{ status: string }>("/api/health");

console.log(result);
