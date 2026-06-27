import { useState } from "react";

export default function Topbar({ onSearch }) {

  const [query, setQuery] = useState("");

  const handleSearch = (value) => {
    setQuery(value);
    onSearch?.(value);
  };

  const navItems = [
    { label: "Features" },
    { label: "Pricing" },
    { label: "Docs" },
    { label: "About" }
  ];

  return (
    <div style={{
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      padding: "12px 16px",
      background: "rgba(255,255,255,0.03)",
      border: "1px solid rgba(255,255,255,0.05)",
      borderRadius: 12,
      color: "white",
      gap: 20
    }}>

      {/* ================= LEFT: SEARCH ================= */}
      <input
        value={query}
        onChange={(e) => handleSearch(e.target.value)}
        placeholder="Search executions..."
        style={{
          flex: 1,
          padding: "8px 10px",
          background: "transparent",
          border: "1px solid rgba(255,255,255,0.1)",
          borderRadius: 8,
          color: "white",
          outline: "none"
        }}
      />

      {/* ================= CENTER NAV ================= */}
      <div style={{
        display: "flex",
        gap: 18,
        alignItems: "center",
        fontSize: 14,
        opacity: 0.9
      }}>
        {navItems.map((item) => (
          <div
            key={item.label}
            style={{
              cursor: "pointer",
              padding: "6px 8px",
              borderRadius: 6,
              transition: "0.2s"
            }}
            onMouseEnter={(e) =>
              e.currentTarget.style.background = "rgba(139,92,246,0.15)"
            }
            onMouseLeave={(e) =>
              e.currentTarget.style.background = "transparent"
            }
          >
            {item.label}
          </div>
        ))}
      </div>

      {/* ================= RIGHT AUTH ================= */}
      <div style={{
        display: "flex",
        gap: 10,
        alignItems: "center"
      }}>

        {/* LOGIN */}
        <button style={{
          padding: "6px 12px",
          background: "transparent",
          border: "1px solid rgba(255,255,255,0.2)",
          color: "white",
          borderRadius: 8,
          cursor: "pointer"
        }}>
          Log In
        </button>

        {/* START FREE */}
        <button style={{
          padding: "6px 12px",
          background: "#8b5cf6",
          border: "none",
          color: "white",
          borderRadius: 8,
          cursor: "pointer",
          fontWeight: "bold"
        }}>
          Start Free
        </button>

      </div>

    </div>
  );
}