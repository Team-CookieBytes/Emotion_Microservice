from deepface import DeepFace



def detect_dominant_emotion(img_path:str):
    try:
        objs = DeepFace.analyze(img_path,actions=("emotion"))
        print(objs)
        dominant_emotion = objs[0]['dominant_emotion']
        return (True,dominant_emotion)
    except Exception: 
        return (False,'')
