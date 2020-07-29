import smtplib
from email.mime.text import MIMEText

body ='this is a tes email.hi'

msg = MIMEText(body)

msg['from']='moheldesouky2@gmail.com'
msg['to']='shaddyeldesouky@gmail.com'
msg['subject']= 'hello'

server =smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('moheldesouky2@gmail.com','maxcousin1243')
server.send_message(msg)
print('mail sent')

server.quit()