import speech_recognition as sr
import os
from PIL import Image

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something')
    audio = r.listen(source)
    print('Thanks! I think I got it.')

try:
    text = r.recognize_google(audio)
    # print('Text: ' + text)
    os.system('python get_hand.py -t "' + text + '" -s 4 -c 0,0,200' )
    img = Image.open('images/0.png')
    img.show()
except:
    pass