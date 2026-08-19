function App() {
  return (
    <div>
      <h1>F1 Telemetry Dashboard</h1>
      <p>Welcome to the F1 Telemetry Dashboard</p>
      <p>Analyze and Visualize Formula 1 Telemetry data</p>
      <header>
        <main className="main-content">
          <section className="upload-card">
            <h2>Upload Telemetry Data</h2>
            <p>
              Upload your telemetry file to start analyzing the session
            </p>
            <input type="file" accept=".csv" />
            <button>Upload & Analyze</button>
          </section>
        </main>
      </header>
    </div>
  )
}

export default App
