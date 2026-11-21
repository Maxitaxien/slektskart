import { Outlet } from "react-router";

export default function HomeRoute() {
  return (
    <div className="flex flex-col bg-eggshell my-20 m-auto pb-10 w-2/4 rounded-xl gap-8 items-center">
      <img src="slektskartv1.png" alt="Slektskart" />
      <Outlet />
    </div>
  );
}
