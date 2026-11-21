import { api } from "./client";

interface TokenResponse {
  access_token: string;
  token_type: string;
}

interface UserCreate {
  email: string;
  password: string;
  display_name: string;
}

export async function handleLogin(
  email: string,
  password: string,
): Promise<TokenResponse> {
  const response: TokenResponse = await api("/api/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });

  console.log(response);
  return response;
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
