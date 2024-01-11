import smtplib
sender="person@gmail.com"
password=input("Enter password")
recv="2bobh@gmail.com"
msg="hello"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender,password)
print("Login successfuly")
server.sendmail(sender,recv,msg)
print("Email has been sent to",recv)  # first goto less secure apps : ON (from google)