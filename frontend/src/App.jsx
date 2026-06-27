import { useState } from "react";

import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";

import Dashboard from "./pages/Dashboard";
import Agent from "./pages/Agent";
import Executions from "./pages/Executions";
import Billing from "./pages/Billing";
import Policies from "./pages/Policies";
import Pricing from "./pages/Pricing";

export default function App() {

  const [view, setView] = useState("dashboard");

  // =========================
  // VIEW ROUTER
  // =========================
  const renderView = () => {

    switch (view) {

      case "dashboard":
        return <Dashboard />;

      case "agent":
        return <Agent />;

      case "executions":
        return <Executions />;

      case "billing":
        return <Billing />;

      case "policies":
        return <Policies />;

      case "pricing":
        return <Pricing />;

      case "features":
        return (
          <div style={{ color: "white" }}>
            Features Page (coming soon)
          </div>
        );

      case "docs":
        return (
          <div style={{ color: "white" }}>
            Docs Page (coming soon)
          </div>
        );

      case "about":
        return (
          <div style={{ color: "white" }}>
            About Page (coming soon)
          </div>
        );

      case "settings":
        return (
          <div style={{ color: "white" }}>
            Settings Page (coming soon)
          </div>
        );

      default:
        return <Dashboard />;
    }
  };

  return (
    <div style={{
      display: "flex",
      minHeight: "100vh",
      background: "#05060a",
      color: "white"
    }}>

      {/* ================= SIDEBAR ================= */}
      <Sidebar setView={setView} />

      {/* ================= MAIN AREA ================= */}
      <div style={{
        flex: 1,
        padding: 20,
        overflow: "auto"
      }}>

        {/* TOPBAR (optional global) */}
        <Topbar onSearch={(q) => console.log("search:", q)} />

        {/* PAGE VIEW */}
        {renderView()}

      </div>

    </div>
  );
}