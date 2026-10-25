import { Route, Routes } from "react-router";

import HomeRoute from "./HomeRoute";
import LoginRoute from "./LoginRoute";
import RegisterRoute from "./RegisterRoute";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<HomeRoute />} />
      <Route path="/login" element={<LoginRoute />} />
      <Route path="/register" element={<RegisterRoute />} />
    </Routes>
  );
}
