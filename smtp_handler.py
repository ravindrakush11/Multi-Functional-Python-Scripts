import smtplib
import getpass

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = input("Enter sender's email: ")
TO_EMAIL = input("Enter receiver's email: ")
PASSWORD = getpass.getpass("Enter password: ")

MESSAGE = """Subject: This is a testing email
Hii Ravindra,

We are pleased to inform you about the testing of email.

Thanks,
Ravindra
"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()