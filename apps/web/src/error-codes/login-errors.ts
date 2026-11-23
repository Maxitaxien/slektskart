export const LOGIN_ERROR_KEYS = {
  invalidCredentials: "login.invalidCredentials",
  serviceUnavailable: "login.serviceUnavailable",
} as const;

export type LoginErrorCode = keyof typeof LOGIN_ERROR_KEYS;
