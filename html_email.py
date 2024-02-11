import getpass 
import smtplib
from email.mime.multipart import MIMEMultipart #create email message obj 
from email.mime.text import MIMEText #to add html content

HOST = 'smtp-mail.outlook.com' #server domain name of outlook
PORT = 587 #server port for smtplib
FROM_EMAIL = 'daniele.basile.jobol@outlook.com'
TO_EMAIL = 'daniele.basile.job@gmail.com' #test email
PSW = getpass.getpass('Enter password: ')
message = MIMEMultipart("alternative") #used for email
message['Subject'] = 'Mail sent using Python' 
message['From'] = FROM_EMAIL 
message['To'] = TO_EMAIL 
message['Cc'] = FROM_EMAIL 
message['Bcc'] = FROM_EMAIL

html = "" 
with open('email.html', 'r') as html_file:
    html = html_file.read()

html_part = MIMEText(html, 'html') 
message.attach(html_part)  # Attach the HTML part to the email message

smtp = smtplib.SMTP(HOST, PORT)
status_code, response = smtp.ehlo()
print(f"Echoing the server: {status_code} {response}")


status_code, response = smtp.starttls()
print(f"Starting the connection: {status_code} {response}")


status_code, response = smtp.login(FROM_EMAIL, PSW)
print(f"Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
smtp.quit()


