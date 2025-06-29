from flask import Flask, send_from_directory
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__, static_folder="../static", static_url_path="/")
    CORS(app)

    from .routes import api
    app.register_blueprint(api)

    # Route root URL to frontend
    @app.route("/")
    def serve_index():
        return app.send_static_file("index.html")

    return app