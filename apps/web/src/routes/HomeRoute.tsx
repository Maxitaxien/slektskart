import { Link, Outlet } from "react-router";
import { useTranslation } from "react-i18next";
import LoginForm from "../components/auth/LoginForm";

export default function HomeRoute() {
  const { t } = useTranslation("common");

  return (
    <div className="flex flex-col bg-eggshell m-auto pb-10 w-2/4 rounded-xl gap-8 items-center">
      <img src="slektskartv1.png" alt="Slektskart" />
      <LoginForm />
      <Link className="bg-lightbrown p-2 rounded-md" to="/register">
        {t("home.registerButton")}
      </Link>
    </div>
  );
}
