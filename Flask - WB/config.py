import os

class Config:
    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = ''
    JWT_SECRET_KEY = ''
    UPLOAD_FOLDER = 'uploads'
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB file size limit
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
