from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    # Define columns for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)

    def set_password(self, password):
        # Hash and store the password
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        # Hash and store the password
        return check_password_hash(self.password_hash, password)
