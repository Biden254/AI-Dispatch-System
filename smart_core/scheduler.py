# Coroutine for scheduling emergency dispatch
# Central scheduler to manage event dispatching


import asyncio
from .ai import calculate_priority, predict_next_busy_dispatcher
from .logger import log_event
from .dispatchers import Dispatcher
from .models import Event, EventType
#from app.state import recent_events  

class Scheduler:
    def __init__(self, dispatchers, event_log, recent_event_list):
        self.dispatchers = dispatchers
        self.event_log = event_log
        self.recent_events = recent_event_list

    async def run(self):
        while True:
            # Gather all events
            all_events = []
            for d in self.dispatchers.values():
                if d.queue:
                    all_events.append(d.queue[0])  # Peek only

            if all_events:
                # Pick highest priority
                highest = max(all_events, key=lambda e: e.priority)
                for name, disp in self.dispatchers.items():
                    if disp.queue and disp.queue[0] == highest:
                        disp.queue.popleft()
                        log_event(name, highest)  # Logs to console and shared log
                        self.recent_events.append(highest)
                        break

            # Predictive suggestion
            busiest = predict_next_busy_dispatcher(self.recent_events)
            if busiest != "none":
                print(f"[PREDICTOR] Suggest: Position more units for {busiest.upper()} incidents.")

            await asyncio.sleep(1)  # Simulated time step