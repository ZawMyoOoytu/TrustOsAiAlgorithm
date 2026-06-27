export async function fetchExecutions() {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/executions");

    if (!res.ok) {
      throw new Error("Failed to fetch executions");
    }

    const data = await res.json();

    // 🔥 SAFE GUARANTEE
    return Array.isArray(data) ? data : [];

  } catch (err) {
    console.error("fetchExecutions error:", err);
    return [];
  }
}