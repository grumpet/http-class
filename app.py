from flask import Flask, request, jsonify, render_template, send_from_directory,make_response
import os
from ftplib import FTP
app = Flask(__name__)

# In-memory data structure to simulate a database
data = {}

UPLOAD_FOLDER = 'uploads'



if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
    
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return 'File uploaded successfully', 201


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html',data=data, files=files)

@app.route('/resource', methods=['GET', 'POST', 'PUT', 'DELETE','PATCH','OPTIONS','HEAD'])
def resource():
    
    if request.method == 'GET':
        return jsonify(data)
    
    elif request.method == 'HEAD':
        response = make_response('', 204)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    elif request.method == 'PATCH':
        patch_data = request.get_json()
        for key, value in patch_data.items():
            if key in data:
                data[key] = value
        return jsonify(patch_data)
    
    elif request.method == 'OPTIONS':
        response = make_response('', 204)
        response.headers['Allow'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD'
        return response
    
    elif request.method == 'POST':
        new_data = request.get_json()
        data.update(new_data)
        return jsonify(new_data), 201

    elif request.method == 'PUT':
        updated_data = request.get_json()
        for key, value in updated_data.items():
            if key in data:
                data[key] = value
        return jsonify(updated_data)

    elif request.method == 'DELETE':
        deleted_data = request.get_json()
        for key in deleted_data:
            if key in data:
                del data[key]
        return jsonify(deleted_data)

if __name__ == '__main__':
    app.run(debug=True)