import cv2
import numpy as np
from PIL import Image
import os

path = 'data'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("./cascade/haarcascade_frontalface_alt2.xml")

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    if len(imagePaths):
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')
            face_training_id = int(os.path.split(imagePath)[-1].split(".")[0])   
            faceSamples.append(img_numpy)
            ids.append(face_training_id)

    return faceSamples, ids

print("Training...")
faces, ids = getImagesAndLabels(path)

if faces == [] or ids == []:
    print("None")
else:
    recognizer.train(faces, np.array(ids))
    recognizer.write(r'./trainer/trainer.yml') 
    print("Totol " + str(len(np.unique(ids))) + " Pictures")