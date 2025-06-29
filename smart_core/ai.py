# AI-driven decision support for dispatchers
# Priority scoring and prediction logic

from .models import Event

def calculate_priority(event: Event) -> float:
    # Simple rule-based prioritization
    base_score = {
        'fire': 8,
        'medical': 9,
        'police': 7
    }[event.event_type.value]

    urgency_weight = event.historical_urgency * 1.5
    time_weight = 2 if 0 <= event.time_of_day <= 6 else 1
    weather_weight = 1.2 if event.weather.lower() in ['storm', 'rain'] else 1

    return round(base_score * urgency_weight * time_weight * weather_weight, 2)

def predict_next_busy_dispatcher(recent_events: list[Event]) -> str:
    from collections import Counter
    last_10 = list(recent_events)[-10:]
    count = Counter(e.event_type.value for e in last_10)
    return count.most_common(1)[0][0] if count else "none"