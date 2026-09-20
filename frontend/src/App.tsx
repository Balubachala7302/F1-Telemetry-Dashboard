import { useEffect, useState } from "react";
interface Telemetry {
  id: number;
  driver_id: number;
  lap_number: number;
  speed: number;
  throttle: number;
  brake: number;
  gear: number;
  rpm: number;
  lap_time: number;
}

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [telemetry, setTelemetry] = useState<Telemetry[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/telemetry/")
      .then((response) => response.json())
      .then((data) => {
        setTelemetry(data);
      })
      .catch((error) => {
        console.error("Error fetching telemetry:", error);
      });
  }, []);
  const handleAnalyze = async () => {
    if (!file) {
      alert("Please select a CSV file first.");
      return;
    }
    const formData = new FormData();
    formData.append("file", file)

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/telemetry/upload",
        {
          method: "POST",
          body: formData
        }
      );

      if (!response.ok) {
        throw new Error("Upload failed");
      }
      const result = await response.json();
      console.log("Upload successful:", result);
      const telemetryResponse = await fetch(
        "http://127.0.0.1:8000/telemetry/"
      );
      const data = await telemetryResponse.json();
      console.log("Telemetry data :", data);
      setTelemetry(data);
      alert("Telemetry uploaded successfully");
    }
    catch (error) {
      console.error("Error uploading telemetry:", error);
      alert(error instanceof Error ? error.message : String(error));
    }
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

        <section className="telemetry-card">
          <h2>Telemetry Data</h2>

          <p>Total Records: {telemetry.length}</p>

          <table>
            <thead>
              <tr>
                <th>Lap</th>
                <th>Speed</th>
                <th>Throttle</th>
                <th>Brake</th>
                <th>Gear</th>
                <th>RPM</th>
                <th>Lap Time</th>
              </tr>
            </thead>

            <tbody>
              {telemetry.map((data) => (
                <tr key={data.id}>
                  <td>{data.lap_number}</td>
                  <td>{data.speed}</td>
                  <td>{data.throttle}</td>
                  <td>{data.brake}</td>
                  <td>{data.gear}</td>
                  <td>{data.rpm}</td>
                  <td>{data.lap_time}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </main>
    </div>
  )
}

export default App