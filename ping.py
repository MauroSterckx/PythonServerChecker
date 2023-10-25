import os
import subprocess

ips = ["localhost", "test123", "localhost"]

def ping(ip):
    res = subprocess.call(f"ping -n 1 {ip}", stdout=subprocess.DEVNULL)
    if res == 0:
        return True
    else:
        return False



