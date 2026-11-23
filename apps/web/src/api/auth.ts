import { api } from "./client";

interface UserCreate {
  email: string;
  password: string;
  display_name: string;
}

export async function handleLogin(
  email: string,
  password: string,
): Promise<boolean> {
  const response: Response = await api("/api/auth/login", {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });

  return response.ok;
}

export async function handleRegister(
  email: string,
  password: string,
  displayName: string,
): Promise<UserCreate> {
  return api("/api/auth/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
      display_name: displayName,
    }),
  });
}
