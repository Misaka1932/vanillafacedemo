# 此为主程序

import cv2
import os
from win32com.client import Dispatch

video = cv2.VideoCapture(0) #VideoCapture()中参数是0，表示打开笔记本的内置摄像头
                            #如果想打开一段录制好的视频，就在括号里面输入该视频的路径

font = cv2.FONT_HERSHEY_COMPLEX
fps = video.get(cv2.CAP_PROP_FPS) #获取视频的帧率和图像的尺寸
print(fps)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)

def face_detect_demo(img):
    # 将图片转换为灰度图片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #  创建级联分类器，通过该分类器检测人脸 参数：特征数据
    face_detector = cv2.CascadeClassifier(r'./cascade/haarcascade_frontalface_default.xml')
    # 检测人脸并返回人脸信息
    faces = face_detector.detectMultiScale(gray)
    # 遍历人脸信息获取 xX轴坐标  yY轴坐标  w宽度  h高度
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w , y + h), color = (0, 0, 255), thickness = 2) 
        # 通过矩形框出图片人脸部分
        cv2.putText(img, "Unknown", (x + 10, y - 5), font, 1, (255, 255, 255), 2)
        # 标出人名

    cv2.imshow('Face Capture' , img)

def welcome(id):  #语音播报功能
    '''
    id 0: 程序正常启动
    id 1: 未识别到图像
    id 2: 识别到数据库中的图像
    id 3: 识别到陌生人
    id 9: 退出
    '''
    if id == 0:
        msg = '欢迎'
    if id == 9:
        msg = '再见'

    speaker = Dispatch('SAPI.SpVoice')
    speaker.Speak(msg)
    del speaker

# welcome(0)
while True:
    ret, frame = video.read()
    # cv2.imshow("Face Capture", frame) 
    cv2.imwrite(r"./photo.png", frame)
    # video.read()是按帧读取视频，ret,frame是获cap.read()方法的两个返回值。
    # 其中ret是bool类型，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。
    # frame就是每一帧的图像，是个三维矩阵。

    c = cv2.waitKey(1) #显示完一帧后要等待多少毫秒显示下一帧，0为暂停
    img = cv2.imread(r"./photo.png")
    face_detect_demo(img)

    if c == 27:
        # welcome(9)
        break #esc退出

video.release()
cv2.destroyAllWindows()