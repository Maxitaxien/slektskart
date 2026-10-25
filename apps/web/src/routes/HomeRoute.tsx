import { Link } from "react-router";
import { useTranslation } from "react-i18next";

export default function HomeRoute() {
  const { t } = useTranslation("common");

  return (
    <div>
      <h1>hi there!</h1>
      <Link to="/register">{t("home.registerButton")}</Link>
      <Link to="/login">{t("home.loginButton")}</Link>
    </div>
  );
}
