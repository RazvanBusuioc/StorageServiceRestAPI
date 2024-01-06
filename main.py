import json
from flask import Flask, jsonify, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        res = Response()
        res.headers['X-Content-Type-Options'] = '*'
        return res


@app.route('/api/read', methods=['GET'])
def download_file():
    fileName = request.args.get("fileName")
    isCloud = request.args.get("isCloud")
    return jsonify({ 'error': 'No such file'}), 404


@app.route('/api/match-filename', methods=['GET'])
def get_files():
    fileName = request.args.get("fileName")
    isCloud = request.args.get("isCloud")
    return jsonify({ 'error': 'No such file'}), 404


@app.route('/api/deleteFile', methods=['DELETE'])
def delete_file():
    fileName = request.args.get("fileName")
    isCloud = request.args.get("isCloud")
    print(isCloud)
    return jsonify({ 'error': 'No such file'}), 404


@app.route('/api/update', methods=['POST'])
def update_file():
    fileName = request.form['fileName']
    file = request.files['file'] 
    return "Success"


@app.route('/api/create', methods=['POST'])
def create_file():
    fileName = request.form['fileName']
    file = request.files['file'] 
    return "Success"

if __name__ == '__main__':
   app.run(port=3000)