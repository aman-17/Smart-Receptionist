import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime
import speech_recognition as sr
import cv2

r=sr.Recognizer()

def speech_to_text():
    global sr
    print('Hello! you need to register while entering the office.')
    input("\n\nPress Enter to Register\n\n")
    with sr.Microphone() as source:
        print('Please say your name')
        audio=r.listen(source)

        try:
            text=r.recognize_google(audio)

            print('You said: {}'.format(text))

        except:
            print('Sorry could not recognize')
    return text
def date():
    date1=str(datetime.now())
    return date1


def handle_date():
    date=str(datetime.now()).split(' ')[0]
    if not(os.path.isdir(date)):
        os.mkdir(date)
    return date
	

        
camera = cv2.VideoCapture(0)
return_value,image = camera.read()
#if cv2.waitKey(1)& 0xFF == ord('s'):
#text = str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg'
cv2.imwrite(handle_date()+"/"+speech_to_text().replace(' ','_').lower()+".jpg",image)
camera.release()

print('Thanks for visiting, I have register your data and vistied on: \n'+date())
