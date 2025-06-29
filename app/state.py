from smart_core.dispatchers import Dispatcher
from smart_core.scheduler import Scheduler
from smart_core.models import Event
from collections import deque

dispatchers = {
    'fire': Dispatcher('fire'),
    'medical': Dispatcher('medical'),
    'police': Dispatcher('police')
}

event_log = deque()
recent_events = deque(maxlen=20)  # Store last 20 events

scheduler = Scheduler(dispatchers, event_log, recent_events)