from flask import Blueprint, request, jsonify, current_app
import os
from werkzeug.utils import secure_filename

admin_bp = Blueprint('admin_bp', __name__)

# Function to check if file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@admin_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400

    # Check file size limit
    if len(file.read()) > current_app.config['MAX_FILE_SIZE']:
        return jsonify({"error": "File size exceeds limit"}), 400
    file.seek(0)  # Reset file pointer after size check

    # Secure and save the uploaded file
    filename = secure_filename(file.filename)
    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(upload_path)
    
    return jsonify({"message": "File uploaded successfully"}), 200
