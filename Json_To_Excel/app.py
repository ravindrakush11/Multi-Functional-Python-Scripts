from flask import Flask, request, send_file
import pandas as pd
import os
from tempfile import NamedTemporaryFile

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JSON to Excel Converter</title>
</head>
<body>
    <h1>JSON to Excel Converter</h1>
    <h2>Convert Folder:</h2>
    <input type="file" id="jsonFolder" multiple directory webkitdirectory>
    <button onclick="convertFolderToJson()">Convert Folder to Excel</button>
    <br><br>
    <h2>Convert Single File:</h2>
    <input type="file" id="jsonFile">
    <button onclick="convertFileToJson()">Convert File to Excel</button>

    <script>
        function convertFolderToJson() {
            const input = document.getElementById('jsonFolder');
            const files = input.files;
            const formData = new FormData();

            for (let i = 0; i < files.length; i++) {
                formData.append('jsonFiles', files[i]);
            }

            fetch('/convert_folder', {
                method: 'POST',
                body: formData
            })
            .then(response => response.blob())
            .then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'output.xlsx';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
            })
            .catch(error => console.error('Error:', error));
        }

        function convertFileToJson() {
            const input = document.getElementById('jsonFile');
            const file = input.files[0];
            const formData = new FormData();
            formData.append('jsonFile', file);

            fetch('/convert_file', {
                method: 'POST',
                body: formData
            })
            .then(response => response.blob())
            .then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'output.xlsx';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
            })
            .catch(error => console.error('Error:', error));
        }
    </script>
</body>
</html>'''

@app.route('/convert_folder', methods=['POST'])
def convert_folder_to_excel():
    uploaded_files = request.files.getlist('jsonFiles')
    all_data = []

    for file in uploaded_files:
        filename = file.filename
        if filename.endswith('.json'):
            data = pd.read_json(file)
            data['id'] = os.path.splitext(filename)[0].split('/')[-1]
            all_data.append(data)

    if all_data:
        json_data = pd.concat(all_data, ignore_index=True)
        with NamedTemporaryFile(delete=False) as tmp:
            excel_file = tmp.name + '.xlsx'
            json_data.to_excel(excel_file, index=False)
            return send_file(excel_file, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    else:
        return 'No JSON files found.'

@app.route('/convert_file', methods=['POST'])
def convert_file_to_excel():
    file = request.files['jsonFile']
    filename = file.filename
    if filename.endswith('.json'):
        data = pd.read_json(file)
        data['id'] = os.path.splitext(filename)[0]
        with NamedTemporaryFile(delete=False) as tmp:
            excel_file = tmp.name + '.xlsx'
            data.to_excel(excel_file, index=False)
            return send_file(excel_file, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    else:
        return 'Invalid file format. Please select a JSON file.'

if __name__ == '__main__':
    app.run(debug=True)