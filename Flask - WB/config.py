import os

class Config:
    SECRET_KEY = '38f15f6d5e829dfae19c42b5f9a1174a35e8b38c5f13bbdfd9fcb2f27c4b0c2c'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/flask_db'
    JWT_SECRET_KEY = 'fb7635b21f7984b7238f42e37b1ae4799df5c3d8ed5b6a87a623aff918c7a4a2'
    UPLOAD_FOLDER = 'uploads'
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB file size limit
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
