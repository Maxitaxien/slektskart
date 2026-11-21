const API_URL = import.meta.env.VITE_API_URL;

export async function api<T>(path: string, args?: RequestInit): Promise<T> {
  if (!args) {
    args = {};
  }

  const response = await fetch(`${API_URL}${path}`, args);

  if (!response.ok) {
    throw new Error(`API error: ${response.status}`);
  }

  return response.json();
}
