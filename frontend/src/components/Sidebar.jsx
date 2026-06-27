import { useState } from "react";

export default function Sidebar({ setView }) {

  const [active, setActive] = useState("dashboard");

  const menu = [
    { label: "Dashboard", key: "dashboard" },
    { label: "Executions", key: "executions" },
    { label: "Agent", key: "agent" },
    { label: "Policies", key: "policies" },
    { label: "Billing", key: "billing" },
    { label: "Settings", key: "settings" }
  ];

  const handleClick = (key) => {
    setActive(key);
    setView(key);
  };

  return (
    <div style={{
      width: 240,
      height: "100vh",
      background: "#0a0b10",
      borderRight: "1px solid rgba(255,255,255,0.05)",
      padding: 20,
      color: "white"
    }}>

      {/* LOGO */}
      <h2 style={{
        color: "#8b5cf6",
        marginBottom: 30,
        fontSize: 20
      }}>
        TrustOsAi
      </h2>

      {/* MENU */}
      {menu.map((item) => (
        <div
          key={item.key}
          onClick={() => handleClick(item.key)}
          style={{
            padding: "10px 12px",
            marginBottom: 8,
            borderRadius: 8,
            cursor: "pointer",
            background: active === item.key
              ? "rgba(139,92,246,0.2)"
              : "transparent",
            color: active === item.key ? "#fff" : "#aaa",
            transition: "0.2s"
          }}
        >
          {item.label}
        </div>
      ))}

    </div>
  );
}