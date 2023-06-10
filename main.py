import json
from flask import Flask, jsonify
from flask import request
from deepface import DeepFace
app = Flask(__name__)
file_path = 'Test_Data\\new_face.jpg'
@app.route('/upload', methods =['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['face']
        print(f)
        f.save(file_path)
        emotion  = DeepFace.analyze(file_path,actions =['emotion'])[0]['dominant_emotion']
        return emotion

@app.route('/')
def index():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

app.run()