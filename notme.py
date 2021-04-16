# Bedoff (*-*)

import os   # https://python-istihza.yazbel.com/standart_moduller/os.html
import datetime # kurulu olan işletim sisteminden zaman bilgisini almak için
import time # kurulu olan işletim sisteminden zaman bilgisini almak için
import dns.resolver #ileride dns ve ip değiştirmek için kullanacağım bir kütüphane şuanda bu özellikler hazır değil

os.system ("apt-get update")
os.system ("apt-get install figlet") # güzel bir karşılama için figlet yüklüyorum
os.system ("apt-get install tor") # tor network e bağlanabilmek için tor kuruyorum

os.system ("cd..")
os.system ("cd..")
os.system ("cd root")
os.system ("cd Desktop")

os.system ("clear") # kafa karıştırıcı olmaması ve sade gözükmesi açısından konsolu temizliyorum

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
print("3- Automatic Proxychain (Join tor network)")   # kolaylık olması açısından bir kullanıcının seçim yapabileceği bir menü hazırladım
print(style.RED +"4- Automatic Netmask Changer (DEACTIVATED)")
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


if selectno=="3":
	
	os.system("clear") # temizlik açısından tekrardan bir konsol temizliği
	os.system ("figlet     PROXYchain") # figlet ile proxychain ekranı oluşturdum
	
	print ("")
	print ("")
	print("1- Automatic setup proxychains.conf") 
	print("2- Open firefox with tor network")
	
	print("")
	selectno = input ("Select = ") # seçim yaptırtmak için tekrardan selectno değişkenini kullanıyorum
	
	if(selectno=="1"):
	
		os.system("clear")
		os.system("service tor start")  # tor servisini başlatıyorum
		os.system("service tor status") # tor servisini açtığımı kullanıcıya belirtiyorum
		print("")
		print("")
	
		print("Configure your proxychains.conf") 
		time.sleep(4)
	
		os.system("rm /etc/proxychains.conf") # tor un oluşturduğu proxychains.conf dosyasını siliyorum
	
		os.system("cd ..")
		os.system("cd ..")
		os.system("cd root")
		os.system("cd Desktop")
		os.system("cd notMe")  
	
		os.system("mv proxychains.conf /etc/") # daha öncesinden düzenlediğim ve github dan çektiğim proxychains.conf dosyasını notMe den /etc/ (ait olduğu yere) yolluyorum
		os.system("clear") 
		
		print(style.GREEN +"Configure DONE")
		time.sleep(2)
		
		os.system("clear")
		os.system("service tor restart") # tor servisini yeniden başlatıyorum
		time.sleep(4)
		os.system("clear")

		os.system("proxychains firefox www.google.com") # firefox u proxychains ile başlatıp google.com a yolluyorum

	if(selectno=="2"): # eğer bir kere proxychains kurulumu yapıldıysa artık 2. seçenek kullanılarak daha optimize ve seri çalışılabilir
		
		print("give me a sec")
		os.system("clear")
		os.system("service tor start") # her ihtimale karşı servisi yeniden başlatmayı deniyorum
		os.system(style.GREEN +"service tor restart") # ardından bir bug olmaması açısından resetliyorum
		time.sleep(4)
		os.system("clear")

		os.system("proxychains firefox www.google.com") # firefox u proxychains ile başlatıp google.com a yolluyorum

	else:
		print(style.RED +"wrong number")

else:  # eğer menüde hazır olmayan toollara gitmek istenirse hata mesajı ayarladım

	print(style.RED + "")
	print("this tool is not ready")
	
	
		
	
	







