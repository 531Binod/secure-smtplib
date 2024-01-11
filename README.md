# Sending a Plain-Text Email
you’ll learn to send plain-text emails using Python. 
These are emails that you could write up in a simple text editor.

# Starting a Secure SMTP Connection
When you send emails through Python, you should make sure that your SMTP connection is encrypted, 
so that your message and login credentials are not easily accessed by others. 
SSL (Secure Sockets Layer) and TLS (Transport Layer Security) are two protocols that can be used to encrypt an SMTP connection. 
It’s not necessary to use either of these when using a local debugging server.

There are two ways to start a secure connection with your email server:
Start an SMTP connection that is secured from the beginning using SMTP_SSL().
Start an unsecured SMTP connection that can then be encrypted using .starttls().
# Send Email to Multiple Recipients using Python
If you need to send the same message to different people. 
You can use for loop for that. For example, you have a list of email ids to which you need to send the same mail. 
To do so, insert a “for” loop between the initialization and termination of the SMTP session. 
Loop will initialize turn by turn and after sending the email, the SMTP session will be terminated.

1.import smtplib
<br>
2.# list of email_id to send the mail
<br>
3.li = ["xxxxx@gmail.com", "yyyyy@gmail.com"]
<br>
4. for dest in li:
<br>
5.	   s = smtplib.SMTP('smtp.gmail.com', 587)
<br>
6.	   s.starttls()
<br>
7.	   s.login("sender_email_id", "sender_email_id_password")
<br>
8.	   message = "Message_you_need_to_send"
<br>
9.	   s.sendmail("sender_email_id", dest, message)
<br>
10.	   s.quit()
