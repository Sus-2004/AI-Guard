import { useState } from "react";
import axios from "axios";
import "./index.css";

export default function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);

  async function check() {
    const res = await axios.post("/api/check", { query });
    setResult(res.data);
  }

  return (
    <div className="container">
      <h1>AI Guard — SQL Injection Detector</h1>
      <textarea
        placeholder="Type SQL query..."
        value={query}
        onChange={e => setQuery(e.target.value)}
      />
      <button onClick={check}>Analyze</button>

      {result && (
        <div className={result ${result.label.toLowerCase()}}>
          <h2>{result.label}</h2>
          <p>{result.percentage}% confidence</p>
        </div>
      )}
    </div>
  );
}