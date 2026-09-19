import { useEffect } from "react";
import { api } from "@/api/client";

function App() {
  useEffect(() => {
    async function testApi() {
      const result = await api<{ status: string }>("/api/health");

      console.log(result);
    }

    testApi();
  }, []);

  return <h1>API test</h1>;
}

export default App;
