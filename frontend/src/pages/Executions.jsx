import { useEffect, useState } from "react";

export default function Executions() {
  const [executions, setExecutions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/executions")
      .then(res => res.json())
      .then(data => {
        console.log("EXECUTIONS:", data);

        // IMPORTANT FIX (data is array, not object)
        setExecutions(Array.isArray(data) ? data : []);
      })
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h2>Executions (Live)</h2>

      {executions.length === 0 ? (
        <p>No executions found</p>
      ) : (
        executions.map((ex) => (
          <div key={ex.execution_id}>
            <p>Status: {ex.status}</p>
            <p>Trust: {ex.trust_score}</p>
            <p>Runtime: {ex.runtime_ms} ms</p>
            <p>Task: {ex.task}</p>
          </div>
        ))
      )}
    </div>
  );
}