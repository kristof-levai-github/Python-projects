#---------------------------------------------------------email

#kell hozzá -> smtp server

import smtplib
from email import message

#sima email küldése, attachment nélkül:


#from_addr = 'email-honnan'
#to_addr = 'email-hova'
#subject = 'ez lesz az email szövege (fejléce)'
#body vagy content = 'Ez lesz magában a levélben!'


#------------------------------------------------------

#msg = message.Message()
#ms.add_header('from', from_addr)
#msg.add_header('to', to addr)
#msg.add_header('subject', subject)
#msg.set_payload(body)
#msg

#server = smtplib.SMTP('smtp.dreamhost.com', 587) #email-server - port
#server.login(from_addr, 'password') - email, pass
#server.send_message(msg, from_addr=from_addr, to_addrs=[to addr]) | lehet email lista is

#------------------------------------------------------



#email küldése attachmenttel:

import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from email.mime.application import MIMEApplication


#from_addr = 'email-honnan'
#to_addr = 'email-hova'
#subject = 'ez lesz az email szövege (fejléce)'
#body vagy content = 'Ez lesz magában a levélben!'

#------------------------------------------------------

#msg = MIMEMultipart()
#msg['From'] = from_addr
#msg['To'] = to_addr
#msg['Subject'] = subject
#body = MIMEText(content, 'plain')
#msg.attach(body)

#filename = "kep.png
#with open(filename, 'r') as f:
    #attachment = MIMEApplication(f.read(), Name=basename(filename))
    #attachment = ['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))

#ezzel a 4 sorral gyakorlatilag leformáztuk

#msg.attach(attachment)

#server = smtplib.SMTP('smtp.dreamhost.com', 587) #email-server - port
#server.login(from_addr, 'password') - email, pass
#server.send_message(msg, from_addr=from_addr, to_addrs=[to addr]) | lehet email lista is

#------------------------------------------------------



#Sok Email küldése egy .csv fájlból
#simán sok email küldése egy listából:
#https://levelup.gitconnected.com/sending-bulk-emails-via-python-4592b7ee57a5

import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



#email_semder = "az az email, amiről küldjük a mass-t"
#password = "sender email passwordja"
#subject = "Hajrá!

#------------------------------------------------------

#with open('email.csv', 'r') as csfile:
 #   reader = csv.reader(csvfile)
  #      for line in reader:
   #     text="hello"+line[1]+"you"+line[2]+"plan has been activated" |line1,2 = második és harmadik sor a csv-nek pl: ha ,-el van elválasztva akkor az 1 és 2. , utáni lesz
    #    print(text)

#email_send = line[0]
#msg = MIMEMultipart()
#msg[from] #ugyan az mint fennt
#msg[to]
#msg[subject]
#msg.attach(MIMEText(text,"plain"))
#text = msg.as_string()


#server = smtplib.SMTP_SSL | ha kell ssl| ('smtp.dreamhost.com', 587) #email-server - port
#server.login(from_addr, 'password') - email, pass
#server.sendmail(email_user, email_send, text)

#server.quit()

#------------------------------------------------------

#google -> allow less secure apps: ON -> google-nél enélkül tiltja a python scriptet




#emails with http
#minden ugyan az, csak a body változik

#body = """<html>
#            <body>
 #             <p>Hi,<b>My name is Sarath Kaul</b></p>
  #            <p> I am reaching out to you to check my email HTML Content </p>
   #         </body>
    #      </html>
     #  """
#msg.attach(MIMEText(body, 'html')


