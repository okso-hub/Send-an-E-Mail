import smtplib, ssl
from email.message import EmailMessage

subject = input("Enter subject: ")
body = input("Enter content: ")
sender_email = input("Enter your E-Mail address: ")
receiver_email = input("Enter receiver E-Mail: ")
password = input("Enter your password: ")

message= EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subcject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending E-Mail...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Success.")
