import React from "react";

export default function Landing() {
  return (
    <div style={{ background: "#0A0F1C", color: "white", minHeight: "100vh" }}>

      {/* NAVBAR */}
      <div style={{
        display: "flex",
        justifyContent: "space-between",
        padding: "20px 40px",
        borderBottom: "1px solid rgba(255,255,255,0.05)"
      }}>
        <div style={{ fontWeight: "bold", color: "#00D4FF" }}>
          ⚡ TrustOS
        </div>

        <div style={{ display: "flex", gap: 20, opacity: 0.8 }}>
          <span>Features</span>
          <span>Pricing</span>
          <span>Docs</span>
          <span>About</span>
        </div>

        <div style={{ display: "flex", gap: 10 }}>
          <button style={{ background: "transparent", color: "white" }}>
            Login
          </button>
          <button style={{
            background: "#00D4FF",
            padding: "8px 16px",
            borderRadius: 8,
            border: "none"
          }}>
            Get Started Free
          </button>
        </div>
      </div>

      {/* HERO */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "1fr 1fr",
        padding: "80px 60px",
        gap: 40
      }}>

        {/* LEFT */}
        <div>
          <div style={{
            background: "rgba(0,212,255,0.1)",
            padding: "6px 12px",
            display: "inline-block",
            borderRadius: 20,
            color: "#00D4FF",
            fontSize: 12
          }}>
            AI-POWERED • SECURE • COMPLIANT
          </div>

          <h1 style={{ fontSize: 50, marginTop: 20 }}>
            Build <span style={{ color: "#00D4FF" }}>Trust</span>.<br />
            Ship Faster.
          </h1>

          <p style={{ opacity: 0.7, marginTop: 20 }}>
            TrustOS is your AI Control Plane for secure AI execution,
            policy enforcement, and compliance at scale.
          </p>

          <div style={{ marginTop: 30, display: "flex", gap: 15 }}>
            <button style={{
              background: "#00D4FF",
              padding: "12px 20px",
              borderRadius: 10,
              border: "none"
            }}>
              Get Started Free →
            </button>

            <button style={{
              background: "transparent",
              border: "1px solid rgba(255,255,255,0.2)",
              padding: "12px 20px",
              borderRadius: 10,
              color: "white"
            }}>
              View Docs
            </button>
          </div>
        </div>

        {/* RIGHT DASHBOARD PREVIEW */}
        <div style={{
          background: "#111827",
          borderRadius: 16,
          padding: 20,
          border: "1px solid rgba(255,255,255,0.05)"
        }}>

          <h3>Dashboard Overview</h3>

          <div style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: 10,
            marginTop: 20
          }}>
            <div style={cardStyle}>
              Requests<br /><b>1,240</b>
            </div>

            <div style={cardStyle}>
              Success Rate<br /><b>99.6%</b>
            </div>

            <div style={cardStyle}>
              Latency<br /><b>842ms</b>
            </div>

            <div style={cardStyle}>
              Tokens<br /><b>2.45M</b>
            </div>
          </div>

          <div style={{
            marginTop: 20,
            fontSize: 12,
            opacity: 0.7
          }}>
            Usage by Agent
          </div>

          <div style={{ marginTop: 10 }}>
            {["policy-enforcer", "rate-limiter", "auth-guard"].map((a, i) => (
              <div key={i} style={{
                display: "flex",
                justifyContent: "space-between",
                padding: "6px 0",
                borderBottom: "1px solid rgba(255,255,255,0.05)"
              }}>
                <span>{a}</span>
                <span>{Math.floor(Math.random() * 5000)}</span>
              </div>
            ))}
          </div>

        </div>

      </div>
    </div>
  );
}

const cardStyle = {
  background: "#0B1220",
  padding: 15,
  borderRadius: 10,
  border: "1px solid rgba(255,255,255,0.05)"
};