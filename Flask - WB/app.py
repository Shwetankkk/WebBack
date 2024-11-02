from flask import Flask,jsonify
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Importing necessary modules and avoid circular imports
from extensions import db  # Import only db here
from auth import auth_bp
from public_routes import public_bp
import admin_routes  # Avoids circular import

load_dotenv()   # Load environment variables from .env file

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configurations

    # Initialize extensions with app
    db.init_app(app)
    jwt = JWTManager(app)
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_routes.admin_bp)  # Register admin_bp here
    
    @app.route('/')  # Define the route for the root URL
    def home():
        print("Welcome to the Flask server!")  # Print message to console
        return """
        <html>
        <head>
            <style>
                body {
                    background-color: black;  
                    color: orange;  
                    font-family: 'Imperial', sans-serif;  
                    display: flex; 
                    justify-content: center; 
                    align-items: center;
                    height: 100vh; 
                    margin: 0; 
                }
                h1 {
                    text-align: center;  
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Web Backend Mid Semester Project!<br> Head over to Postman to test the project.</h1>
            
        </body>
        </html>
        """  

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    
