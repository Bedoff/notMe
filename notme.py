# Bedoff (*-*)

import os
import datetime
import time
import dns.resolver

os.system ("apt-get install figlet")
os.system ("clear")

resolvString = 'nameserver 127.0.0.1'


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    WHITE = '\033[37m'
    RESET = '\033[0m'


print(style.BLUE + "")

os.system ("figlet     NotME")

print(style.WHITE + "")

print("1- Automatic MAC Changer (LAN)")
print("2- Automatic MAC Changer (WIFI)")
print(style.RED +"3- Automatic DNS Changer (DEACTIVATED)")
print("4- Automatic Netmask Changer (DEACTIVATED)")
print("5- Automatic IP Changer (DEACTIVATED)")


print(style.RESET + "")
	



selectno = input ("Select = ")



if selectno=="1":
	settime = int( input ("SetTime(SEC) = "))


	os.system("clear")
	print(style.BLUE + "")
	
	
	a = 1
	while a==1:
		now = datetime.datetime.now()
		print (" ")	
		print (style.RESET + "Time= " + now.strftime("%H:%M:%S"))
		print (style.BLUE + "" )
		os.system("macchanger --random eth0")
		time.sleep(settime)




if selectno=="2":
	settime = int( input ("SetTime(SEC) = "))


	os.system("clear")
	print(style.BLUE + "")
	
	
	a = 1
	while a==1:
		now = datetime.datetime.now()
		print (" ")	
		print (style.RESET + "Time= " + now.strftime("%H:%M:%S"))
		print (style.BLUE + "" )
		os.system("macchanger --random wlan0")
		time.sleep(settime)




else:

	print(style.RED + "")
	print("this tool is not ready")
	

		
	
	







