import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['to'] = "#Reciever Email"
email['from'] = 'Python Iterpreter'
email['subject'] = 'Test'

email.set_content('This is a Test Mail \n From Idris')

with smtplib.SMTP(host = "smtp.gmail.com", port = "587") as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("senderEmail",'password')
    smtp.send_message(email)
    print("Email Sent!")