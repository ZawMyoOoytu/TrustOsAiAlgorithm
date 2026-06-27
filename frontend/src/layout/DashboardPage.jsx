import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";
import Dashboard from "../pages/Dashboard";
import Agent from "../pages/Agent";

export default function DashboardPage() {
  const path = window.location.pathname;

  return (
    <div style={{ display: "flex", background: "#0A0F1C" }}>
      <Sidebar />

      <div style={{ flex: 1 }}>
        <Topbar />

        {path === "/agent" ? <Agent /> : <Dashboard />}
      </div>
    </div>
  );
}