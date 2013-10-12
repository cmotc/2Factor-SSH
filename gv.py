#!/usr/bin/env python
# __author__ = 'vageli'

from googlevoice import Voice

username = 'GOOGLE VOICE USERNAME' #include @gmail.com
password = 'GOOGLE VOICE PASSWORD'
voice = Voice()

def sendTxt(number, message):
	try:
		voice.login(username,password)

	except LoginError:
		return -1

	voice.send_sms(number, message)