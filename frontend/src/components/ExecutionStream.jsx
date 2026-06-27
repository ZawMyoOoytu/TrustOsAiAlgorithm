import useExecutionStream from "../hooks/useExecutionStream";
import "../styles/execution-stream.css";
import ExecutionTimeline from "./ExecutionTimeline";

export default function ExecutionStream({ executionId }) {
  const { logs, status, trustScore } =
    useExecutionStream(executionId);

  return (
    <div className="stream-container">

      {/* HEADER */}
      <div className="stream-header">
        <h2>Execution Stream</h2>

        <div style={{ display: "flex", gap: 10 }}>
          <div className={`status ${status}`}>
            {status}
          </div>

          <div className="trust">
            Trust: {trustScore}
          </div>
        </div>
      </div>

      {/* LOG STREAM */}
      <div className="log-box">

        {logs.length === 0 ? (
          <p style={{ opacity: 0.5 }}>
            Waiting for execution...
          </p>
        ) : (
          logs.map((log, i) => (
            <div
              key={i}
              className={`log-line ${log.type}`}
            >
              <span className="dot"></span>
              {log.message}
            </div>
          ))
        )}

      </div>

      {/* TIMELINE VIEW (NEW) */}
      <ExecutionTimeline logs={logs} />

    </div>
  );
}