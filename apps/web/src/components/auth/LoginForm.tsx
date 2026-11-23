import { useState } from "react";
import { useTranslation } from "react-i18next";
import TextEntry from "../common/TextEntry";
import { ApiError } from "../../api/client";
import { handleLogin } from "../../api/auth";
import type { LoginErrorCode } from "../../error-codes/login-errors";
import { LOGIN_ERROR_KEYS } from "../../error-codes/login-errors";

export default function LoginForm({ onSuccess }: { onSuccess: () => void }) {
  const { t } = useTranslation("auth");

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loginError, setLoginError] = useState<LoginErrorCode | null>(null);

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        handleLogin(email, password)
          .then(onSuccess)
          .catch((error) => {
            if (error instanceof ApiError && error.status === 401) {
              setLoginError("invalidCredentials");
              return;
            } else {
              setLoginError("serviceUnavailable");
              return;
            }
          });
      }}
    >
      <TextEntry
        placeholder={t("shared.emailLabel")}
        type="email"
        value={email}
        onChange={setEmail}
      />
      <TextEntry
        placeholder={t("shared.passwordLabel")}
        type="password"
        value={password}
        onChange={setPassword}
      />
      <button className="bg-lightbrown mt-4 p-2 rounded-md">
        {t("login.submit")}
      </button>
      {loginError && <InvalidLoginDisplay loginError={loginError} />}
    </form>
  );
}

function InvalidLoginDisplay({ loginError }: { loginError: LoginErrorCode }) {
  const { t } = useTranslation("auth");
  return <p className="text-red-500">{t(LOGIN_ERROR_KEYS[loginError])}</p>;
}
