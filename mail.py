import smtplib
import imghdr
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Test mail'
#msg['Subject'] = 'Test mail- with attachment'
msg['From'] = 'Senders Email ID'
msg['To'] = 'Recievers Email ID'
msg.set_content('This is a test mail')
#msg.set_content('Check out this really cute puppy!')

#files = ['puppy.jpg']
#
# for file in files:
#       with open(file, 'rb') as f:
#           file_data = f.read()
#           file_type = imghdr.what(f.name)
#           file_name = f.name
#
#       msg.add_attachment(file_data,maintype='image',subtype=file_type,filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
       smtp.login('YOUR_EMAIL_ID', 'YOUR_PASSWORD')
       smtp.send_message(msg)

