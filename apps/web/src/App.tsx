import { useEffect } from "react";
import { api } from "@/api/client";
import AppRoutes from "./routes/AppRoutes";

function App() {
  useEffect(() => {
    async function testApi() {
      const result = await api<{ status: string }>("/api/health");

      console.log(result);
    }

    testApi();
  }, []);

  return <AppRoutes />;
}

export default App;
