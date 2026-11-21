import LoginForm from "../components/auth/LoginForm";
import { Link } from "react-router";
import { useTranslation } from "react-i18next";

export default function LoginRoute() {
  const { t } = useTranslation("common");

  return (
    <div className="flex flex-col gap-8">
      <LoginForm />
      <Link className="bg-lightbrown p-2 rounded-md" to="/register">
        {t("home.registerButton")}
      </Link>
    </div>
  );
}
