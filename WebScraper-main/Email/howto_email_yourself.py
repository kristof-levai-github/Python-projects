#pip install creds
import creds
import requests
import pandas as pd 
import smtplib #the directory we need to send emails (SMTP = simple mail transfer protocol)

#ezek építik fel az emailt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#kell egy credentials.py is a küldővel, fogadóval és a küldő jelszóval
creds.sender = 'kristof.zalan.levai@student.uni-miskolc.hu'
creds.recipient = 'kristof.levai@gmail.com'
creds.password = 'Xezfgegu2002'

def email_new(df):
    #értelem szerűen ezek az adataink és a subject amit látunk
    message = MIMEMultipart()
    message['Subject'] = 'New data from today'
    message['From'] = creds.sender
    message['To'] = creds.recipient

    #ez az actual elküldött rész, az elején a df azért kell, hogy egy dataframeba legyen
    html = MIMEText(df.to_html(index=False), "html")
    message.attach(html)
    #gmail nem, megy -> outlook
    with smtplib.SMTP("smtp.office365.com", 587) as server: 
        server.starttls()
        server.login(creds.sender, creds.password)
        server.sendmail(creds.sender, creds.recipient, message.as_string())

def data_get():
#--------- PÉLDA ADATOK ---------------#
    r = requests.get('https://rickandmortyapi.com/api/episode')
    episodes = pd.json_normalize(r.json()['results'])

    return episodes

if __name__ == '__main__':
    data = data_get()
    email_new(data)