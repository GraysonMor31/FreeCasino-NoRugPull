from flask import jsonify

def register_routes(app):

    @app.route("/")
    def hello():
        return "Hello from Flask running on localhost!"

    @app.route("/api/health")
    def health_check():
        return jsonify({
            "status": "200, OK",
            "message": "Server is healthy",
            "environment": "local"
        })
