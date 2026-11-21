import { useTranslation } from "react-i18next";
import { useState } from "react";
import TextEntry from "../common/TextEntry";
import { handleRegister } from "../../api/auth";

export default function RegisterForm() {
  const { t } = useTranslation("auth");

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [displayName, setDisplayName] = useState("");

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        handleRegister(email, password, displayName);
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
      <TextEntry
        placeholder={t("register.displayNameLabel")}
        type="text"
        value={displayName}
        onChange={setDisplayName}
      />
      <button className="bg-lightbrown mt-4 p-2 rounded-md">
        {t("register.submit")}
      </button>
    </form>
  );
}
