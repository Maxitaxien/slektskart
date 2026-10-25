import { useTranslation } from "react-i18next";

export default function RegisterForm() {
  const { t } = useTranslation("auth");
  return (
    <div>
      <h1>{t("register.title")}</h1>
      <button>{t("register.submit")}</button>
    </div>
  );
}
