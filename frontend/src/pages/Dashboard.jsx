import { useEffect, useMemo, useState } from "react";

export default function Dashboard() {

  // =========================
  // STATE
  // =========================
  const [executions, setExecutions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // =========================
  // FETCH EXECUTIONS
  // =========================
  useEffect(() => {

    const loadExecutions = async () => {

      try {
        setLoading(true);

        const res = await fetch("http://127.0.0.1:8000/api/executions");

        const data = await res.json();

        setExecutions(Array.isArray(data) ? data : []);

        setError(null);

      } catch (err) {
        console.error(err);
        setError(err.message);
        setExecutions([]);
      } finally {
        setLoading(false);
      }

    };

    loadExecutions();

  }, []);

  // =========================
  // SAFE ARRAY
  // =========================
  const safe = Array.isArray(executions) ? executions : [];

  // =========================
  // STATS
  // =========================
  const stats = useMemo(() => {

    const total = safe.length;

    const success = safe.filter(e => e.status === "completed").length;

    const successRate = total ? (success / total) * 100 : 0;

    const avgLatency =
      safe.reduce((sum, e) => sum + (Number(e.runtime_ms) || 0), 0) /
      (total || 1);

    return {
      total,
      successRate: successRate.toFixed(1),
      avgLatency: avgLatency.toFixed(0)
    };

  }, [safe]);

  // =========================
  // UI
  // =========================
  return (
    <div style={{ color: "white" }}>

      {/* ================= HEADER ================= */}
      <div style={{ marginBottom: 20 }}>
        <h2>Dashboard</h2>
        <p style={{ opacity: 0.6 }}>
          AI execution + policy control + usage metering system
        </p>
      </div>

      {/* ================= LOADING ================= */}
      {loading && (
        <div style={{ opacity: 0.7 }}>
          Loading executions...
        </div>
      )}

      {/* ================= ERROR ================= */}
      {error && (
        <div style={{ color: "red" }}>
          Error: {error}
        </div>
      )}

      {/* ================= STATS CARDS ================= */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(3, 1fr)",
        gap: 15,
        marginTop: 20
      }}>

        <Card title="Total Executions" value={stats.total} />
        <Card title="Success Rate" value={`${stats.successRate}%`} />
        <Card title="Avg Latency" value={`${stats.avgLatency} ms`} />

      </div>

      {/* ================= EXECUTIONS LIST ================= */}
      <div style={{
        marginTop: 20,
        background: "#0b0f1a",
        padding: 15,
        borderRadius: 12,
        maxHeight: 500,
        overflowY: "auto"
      }}>

        <h3>Recent Executions</h3>

        {safe.length === 0 && !loading && (
          <p style={{ opacity: 0.6 }}>No executions found</p>
        )}

        {safe.map((e, i) => (
          <div key={i} style={{
            marginTop: 10,
            padding: 10,
            background: "#111827",
            borderRadius: 8,
            border: "1px solid rgba(255,255,255,0.05)"
          }}>

            <div><b>Status:</b> {e.status}</div>
            <div><b>Trust:</b> {e.trust_score}</div>
            <div><b>Runtime:</b> {e.runtime_ms} ms</div>

            <div style={{ fontSize: 12, opacity: 0.6, marginTop: 5 }}>
              {e.task || "No task"}
            </div>

          </div>
        ))}

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