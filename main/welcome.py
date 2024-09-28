import os
from win32com.client import Dispatch

def welcome(): 
    msg  = '所有人，排位赛报名了，最后十分钟再不报名没机会了'
    msg2 = '所有人，上号打盐场了，所有人上号，打盐场了，所有人上号，打盐场了'
    speaker = Dispatch('SAPI.SpVoice')
    speaker.Speak(msg)
    speaker.Speak(msg2)
    del speaker

welcome()