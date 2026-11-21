import { useState } from "react";
import { useTranslation } from "react-i18next";
import TextEntry from "../common/TextEntry";
import { handleLogin } from "../../api/auth";

export default function LoginForm() {
  const { t } = useTranslation("auth");

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        handleLogin(email, password);
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
    </form>
  );
}
