# Data models for emergency incidents
# Event dataclasses or structures

from dataclasses import dataclass
from enum import Enum
import time

class EventType(Enum):
    FIRE = 'fire'
    MEDICAL = 'medical'
    POLICE = 'police'

@dataclass
class Event:
    event_type: EventType
    location: str
    time_of_day: int  # 0-23
    weather: str
    historical_urgency: int  # 1 to 10
    timestamp: float = time.time()
    priority: float = 0.0  # To be assigned later