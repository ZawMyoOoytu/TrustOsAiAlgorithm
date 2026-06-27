import { useEffect, useState, useMemo } from "react";

export default function Billing() {

  const [executions, setExecutions] = useState([]);

  // =========================
  // FETCH EXECUTIONS (reuse backend)
  // =========================
  useEffect(() => {

    const fetchData = async () => {

      try {
        const res = await fetch("http://127.0.0.1:8000/api/executions");
        const data = await res.json();

        setExecutions(Array.isArray(data) ? data : []);

      } catch (err) {
        console.error(err);
        setExecutions([]);
      }

    };

    fetchData();

  }, []);

  const safe = Array.isArray(executions) ? executions : [];

  // =========================
  // USAGE CALCULATION
  // =========================
  const usage = useMemo(() => {

    const totalRuns = safe.length;

    const totalRuntime = safe.reduce(
      (sum, e) => sum + (Number(e.runtime_ms) || 0),
      0
    );

    const avgRuntime = totalRuns ? totalRuntime / totalRuns : 0;

    const creditsUsed = totalRuns; // simple model

    const creditsLeft = Math.max(0, 10 - creditsUsed);

    return {
      totalRuns,
      totalRuntime,
      avgRuntime: avgRuntime.toFixed(0),
      creditsUsed,
      creditsLeft
    };

  }, [safe]);

  // =========================
  // UI
  // =========================
  return (
    <div style={{ color: "white" }}>

      <h2>Billing & Usage</h2>

      {/* ================= CARDS ================= */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(3, 1fr)",
        gap: 15,
        marginTop: 20
      }}>

        <Card title="Total Executions" value={usage.totalRuns} />
        <Card title="Credits Used" value={usage.creditsUsed} />
        <Card title="Credits Left" value={usage.creditsLeft} />

        <Card title="Total Runtime (ms)" value={usage.totalRuntime} />
        <Card title="Avg Runtime (ms)" value={usage.avgRuntime} />
        <Card title="System Status" value="Active" />

      </div>

      {/* ================= PLAN SECTION ================= */}
      <div style={{
        marginTop: 30,
        padding: 20,
        background: "#0b0f1a",
        borderRadius: 12
      }}>

        <h3>Current Plan</h3>

        <p style={{ opacity: 0.7 }}>
          Free Developer Tier
        </p>

        <p>
          Credits Remaining: <b>{usage.creditsLeft}</b>
        </p>

        <button style={{
          marginTop: 10,
          padding: "10px 15px",
          background: "#8b5cf6",
          color: "white",
          border: "none",
          borderRadius: 8,
          cursor: "pointer"
        }}>
          Upgrade Plan (Mock)
        </button>

      </div>

    </div>
  );
}

// =========================
// CARD COMPONENT
// =========================
function Card({ title, value }) {
  return (
    <div style={{
      background: "#111827",
      padding: 15,
      borderRadius: 10,
      border: "1px solid rgba(255,255,255,0.05)"
    }}>
      <div style={{ fontSize: 12, opacity: 0.7 }}>{title}</div>
      <div style={{ fontSize: 20, marginTop: 5 }}>{value}</div>
    </div>
  );
}