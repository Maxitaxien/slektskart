import { Route, Routes } from "react-router";

import AuthProvider from "../auth/AuthProvider";

import HomeRoute from "./HomeRoute";
import LoginRoute from "./LoginRoute";
import RegisterRoute from "./RegisterRoute";

export default function AppRoutes() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/" element={<HomeRoute />}>
          <Route index element={<LoginRoute />} />
          <Route path="/login" element={<LoginRoute />} />
          <Route path="/register" element={<RegisterRoute />} />
        </Route>
      </Routes>
    </AuthProvider>
  );
}
