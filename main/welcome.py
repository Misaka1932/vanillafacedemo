import os
from win32com.client import Dispatch

def welcome(): 
    msg  = '香草'
    msg2 = '真可爱喵'
    speaker = Dispatch('SAPI.SpVoice')
    speaker.Speak(msg)
    speaker.Speak(msg2)
    del speaker

welcome()