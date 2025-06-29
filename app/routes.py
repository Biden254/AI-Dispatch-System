from flask import Blueprint, request, jsonify, Response
from smart_core.models import Event, EventType
from smart_core.ai import calculate_priority, predict_next_busy_dispatcher
from app.state import dispatchers, event_log, recent_events
import csv
import io

api = Blueprint("api", __name__)

@api.route("/api/event", methods=["POST"])
def add_event():
    data = request.json
    try:
        event = Event(
            event_type=EventType(data["event_type"]),
            location=data["location"],
            time_of_day=int(data["time_of_day"]),
            weather=data["weather"],
            historical_urgency=int(data["historical_urgency"]),
        )
        event.priority = calculate_priority(event)
        dispatchers[data["event_type"]].queue.append(event)
        return jsonify({"status": "success", "priority": event.priority}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@api.route("/api/logs", methods=["GET"])
def get_logs():
    return jsonify(list(event_log)), 200

@api.route("/api/prediction", methods=["GET"])
def get_prediction():
    pred = predict_next_busy_dispatcher(list(recent_events))
    return jsonify({"predict": pred}), 200

@api.route("/api/export", methods=["GET"])
def export_logs_csv():
    if not event_log:
        return jsonify({"error": "No logs available"}), 404

    # Convert to CSV
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=event_log[0].keys())
    writer.writeheader()
    writer.writerows(event_log)

    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={"Content-Disposition": "attachment;filename=dispatch_logs.csv"}
    )
