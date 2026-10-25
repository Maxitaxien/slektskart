import { useTranslation } from "react-i18next";

export default function LoginForm() {
  const { t } = useTranslation("auth");
  return (
    <div>
      <h1>{t("login.title")}</h1>
      <button>{t("login.submit")}</button>
    </div>
  );
}
