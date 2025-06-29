# logger.py
# Logging utilities for the dispatch system

import time
from dataclasses import asdict

def log_event(dispatcher_name, event):
    # Import inside the function to avoid circular import
    from app.state import event_log
    print("log_event called!")  # Debug
    
    # Console log (for debugging)
    print(f"[LOG] {time.strftime('%H:%M:%S')} | Dispatcher: {dispatcher_name.upper()} | "
          f"Event: {event.event_type.value} | Priority: {event.priority} | Location: {event.location}")

    # Save structured event data to shared memory (used by /api/logs and /api/export)
    event_data = asdict(event)
    event_data["dispatcher"] = dispatcher_name
    event_log.append(event_data)
