// static/script.js

const form = document.getElementById('eventForm');
const logsDiv = document.getElementById('logs');
const predictionDiv = document.getElementById('prediction');

const API_BASE = 'http://localhost:5000/api';

// Submit new event to backend
form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const payload = Object.fromEntries(formData.entries());
  payload.historical_urgency = parseInt(payload.historical_urgency);
  payload.time_of_day = parseInt(payload.time_of_day);

  try {
    const response = await fetch(`${API_BASE}/event`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    if (response.ok) {
      addLocalLog(`Event sent: ${payload.event_type} → Priority: ${data.priority}`);
    } else {
      addLocalLog(`Error: ${data.error}`);
    }
  } catch (err) {
    addLocalLog(`Network Error: ${err.message}`);
  }
});

// Local client-side log (UI-only, not from server)
function addLocalLog(message) {
  const logItem = document.createElement('div');
  logItem.textContent = `[${new Date().toLocaleTimeString()}] ${message}`;
  logItem.style.color = 'gray';
  logsDiv.prepend(logItem);
}

// Fetch logs from backend every 3s
async function fetchLogs() {
  try {
    const res = await fetch(`${API_BASE}/logs`);
    const logs = await res.json();

    logsDiv.innerHTML = ''; // Clear existing
    logs.reverse().forEach(log => {
      const logItem = document.createElement('div');
      const time = new Date(log.timestamp * 1000).toLocaleTimeString();
      const type = log.event_type.toLowerCase();
      const symbol = type === 'fire' ? '🔥' : type === 'medical' ? '🏥' : '🚓';
      const color = type === 'fire' ? 'red' : type === 'medical' ? 'blue' : 'green';

      logItem.innerHTML = `[${time}] ${symbol} <strong>${type.toUpperCase()}</strong> → Priority: ${log.priority} @ ${log.location}`;
      logItem.style.color = color;
      logsDiv.appendChild(logItem);
    });
  } catch (err) {
    console.error("Log fetch error:", err);
  }
}

// Fetch prediction every 3s
async function updatePrediction() {
  try {
    const res = await fetch(`${API_BASE}/prediction`);
    const data = await res.json();
    predictionDiv.textContent = `Suggest placing more units for: ${data.predict.toUpperCase()}`;
  } catch (err) {
    predictionDiv.textContent = 'Error getting prediction';
  }
}

// Auto-refresh every 3 seconds
setInterval(() => {
  fetchLogs();
  updatePrediction();
}, 3000);

// Initial load
fetchLogs();
updatePrediction();
