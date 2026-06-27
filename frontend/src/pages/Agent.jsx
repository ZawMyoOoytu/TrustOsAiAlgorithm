import { useState } from "react";
import ExecutionResultView from "../components/ExecutionResultView";

export default function Agent() {

  const [task, setTask] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // =========================
  // RUN AGENT
  // =========================
  const runAgent = async () => {

    if (!task.trim()) return;

    setLoading(true);
    setError(null);
    setResult(null);

    try {

      const res = await fetch("http://127.0.0.1:8000/api/agent/run", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          user_id: "frontend-user",
          task
        })
      });

      if (!res.ok) {
        throw new Error("Backend request failed");
      }

      const data = await res.json();

      console.log("Agent response:", data);

      setResult(data);

    } catch (err) {
      setError(err.message);
    }

    setLoading(false);
  };

  // =========================
  // UI
  // =========================
  return (
    <div style={{ padding: 20, color: "white" }}>

      <h2>Agent Execution</h2>

      {/* INPUT BOX */}
      <div style={{
        background: "#111827",
        padding: 15,
        borderRadius: 10,
        width: 500
      }}>

        <input
          value={task}
          onChange={(e) => setTask(e.target.value)}
          placeholder="Enter task (e.g. write website)"
          style={{
            width: "100%",
            padding: 10,
            borderRadius: 6,
            border: "1px solid #333",
            outline: "none"
          }}
        />

        <button
          onClick={runAgent}
          disabled={loading}
          style={{
            marginTop: 10,
            padding: "10px 15px",
            background: loading ? "#444" : "#8b5cf6",
            color: "white",
            border: "none",
            borderRadius: 6,
            cursor: "pointer"
          }}
        >
          {loading ? "Running..." : "Execute"}
        </button>

      </div>

      {/* ERROR */}
      {error && (
        <div style={{ color: "red", marginTop: 10 }}>
          {error}
        </div>
      )}

      {/* RESULT VIEW */}
      <div style={{ marginTop: 20 }}>

        <ExecutionResultView result={result?.result} />

      </div>

    </div>
  );
}