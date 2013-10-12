2Factor-SSH
===========

<h4>2-Factor Authentication for SSH</h4>
Files:

<b>2fa.c</b> - PAM module for SSH (change the base_url and code_size options)<br><br>

<b>Python files are for a CGI script to send a code via email or google voice text</b>

<b>otp.py</b> - CGI script that takes a 'username' and 'code' and uses email or sms to send code to user<br>
<b>gv.py</b>  - function to interact with google voice and send a text message with code<br>
<b>sendEmail.py</b> - function to send an email with code to an email address

<h3>Requirements:</h3><br>
<ul><li>C libpam</li>
<li>C libcurl</li>
<li>pygooglevoice</li>
<li>Google Voice Account</li>
