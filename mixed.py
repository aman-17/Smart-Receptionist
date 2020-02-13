import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print('Please speak the information you want to send: ')
    audio=r.listen(source)

    try:
        text=r.recognize_google(audio)

        print('You said: {}'.format(text))

    except:
        print('Sorry could not recognize')
        

message = Mail(
    from_email='Enter your E-mail',
    to_emails='Enter the E-mail you want to send',
    subject='Regarding Meeting',
    html_content='<strong>%s</strong>'%(text))
try:
    sg = SendGridAPIClient('Enter API key')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)        
