import creds
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

creds.sender = 'kristof.zalan.levai@student.uni-miskolc.hu'
creds.recipient = 'kristof.levai@gmail.com'
creds.password = 'Xezfgegu2002'

# Set up the email message
message = MIMEMultipart()
message["From"] = creds.sender
message["To"] = creds.recipient
message["Subject"] = "Teszt_attachment"

# Attach the body text
message.attach(MIMEText("Hello, please find the attached file."))

# Open the file you want to attach
with open("C:\\Users\\ADMIN\\Desktop\\python\web\\webscraper_testsites\\EMAIL\\bizonyitvany.pdf", "rb") as file:
    # Create a MIMEApplication object
    attachment = MIMEApplication(file.read(), _subtype="pdf")

# Set the attachment filename
attachment.add_header(
    "Content-Disposition",
    "attachment",
    filename="bizonyitvany.pdf"
)

# Attach the file to the email message
message.attach(attachment)

# Send the email
with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.starttls()
    server.login(creds.sender, creds.password)
    server.sendmail(creds.sender, creds.recipient, message.as_string())
