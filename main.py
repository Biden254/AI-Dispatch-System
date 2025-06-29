# main.py
# Main entry point for Smart Emergency Dispatch System (Flask + Async Backend)

from app import create_app
from app.backend_runner import run_backend

# Create Flask app instance
app = create_app()

if __name__ == "__main__":
    # Start the async coroutine backend (dispatchers + scheduler) in background
    run_backend()

    # Run Flask server (serves frontend + handles event API)
    app.run(debug=True, port=5000)
