import Sidebar from "./Sidebar";

export default function MainLayout({ children }) {
  return (
    <div style={{ display: "flex" }}>
      <Sidebar />

      <div style={{
        marginLeft: 220,
        width: "100%",
        minHeight: "100vh",
        background: "#05060a",
        color: "white"
      }}>
        {children}
      </div>
    </div>
  );
}