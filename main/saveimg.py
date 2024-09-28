# 此为录入程序

import cv2
import os
import time
from win32com.client import Dispatch

video = cv2.VideoCapture(0) 
font = cv2.FONT_HERSHEY_COMPLEX
piccount = 0

def speakmessage(msg):
    speaker = Dispatch('SAPI.SpVoice')
    speaker.Speak(msg)
    del speaker

def img_main():
    img = cv2.flip(video.read()[1],1)
    # cv2.imshow('Pressing...', img)
    with open(r'./log/global.txt', 'r') as file:
        piccount = file.read()

    piccount = int(piccount)
    piccount = piccount + 1

    saveimgname = "./data/" + str(piccount) + ".png"
    cv2.imwrite(saveimgname, img)
    with open(r'./log/global.txt', 'w') as file:
        file.write(str(piccount))

def saveimg(id):
    if id == 1: 
        speakmessage("请微微把脸部向左转")
        time.sleep(2)
        img_main()

    if id == 2:
        speakmessage("请微微把脸部向右转")
        time.sleep(2)
        img_main()

    if id == 3:
        speakmessage("请回到屏幕正中间，然后眨眨眼")
        time.sleep(1)
        for i in range (1, 9):
            img_main()
            time.sleep(0.5)

speakmessage("请保持面部处于屏幕正中间, 然后按下S键, 开始录入")
flag = 0
while True:
    img = cv2.flip(video.read()[1],1)
    cv2.imshow('Press S to start', img)
    c = cv2.waitKey(1)
    if c == 27:
        break

    if c == 83 or c == 115:
        cv2.destroyAllWindows()
        for flag in range(1, 4):
            # img = cv2.flip(video.read()[1],1)
            # cv2.imshow('Processing', img)
            saveimg(flag)

        speakmessage("录入完毕, 谢谢你的配合")
        break
    # cv2.destroyAllWindows()

video.release()
cv2.destroyAllWindows()