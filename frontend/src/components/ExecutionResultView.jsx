export default function ExecutionResultView({ result }) {

  if (!result) return <p>No result</p>;

  return (
    <div style={{
      background: "#0b0f1a",
      padding: 15,
      borderRadius: 10,
      color: "white"
    }}>

      <h3>{result.title}</h3>
      <p>{result.description}</p>

      {/* FILES */}
      {result.files && result.files.map((file, i) => (
        <div key={i} style={{
          marginTop: 10,
          padding: 10,
          background: "#111827",
          borderRadius: 8
        }}>
          <strong>{file.name}</strong>

          <pre style={{
            whiteSpace: "pre-wrap",
            fontSize: 12
          }}>
            {file.content}
          </pre>
        </div>
      ))}

      {/* STEPS */}
      {result.steps && (
        <div style={{ marginTop: 10 }}>
          <h4>Steps</h4>
          <ul>
            {result.steps.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>
        </div>
      )}

    </div>
  );
}