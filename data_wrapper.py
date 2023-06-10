
from typing import Optional
def face_response(status:bool,emotion:Optional[str]):
    return {"status":status,"emotion":emotion}
def bad_request_for_face():
    return face_response(False,None)

def success_response_for_face(emotion:str):
    return face_response(True,emotion)