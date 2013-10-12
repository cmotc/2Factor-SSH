2Factor-SSH
===========

2-Factor Authentication for SSH
Files:

2fa.c - PAM module for SSH
  -change the base_url and code_size options

Python files are for a CGI script to send a code via email or google voice text

otp.py - CGI script that takes a 'username' and 'code' and uses email or sms to send code to user
gv.py  - function to interact with google voice and send a text message with code
sendEmail.py - function to send an email with code to an email address
