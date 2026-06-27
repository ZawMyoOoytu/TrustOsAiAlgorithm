export default function StatCard({ title, value }) {
  return (
    <div className="glass neon" style={{ padding: "15px" }}>
      <p style={{ opacity: 0.7 }}>{title}</p>
      <h2>{value}</h2>
    </div>
  );
}