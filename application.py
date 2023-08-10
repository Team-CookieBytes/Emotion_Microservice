from machine_learning import detect_dominant_emotion,get_emotion_from_text,get_full_emotion_from_image,get_full_emotion_from_text
from data_wrapper import bad_request_for_face,success_response_for_face

from flask import Flask, jsonify
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS
import base64


UPLOAD_FOLDER = 'temp_face_storage'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','webp'}

application = Flask(__name__)
CORS(application)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def get_extension(filename):
    return filename.rsplit('.', 1)[1].lower()

@application.route('/emotion', methods=['GET', 'POST']) #type: ignore
def upload_file():
    FIELD_NAME = 'face'
    if request.method == 'POST':
        print(request.form)
        # check if the post request has the file part
        file  = None
        image = None
        
        if FIELD_NAME not in request.files:
            
            if('face' not in request.form):
                return bad_request_for_face()
            data  = request.form['face']
            data = data[data.find(",")+1:]
            image = base64.b64decode(data)
            # print(image)

        else:
            
            file = request.files[FIELD_NAME]
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '' or file.filename is None:
                print("no file in the value")
                return bad_request_for_face()
        new_file_name = f'Uploaded_face.png'
        new_file_path = os.path.join(application.config['UPLOAD_FOLDER'], new_file_name)
        if file and allowed_file(file.filename):
            
            filename = secure_filename(file.filename) #type: ignore
            extension = get_extension(filename)
            print(filename)
            new_file_name = f'Uploaded_face.{extension}'
            new_file_path = os.path.join(application.config['UPLOAD_FOLDER'], new_file_name)
            file.save(new_file_path)
        elif image is not None:
            with open(new_file_path,'wb+') as f:
                f.write(image)
        status,emotion = detect_dominant_emotion(new_file_path)
        
        if(not status):
            return bad_request_for_face()
        return success_response_for_face(emotion)

    return bad_request_for_face()

@application.route('/emotion/full', methods=['GET', 'POST']) #type: ignore
def upload_file2():
    FIELD_NAME = 'face'
    if request.method == 'POST':
        print(request.form)
        # check if the post request has the file part
        file  = None
        image = None
        
        if FIELD_NAME not in request.files:
            
            if('face' not in request.form):
                return bad_request_for_face()
            data  = request.form['face']
            data = data[data.find(",")+1:]
            image = base64.b64decode(data)
            # print(image)

        else:
            
            file = request.files[FIELD_NAME]
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '' or file.filename is None:
                print("no file in the value")
                return bad_request_for_face()
        new_file_name = f'Uploaded_face.png'
        new_file_path = os.path.join(application.config['UPLOAD_FOLDER'], new_file_name)
        if file and allowed_file(file.filename):
            
            filename = secure_filename(file.filename) #type: ignore
            extension = get_extension(filename)
            print(filename)
            new_file_name = f'Uploaded_face.{extension}'
            new_file_path = os.path.join(application.config['UPLOAD_FOLDER'], new_file_name)
            file.save(new_file_path)
        elif image is not None:
            with open(new_file_path,'wb+') as f:
                f.write(image)
        status,emotion = get_full_emotion_from_image(new_file_path)
        
        if(not status):
            return bad_request_for_face()
        return emotion

    return bad_request_for_face()

@application.route('/text',methods=['GET','POST']) #type:ignore
def text_analysis():
    if(request.method == 'POST'):
        if(not request.is_json):
            return bad_request_for_face()
        if('text' not in request.json): #type: ignore
            return bad_request_for_face()

        text = request.json['text'] #type: ignore
        if(len(text) == 0):
            print("The text is empty")
            print(request.json)
            print(request.data)
            print(request.form)
            return bad_request_for_face()
        print(f"text is :{text}")
        return success_response_for_face(get_emotion_from_text(text))


    return bad_request_for_face()

@application.route('/text/full',methods=['GET','POST']) #type:ignore
def text_analysis2():
    if(request.method == 'POST'):
        if(not request.is_json):
            return bad_request_for_face()
        if('text' not in request.json): #type: ignore
            return bad_request_for_face()

        text = request.json['text'] #type: ignore
        if(len(text) == 0):
            print("The text is empty")
            print(request.json)
            print(request.data)
            print(request.form)
            return bad_request_for_face()
        print(f"text is :{text}")
        return get_full_emotion_from_text(text[0])


    return bad_request_for_face()
        

@application.route('/') #type: ignore
def test_route():
    return "<p>The server is up</p>"

if __name__ == '__main__':
    application.run(port=8080)




