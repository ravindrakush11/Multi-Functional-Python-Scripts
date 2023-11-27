from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Define the directory where uploaded files will be stored temporarily.
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allow only PDF file uploads.
ALLOWED_EXTENSIONS = {'pdf'}

# Function to check if the file extension is allowed.
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/answer', methods=['POST'])
def upload_pdf():
    # # Check if a file was included in the POST request.
    # if 'file' not in request.files:
    #     return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # Check if the file has a valid file extension (PDF).
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file format. Only PDF files are allowed.'}), 400

    # Create a secure filename and save the file to the upload folder.
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # You can perform further processing on the uploaded PDF file here.
    # For example, extract text, parse content, etc.

    return jsonify({'message': 'File uploaded successfully'})

if __name__ == '__main__':
    app.run(debug=True)
