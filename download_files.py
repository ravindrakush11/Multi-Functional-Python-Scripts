from flask import Flask, request, send_file, jsonify, abort, Response
import os
from flask_cors import CORS
from werkzeug.utils import secure_filename
import zipfile
import io

app = Flask(__name__)
CORS(app)

@app.route('/download-folder', methods=['GET'])
def download_folder():
    data = request.json
    folder_path = data.get('folder_path')
    folder_name = os.path.basename(folder_path.rstrip('/'))
    
    if not folder_path or not os.path.exists(folder_path):
        return jsonify({"error": "Invalid folder path"}), 400
    
    # Collect all file paths in the folder
    files = os.listdir(folder_path)
    print(files)
    
    # Create a ZIP file in memory
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for filename in files:
            file_path = os.path.join(folder_path, filename)
            if os.path.exists(file_path) and os.path.isfile(file_path):
                zf.write(file_path, filename)
    
    memory_file.seek(0)
    
    return send_file(
        memory_file,
        mimetype='application/zip',
        as_attachment=True,
        download_name=f'{folder_name}.zip'
    )

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)

