#!/usr/bin/env python
# __author__ = 'vageli'

import cgi, cgitb
from gv import sendTxt
from sendEmail import sendEmail

form = cgi.FieldStorage() 

#load database of users

#change example code below
#database holds username as key and either email or phone number as value
#emails are prefaced with an 'e' and phone numbers are prefaced with a 'p'
#to determine which handler will send the code

users = {'user1':'p1234567890', 'user2':'etestemail@example.com'}#EXAMPLE DATA

username = form.getvalue('username')
code  = form.getvalue('code')

#Strip quotes around values
username = str(username)
username = username.translate(None, "'")
code = str(code)
code = code.translate(None, "'")
#Code is a string at this point (not a number)

#Check if username exists in database
if username in users:
	#determine method to contact
	if users[username][0] == 'p':
		number = users[username][1:]
		sendTxt(number,code)

	if users[username][0] == 'e':
	#email address must be a list for SMTP
		address = [users[username][1:]]
		sendEmail(address,code)


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head />"
print "<body>"
print "<h2>%s %s</h2>" % (username, code)
print "</body>"
print "</html>"
