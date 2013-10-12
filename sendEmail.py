import smtplib

FROM = 'EMAIL ADDRESS'
password = 'EMAIL PASSWORD

smtp_server = 'smtp.gmail.com:587'

def sendEmail(address, code, subject="CODE"):
	TO = address
	message = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (FROM, ", ".join(TO), subject, code)


	server = smtplib.SMTP(smtp_server)
	server.starttls()
	try:
		server.login(FROM,password)
	except SMTPAuthenticationError:
		pass

	server.sendmail(FROM, TO, message)
	server.quit()