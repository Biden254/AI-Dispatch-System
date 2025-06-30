# 🚨 Smart Emergency Dispatch System with AI and Coroutines

This project simulates a smart city emergency dispatch system using **Python coroutines** and **AI-based prioritization** to efficiently handle fire, medical, and police emergencies in real time.

## 🧠 Project Overview

Emergencies can occur unpredictably, and effective dispatching is critical for saving lives. This system models each dispatcher (fire, medical, and police) as a coroutine managing its own event queue. A central scheduler selects which event to process per time step based on AI-prioritized scores.

The system also includes predictive logic to anticipate future dispatcher load and recommend dynamic resource reallocation.

---

## ⚙️ Features

- **Asynchronous Dispatchers**  
  Each emergency service runs as a separate coroutine to process incoming events concurrently without blocking the system.

- **AI-Based Prioritization**  
  Events are scored using a rule-based model factoring:
  - Event type
  - Historical urgency
  - Proximity
  - Time of day

- **Scheduling Coroutine**  
  - Pulls the highest-priority event from all queues.
  - Ensures fairness and critical-response optimization.
  - Logs every dispatched event with metadata (type, priority, dispatcher, time).

- **Predictive Resource Allocation**  
  - Analyzes trends in event patterns.
  - Predicts dispatcher workload over the next 10 time steps.
  - Suggests unit repositioning to reduce delays in critical zones.

---

## 🛠️ Technologies Used

- Python 3
- Asyncio (for coroutine implementation)
- Custom AI rule-based priority scoring
- Simple time-series based prediction model
