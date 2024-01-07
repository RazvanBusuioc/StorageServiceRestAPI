import json
import requests
from flask import Flask, request, Response
from flask_cors import CORS
from constants import REST_API_PORT, STORAGE_SERVICE_URL, DOWNLOAD_FILE_ENDPOINT, CREATE_FILE_ENDPOINT, UPDATE_FILE_ENDPOINT, DELETE_FILE_ENDPOINT, MATCH_FILE_ENDPOINT

app = Flask(__name__)
CORS(app)

@app.before_request
def handle_preflight():
    if request.method == 'OPTIONS':
        res = Response()
        res.headers['X-Content-Type-Options'] = '*'
        return res


@app.route('/api/read', methods=['GET'])
def download_file():
    parameters = {
        'fileName': request.args.get('fileName'),
        'storageType': 'CLOUD' if request.args.get('isCloud') else 'LOCAL',
    }
    resp = requests.get(STORAGE_SERVICE_URL + DOWNLOAD_FILE_ENDPOINT, json=parameters).content
    print('Response from Storage Service: ')
    print(resp)
    return resp


@app.route('/api/deleteFile', methods=['DELETE'])
def delete_file():
    parameters = {
        'fileName': request.args.get('fileName'),
        'storageType': 'CLOUD' if request.args.get('isCloud') else 'LOCAL',
    }
    resp = requests.delete(STORAGE_SERVICE_URL + DELETE_FILE_ENDPOINT, json=parameters).content
    print('Response from Storage Service: ')
    print(resp)
    return resp

@app.route('/api/update', methods=['POST'])
def update_file():
    multipart_form_data = {
        'upload': ('file', request.files['file']),
        'fileName': (None, request.form['fileName']),
        'storageType': (None, 'CLOUD' if request.form['isCloud'] else 'LOCAL')
    }
    resp = requests.post(STORAGE_SERVICE_URL + UPDATE_FILE_ENDPOINT, files=multipart_form_data).content
    print('Response from Storage Service: ')
    print(resp)
    return resp


@app.route('/api/create', methods=['POST'])
def create_file():
    multipart_form_data = {
        'upload': ('file', request.files['file']),
        'fileName': (None, request.form['fileName']),
        'storageType': (None, 'CLOUD' if request.form['isCloud'] else 'LOCAL')
    }
    resp = requests.post(STORAGE_SERVICE_URL + CREATE_FILE_ENDPOINT, files=multipart_form_data).content
    print('Response from Storage Service: ')
    print(resp)
    return resp


@app.route('/api/match-filename', methods=['GET'])
def get_files():
    parameters = {
        'regexp': request.args.get('regexp'),
        'storageType': 'CLOUD' if request.args.get('isCloud') else 'LOCAL',
    }
    resp = requests.get(STORAGE_SERVICE_URL + MATCH_FILE_ENDPOINT, json=parameters).content
    print('Response from Storage Service: ')
    print(resp)
    return resp


if __name__ == '__main__':
   app.run(port=REST_API_PORT)