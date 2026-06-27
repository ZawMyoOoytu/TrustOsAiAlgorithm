import { useState } from "react";

async function runAgent(task) {
  const res = await fetch("http://127.0.0.1:8000/api/agent/run", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      task,
      user_id: "frontend-user"
    })
  });

  return await res.json();
}

export default function Agent() {

  const [task, setTask] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const execute = async () => {
    setLoading(true);
    const data = await runAgent(task);
    setResult(data);
    setLoading(false);
  };

  return (
    <div style={{ color: "white" }}>

      {/* EXECUTION BOX */}
      <div style={{
        background: "#111827",
        padding: 20,
        borderRadius: 10,
        width: 450
      }}>
        <h3>AI Agent</h3>

        <input
          value={task}
          onChange={(e) => setTask(e.target.value)}
          style={{ width: "100%", padding: 10 }}
        />

        <button onClick={execute} style={{ marginTop: 10 }}>
          {loading ? "Running..." : "Execute"}
        </button>
      </div>

      {/* RESULT */}
      <pre style={{ marginTop: 20 }}>
        {result ? JSON.stringify(result, null, 2) : "No result"}
      </pre>

    </div>
  );
}