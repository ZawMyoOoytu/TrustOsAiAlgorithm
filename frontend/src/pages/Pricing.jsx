export default function Pricing() {

  const plans = [
    {
      name: "Free",
      price: "$0",
      desc: "For testing & development",
      features: [
        "100 executions",
        "Basic AI agent",
        "Community support"
      ]
    },
    {
      name: "Pro",
      price: "$19",
      desc: "For developers & startups",
      features: [
        "10,000 executions",
        "Policy control system",
        "Billing & usage tracking",
        "Priority support"
      ]
    },
    {
      name: "Enterprise",
      price: "$99",
      desc: "For scale & production",
      features: [
        "Unlimited executions",
        "Advanced policy engine",
        "Custom billing rules",
        "Dedicated support"
      ]
    }
  ];

  return (
    <div style={{ color: "white" }}>

      <h2>Pricing Plans</h2>

      <p style={{ opacity: 0.7 }}>
        Choose a plan that fits your AI execution system
      </p>

      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(3, 1fr)",
        gap: 20,
        marginTop: 30
      }}>

        {plans.map((plan, i) => (
          <div key={i} style={{
            background: "#0b0f1a",
            padding: 20,
            borderRadius: 12,
            border: "1px solid rgba(255,255,255,0.05)"
          }}>

            <h3>{plan.name}</h3>
            <h1 style={{ color: "#8b5cf6" }}>{plan.price}</h1>
            <p style={{ opacity: 0.7 }}>{plan.desc}</p>

            <ul style={{ marginTop: 15 }}>
              {plan.features.map((f, idx) => (
                <li key={idx} style={{ marginBottom: 6 }}>
                  {f}
                </li>
              ))}
            </ul>

            <button style={{
              marginTop: 15,
              width: "100%",
              padding: "10px",
              background: "#8b5cf6",
              border: "none",
              color: "white",
              borderRadius: 8,
              cursor: "pointer"
            }}>
              Get Started
            </button>

          </div>
        ))}

      </div>

    </div>
  );
}