# Created By: Ruben Leonardo Sigalingging.

# Created On: Sunday, June 5, 2022, 22:15 PM.

# Using : Python Programming Language Version 3.

# whatsapp sender tool


def whatsapp_sender_tool():
	# https://pypi.org/project/pywhatkit/
	import os
	import sys
	os.system("pip install pywhatkit")
	os.system("chmod 777 WhatsAppSenderTool.py")
	import pywhatkit
	import time
	import requests
	import datetime
	import pyfiglet
	style = pyfiglet.figlet_format("PyWhatKit")
	print(style)
	print("[!] Created By: Ruben Leonardo Sigalingging.")
	print("[!] Created On: Sunday, June 5, 2022, 22:15 PM.")
	print("[!] Using : Python Programming Language Version 3.")
	print("")
	phonenumber = input("[!] Enter Phone Number: ")
	message = input("[!] Enter Message: ")
	hours = int(input("[!] Enter Hours: "))
	minute = int(input("[!] Enter Minutes: "))
	pywhatkit.sendwhatmsg(phonenumber, message, hours, minute)
whatsapp_sender_tool()