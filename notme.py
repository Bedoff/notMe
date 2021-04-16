# Bedoff (*-*)

import os   # https://python-istihza.yazbel.com/standart_moduller/os.html
import datetime # kurulu olan işletim sisteminden zaman bilgisini almak için
import time # kurulu olan işletim sisteminden zaman bilgisini almak için
import dns.resolver #ileride dns ve ip değiştirmek için kullanacağım bir kütüphane şuanda bu özellikler hazır değil

os.system ("apt-get install figlet") # güzel bir karşılama için figlet yüklüyorum
os.system ("clear")

resolvString = 'nameserver 127.0.0.1' # şuan için işlevsel değil 


class style():          
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'        # terminal ekranında farklı renkte yazılar yazmak için kullanıyorum
    BLUE = '\033[34m'  
    WHITE = '\033[37m'
    RESET = '\033[0m'


print(style.BLUE + "")

os.system ("figlet     NotME")   # figlet kullanarak bir karşılama ekranı yaptım

print(style.WHITE + "")

print("1- Automatic MAC Changer (LAN)")
print("2- Automatic MAC Changer (WIFI)")
print(style.RED +"3- Automatic DNS Changer (DEACTIVATED)")   # kolaylık olması açısından bir kullanıcının seçim yapabileceği bir menü hazırladım
print("4- Automatic Netmask Changer (DEACTIVATED)")
print("5- Automatic IP Changer (DEACTIVATED)")


print(style.RESET + "")
	



selectno = input ("Select = ")  # kullanıcının menüden seçip yazdığı rakamı selectno değişkenine atadım



if selectno=="1":  
	settime = int( input ("SetTime(SEC) = "))  # kaç saniyede bir döngünün tekrar etmesi (mac adresinin değişmesi) bilgisini kullanıcıdan aldım


	os.system("clear")
	print(style.BLUE + "")
	
	
	a = 1
	while a==1:  # kullanıcı programı durdurana kadar bitmesini istemediğim için sonsuz döngü kullandım
		now = datetime.datetime.now() # sistemden zaman bilgisini aldım
		print (" ")	
		print (style.RESET + "Time= " + now.strftime("%H:%M:%S")) # zaman bilgisini saat,dakika,saniye olarak ekrana yazdırdım
		print (style.BLUE + "" )
		os.system("macchanger --random eth0") #macchanger --random eth0 ile mac adresini değiştirdim
		time.sleep(settime) # kullanıcının istediği süre ile delay koydum




if selectno=="2":
	settime = int( input ("SetTime(SEC) = "))  # kaç saniyede bir döngünün tekrar etmesi (mac adresinin değişmesi) bilgisini kullanıcıdan aldım


	os.system("clear")
	print(style.BLUE + "")
	
	
	a = 1
	while a==1:  # kullanıcı programı durdurana kadar bitmesini istemediğim için sonsuz döngü kullandım
		now = datetime.datetime.now() # sistemden zaman bilgisini aldım
		print (" ")	
		print (style.RESET + "Time= " + now.strftime("%H:%M:%S")) # zaman bilgisini saat,dakika,saniye olarak ekrana yazdırdım
		print (style.BLUE + "" )
		os.system("macchanger --random wlan0") #macchanger --random wlan0 ile mac adresini değiştirdim
		time.sleep(settime) # kullanıcının istediği süre ile delay koydum




else:  # eğer menüde hazır olmayan toollara gitmek istenirse hata mesajı ayarladım

	print(style.RED + "")
	print("this tool is not ready")
	

		
	
	







