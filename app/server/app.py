from flask import Flask 
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app

if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=False)