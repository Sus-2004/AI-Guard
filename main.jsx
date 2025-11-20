function App() {
    const [query, setQuery] = React.useState("");
    const [result, setResult] = React.useState(null);
    const [percentage, setPercentage] = React.useState(null);

    const analyzeQuery = async () => {
        if (query.trim() === "") {
            alert("Please enter a SQL query.");
            return;
        }

        const response = await fetch("http://localhost:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ query }),
        });

        const data = await response.json();
        setResult(data.status);
        setPercentage(data.percentage);
    };

    return (
        <div className="card">
            <h2>AI Guard — SQL Injection Detector</h2>
            <p>Enter a SQL query to check if it is safe or unsafe.</p>

            <textarea
                placeholder="Enter SQL query here..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />

            <button onClick={analyzeQuery}>Analyze</button>

            {result && (
                <div style={{ marginTop: "20px" }}>
                    <h3 className={result === "safe" ? "result-safe" : "result-unsafe"}>
                        {result === "safe" ? "✔ Safe Query" : "✘ Unsafe Query"}
                    </h3>
                    {percentage !== null && (
                        <p>Confidence: <b>{percentage}%</b></p>
                    )}
                </div>
            )}
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById("root"));