import smtplib
import ssl
import email

subject = 'Email from python'
body = 'This is an email from python'
sender_email = 'kapilkatari2002@gmail.com'
reciever_email = 'kapil.kataria2020@vitbhopal.ac.in'
password = input('Enter you password: ')

message = email.message.EmailMessage()
message['From'] = sender_email
message['To'] = reciever_email
message['Subject'] = subject
message.set_content(body)

context = ssl.create_default_context()


print('Sending Email.....')

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message.as_string)

