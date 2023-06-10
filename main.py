from machine_learning import detect_dominant_emotion
from data_wrapper import bad_request_for_face,success_response_for_face

from flask import Flask, jsonify
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'temp_face_storage'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','webp'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def get_extension(filename):
    return filename.rsplit('.', 1)[1].lower()

@app.route('/emotion', methods=['GET', 'POST']) #type: ignore
def upload_file():
    FIELD_NAME = 'face'
    if request.method == 'POST':
        # check if the post request has the file part
        if FIELD_NAME not in request.files:
            return bad_request_for_face()
        file = request.files[FIELD_NAME]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '' or file.filename is None:
            return bad_request_for_face()
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            extension = get_extension(filename)
            print(filename)
            new_file_name = f'Uploaded_face.{extension}'
            new_file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_file_name)
            file.save(new_file_path)
            status,emotion = detect_dominant_emotion(new_file_path)
            if(not status):
                return bad_request_for_face()
            return success_response_for_face(emotion)

    return bad_request_for_face()


@app.route('/') #type: ignore
def test_route():
    return "<p>The server is up</p>"




