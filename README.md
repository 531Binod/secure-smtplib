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
