const API_URL = import.meta.env.VITE_API_URL;

export class ApiError extends Error {
  readonly status: number;

  constructor(status: number, message: string) {
    super(message);
    this.name = "ApiError";
    this.status = status;
  }
}

export async function api<T>(path: string, args?: RequestInit): Promise<T> {
  if (!args) {
    args = {};
  }

  const response = await fetch(`${API_URL}${path}`, args);
  const body = await response.json();

  if (!response.ok) {
    throw new ApiError(response.status, body.detail);
  }

  return body;
}
