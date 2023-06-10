import requests
import os

TEST_DATA = "TEST_DATA"
TEST_FILE = "face_2.jpg"
API_ENDPOINT  = "http://127.0.0.1:5000/emotion"
def send_file(file_path):
    with open(file_path,'rb') as f:
        r = requests.post(API_ENDPOINT,files={"face":f})
        return r.json()

def main():
    file_path = os.path.join(TEST_DATA,TEST_FILE)
    print(send_file(file_path))

if __name__ == "__main__":
    main()