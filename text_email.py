import getpass 
import smtplib
HOST = 'smtp-mail.outlook.com' #server domain name of outlook
PORT = 587 #server port for smtplib
FROM_EMAIL = 'daniele.basile.jobol@outlook.com'
TO_EMAIL = 'daniele.basile.job@gmail.com' #test email
PSW = getpass.getpass('Enter password: ')
MESSAGE = """ Subject: Mail sent using Python
Hi Python fan,
This email is sent using a test account,

Thanks,
Test Account
"""
smtp = smtplib.SMTP(HOST, PORT)
status_code, response = smtp.ehlo()
print(f"Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"Starting the connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PSW)
print(f"Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()