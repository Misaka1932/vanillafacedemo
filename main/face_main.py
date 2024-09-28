import cv2
import os
import time

video = cv2.VideoCapture(0) 
font = cv2.FONT_HERSHEY_COMPLEX
fps = video.get(cv2.CAP_PROP_FPS)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('./trainer/trainer.yml')
cascadePath = './cascade/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)

face_name = "Unknown"
names = ['None', 'vanilla', 'vanilla_2']
face_output_id = 0
face_1st_flag = 0

while True:
    img = cv2.flip(video.read()[1],1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(32, 32))
    if len(faces):
        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            face_output_id, confidence = recognizer.predict(gray[y : y + h, x : x + w])
            real_confidence = int(100 - confidence) + 30
            if (real_confidence > 70):
                if face_output_id <= 10:
                    face_name = 'vanilla'
                else:
                    face_name = 'vanilla_2'
                print(face_output_id)

                face_confidence = str(real_confidence) + "%"
                if face_1st_flag == 0:
                    face_1st_flag = 1
                    face_1st_id = face_output_id
                    face_1st_time = time.time()

                else:
                    if 1.1 > time.time() - face_1st_time > 1.0 :
                        if face_output_id == face_1st_id:
                            face_1st_flag = 0
                            
                        if time.time() - face_1st_time > 1.1:
                            face_1st_flag = 0
                
            else:
                face_name = "Unknown"
                face_confidence = str(real_confidence) + "%"

            cv2.putText(img, str(face_name), (x + 5, y - 5), font, 1, (147,20,255), 2)
            cv2.putText(img, str(face_confidence), (x + 5, y + h - 5), font, 1, (255,255,255), 1)  

    cv2.imshow('Face Capture',img) 

    if cv2.waitKey(10) == 27:
        break

video.release()
cv2.destroyAllWindows()