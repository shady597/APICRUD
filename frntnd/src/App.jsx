import { useState } from "react";

const BASE_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000/users/";

export default function CreateUser() {
  const [form, setForm]     = useState({ name: "", email: "" });
  const [loading, setLoading] = useState(false);
  const [error, setError]   = useState(null);
  const [success, setSuccess] = useState(null);

  function handleChange(e) {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setSuccess(null);

    try {
      const res = await fetch(`${BASE_URL}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        throw new Error(data.detail ?? `Error ${res.status}`);
      }

      const user = await res.json();
      setSuccess(user);
      setForm({ name: "", email: "" });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
      console.log("Request completed");
    }
  }

  return (
    <div style={{ maxWidth: 400, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h2>Create User</h2>

      <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
        <input
          name="name"
          placeholder="Full name"
          value={form.name}
          onChange={handleChange}
          style={inputStyle}
        />
        <input
          name="email"
          type="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
          style={inputStyle}
        />
        <button onClick={handleSubmit} disabled={loading} style={btnStyle}>
          {loading ? "Creating…" : "Create User"}
        </button>
      </div>

      {error   && <p style={{ color: "red",   marginTop: 12 }}>{error}</p>}
      {success && <p style={{ color: "green", marginTop: 12 }}>User <strong>{success.name}</strong> created!</p>}
    </div>
  );
}

const inputStyle = {
  padding: "8px 12px",
  fontSize: 14,
  border: "1px solid #ccc",
  borderRadius: 6,
};

const btnStyle = {
  padding: "9px 16px",
  fontSize: 14,
  background: "#111",
  color: "#fff",
  border: "none",
  borderRadius: 6,
  cursor: "pointer",
};