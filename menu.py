import json
import sys

# ping.py
from ping import ping
from check import checkServers


def listServers():
    with open("ips.json", "r") as f:
        data = json.load(f)
        ip_data = data["ips"]
        print("Volgende ip-adressen worden gecheckt:")
        for element in ip_data:
            print(f"+ {element}")
        print("\n\n")


def addServer():
    with open("ips.json", "r") as f:
        data = json.load(f)
        ip_data = data["ips"]
        print("Volgende ip-adressen worden gecheckt:")
        for element in ip_data:
            print(f"+ {element}")
        print("\n\n")

    while True:
        print("type 'stop' om te stoppen met ip's ingeven")
        newIP = input("Geef nieuw ip >")
        if newIP != "stop":
            ip_data.append(newIP)
        else:
            with open("ips.json", "w") as f:
                json.dump({"ips": ip_data}, f, indent=4)
            break


def addServerIP(ip):
    with open("ips.json", "r") as f:
        data = json.load(f)
        ip_data = data["ips"]
        ip_data.append(ip)
        with open("ips.json", "w") as f:
            json.dump({"ips": ip_data}, f, indent=4)


def removeServer():
    with open("ips.json", "r") as f:
        data = json.load(f)
        ip_data = data["ips"]
        print("Volgende ip-adressen worden gecheckt:")
        for index, element in enumerate(ip_data):
            print(f"[{index}] {element}")
        print("\n\n")

    while True:
        print("type 'stop' om te stoppen met ip's te verwijderen")
        remIp = input("Geef index van ip > ")
        if remIp != "stop":
            ip_data.pop(int(remIp))
        else:
            pass


def removeServerIP(ip):
    with open("ips.json", "r") as f:
        data = json.load(f)
        ip_data = data["ips"]
        ip_data.remove(ip)
        with open("ips.json", "w") as f:
            json.dump({"ips": ip_data}, f, indent=4)


def menu():
    print("Welkom, kies uit de volgende opties:")
    print("[1] Check ip-adressen")
    print("[2] Voeg ip-adres toe")
    print("[3] Verwijder ip-adres")
    print("[4] Check ip-adressen (ping)")
    keuze = input("Keuze > ")
    if keuze == "1":
        listServers()
    elif keuze == "2":
        addServer()
    elif keuze == "3":
        removeServer()
    elif keuze == "4":
        checkServers()
    else:
        print("Geen geldige keuze")
        menu()


# ....

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        listServers()
    elif sys.argv[1] == "add":
        addServerIP(sys.argv[2])
    elif sys.argv[1] == "remove":
        removeServerIP()
    elif sys.argv[1] == "check":
        checkServers()
    else:
        print("Geen geldige keuze")
