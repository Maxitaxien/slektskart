import { Link } from "react-router";
import { useTranslation } from "react-i18next";
import RegisterForm from "../components/auth/RegisterForm";

export default function RegisterRoute() {
  const { t } = useTranslation("common");

  return (
    <div className="flex flex-col gap-6">
      <RegisterForm />
      <Link className="bg-lightbrown p-2 rounded-md" to="/">
        {t("home.backButton")}
      </Link>
    </div>
  );
}
