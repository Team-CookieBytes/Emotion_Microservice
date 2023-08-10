from deepface import DeepFace
from LeXmo import LeXmo


def detect_dominant_emotion(img_path:str):
    try:
        
        print(img_path)
        objs = DeepFace.analyze(img_path,actions=("emotion"))
        
        print(objs)
        dominant_emotion = objs[0]['dominant_emotion']
        return (True,dominant_emotion)
    except Exception: 
        return (False,'')
    
def get_full_emotion_from_image(img_path:str):
    try:
        
        print(img_path)
        objs = DeepFace.analyze(img_path,actions=("emotion"))
        
        print(objs)
        
        return (True,objs[0]['emotion'])
    except Exception: 
        return (False,'')


def get_emotion_from_text(text:str):
    value = LeXmo.LeXmo(text)
    print(value)
    del value['text']
    if( all(value[x] == 0 for x in value )):
        return 'neutral'
    return max(value,key= lambda x: value[x]) 

def get_full_emotion_from_text(text:str):
    value = LeXmo.LeXmo(text)
    print(value)
    del value['text']
    return value;
    
    
    
   