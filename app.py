from flask import Flask, jsonify


def create_app():
    """Flask application factory.

    Returns a Flask app with a single route `/` that returns JSON.
    """
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return jsonify(message="Hello, World!")

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=True)
