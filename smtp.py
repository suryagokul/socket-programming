import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

server = smtplib.SMTP('smtp.gmail.com', 25)

server.connect('smtp.gmail.com')

server.ehlo()

server.starttls()

server.ehlo()

server.login('peddintigokul946@gmail.com', '**************')

# place App password as 2nd argument in login.To get app password follow steps said in this  https://www.interviewqs.com/blog/py-email

msg = MIMEMultipart()

msg['From'] = 'Surya'
msg['To'] = 'tavew21525@liaphoto.com'             # temporary mail created using https://temp-mail.org/en website...
msg['subject'] = "Text message"

with open("message.txt", 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = "C:\\Users\\SURYA\\Pictures\\cross-entropy-diagram.png"

attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')

p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')

msg.attach(p)

text = msg.as_string()

server.sendmail('peddintigokul946@gmail.com', 'tavew21525@liaphoto.com', text)
