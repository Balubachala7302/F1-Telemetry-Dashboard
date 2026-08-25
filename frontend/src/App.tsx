import { useState } from "react";

function App() {
  const [file, setFile] = useState<File | null>(null);
  const handleAnalyze = () => {
    console.log(file);
  };
  return (
    <div className="dashboard">
      <header className="header">
        <h1>F1 Telemetry Dashboard</h1>
        <p>Welcome to the F1 Telemetry Dashboard</p>
        <p>Analyze and Visualize Formula 1 Telemetry data</p>
      </header>

      <main className="main-content">
        <section className="upload-card">
          <h2>Upload Telemetry Data</h2>

          <p>
            Upload your telemetry file to start analyzing the session
          </p>

          <input
            type="file"
            accept=".csv"
            onChange={(event) =>
              setFile(event.target.files?.[0] ?? null)
            }
          />

          {file && <p>Selected file: {file.name}</p>}

          <button onClick={handleAnalyze}>Upload & Analyze</button>
        </section>
      </main>
    </div>
  )
}

export default App