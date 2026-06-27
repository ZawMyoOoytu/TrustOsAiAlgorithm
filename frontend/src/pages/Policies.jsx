import { useEffect, useState, useMemo } from "react";

export default function Policies() {

  const [executions, setExecutions] = useState([]);

  // =========================
  // FETCH EXECUTIONS
  // =========================
  useEffect(() => {

    const load = async () => {
      try {
        const res = await fetch("http://127.0.0.1:8000/api/executions");
        const data = await res.json();

        setExecutions(Array.isArray(data) ? data : []);

      } catch (err) {
        console.error(err);
        setExecutions([]);
      }
    };

    load();

  }, []);

  const safe = Array.isArray(executions) ? executions : [];

  // =========================
  // POLICY ANALYTICS
  // =========================
  const policyStats = useMemo(() => {

    const total = safe.length;

    const allowed = safe.filter(
      e => e.billing?.allowed === true
    ).length;

    const blocked = total - allowed;

    const lowRisk = safe.filter(
      e => e.policy?.risk_level === "low"
    ).length;

    const highRisk = total - lowRisk;

    return {
      total,
      allowed,
      blocked,
      lowRisk,
      highRisk
    };

  }, [safe]);

  // =========================
  // UI
  // =========================
  return (
    <div style={{ color: "white" }}>

      <h2>Policy Control Center</h2>

      {/* ================= STATS ================= */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(3, 1fr)",
        gap: 15,
        marginTop: 20
      }}>

        <Card title="Total Executions" value={policyStats.total} />
        <Card title="Allowed" value={policyStats.allowed} />
        <Card title="Blocked" value={policyStats.blocked} />

        <Card title="Low Risk" value={policyStats.lowRisk} />
        <Card title="High Risk" value={policyStats.highRisk} />
        <Card title="Policy Engine" value="Active" />

      </div>

      {/* ================= EXECUTION POLICY LIST ================= */}
      <div style={{
        marginTop: 30,
        background: "#0b0f1a",
        padding: 15,
        borderRadius: 10
      }}>

        <h3>Recent Policy Decisions</h3>

        {safe.slice(0, 10).map((e, i) => (
          <div key={i} style={{
            padding: 10,
            marginTop: 10,
            background: "#111827",
            borderRadius: 8
          }}>

            <div>
              <b>Status:</b> {e.status}
            </div>

            <div>
              <b>Risk:</b> {e.policy?.risk_level}
            </div>

            <div>
              <b>Allowed:</b>{" "}
              {e.billing?.allowed ? "YES" : "NO"}
            </div>

            {e.policy?.flags?.length > 0 && (
              <div style={{ color: "#f87171" }}>
                Flags: {e.policy.flags.join(", ")}
              </div>
            )}

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