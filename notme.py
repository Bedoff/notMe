# Bedoff (*-*)

import os   
import datetime 
import time 
import dns.resolver 

os.system ("apt-get update")
os.system ("apt-get install figlet") m
os.system ("apt-get install tor") 

os.system ("clear") 

resolvString = 'nameserver 127.0.0.1' # şuan için işlevsel değil 


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
print("3- Automatic Proxychain (SOCKS5)")   
print(style.RED +"4- Automatic Netmask Changer (DEACTIVATED)")
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

if selectno=="3":
	
	os.system("clear") 
	os.system ("figlet     PROXYchain") 
	
	print ("")
	print ("")
	print("1- Automatic setup proxychains.conf") 
	print("2- Open firefox with proxychain ")
	
	print("")
	selectno = input ("Select = ") 
	
	if(selectno=="1"):
	
		os.system("clear")
		os.system("service tor start") 
		os.system("service tor status") 
		print("")
		print("")
	
		print("Configure your proxychains.conf") 
		time.sleep(4)
	
		os.system("rm /etc/proxychains.conf") 
	
		os.system("cd ..")
		os.system("cd ..")
		os.system("cd root")
		os.system("cd Desktop")
		os.system("cd notMe")  
	
		os.system("mv proxychains.conf /etc/") 
		os.system("clear") 
		
		print(style.GREEN +"Configure DONE")
		time.sleep(2)
		
		os.system("clear")
		os.system("service tor restart") 
		time.sleep(4)
		os.system("clear")

		os.system("proxychains firefox www.google.com") 

	if(selectno=="2"): 
		
		print("give me a sec")
		os.system("clear")
		os.system("service tor start") 
		os.system(style.GREEN +"service tor restart") 
		time.sleep(4)
		os.system("clear")

		os.system("proxychains firefox www.google.com") 

	else:
		print(style.RED +"wrong number")

else:  

	print(style.RED + "")
	print("this tool is not ready")
	
	
		
	
	





