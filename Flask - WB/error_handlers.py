def handle_errors(app):
    # Handle 400 Bad Request errors
    @app.errorhandler(400)
    def bad_request(error):
        return {"error": "Bad Request", "message": str(error)}, 400

    # Handle 401 Unauthorized errors
    @app.errorhandler(401)
    def unauthorized(error):
        return {"error": "Unauthorized", "message": str(error)}, 401

    # Handle 404 Not Found errors
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Not Found", "message": str(error)}, 404

    # Handle 500 Internal Server Error
    @app.errorhandler(500)
    def server_error(error):
        return {"error": "Internal Server Error", "message": str(error)}, 500
