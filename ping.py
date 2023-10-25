import os
import subprocess

ips = ["localhost", "test123", "localhost"]

def ping(ip):
    res = subprocess.call(f"ping -n 1 {ip}", stdout=subprocess.DEVNULL)
    if res == 0:
        return True
    else:
        return False

def menu():
    print("Volgende ip-adressen worden gecheckt:")
    for element in ips:
        print(f"+ {element}")
    while True:
        newIP = input("Geef nieuw ip")


print(ping("localhost"))
print(ping("localhost69"))


