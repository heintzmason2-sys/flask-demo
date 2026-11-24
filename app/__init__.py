from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        return "Hello, Mason!"

    return app

    @app.get("/health")
    def health():
        return {"status": "ok"}
