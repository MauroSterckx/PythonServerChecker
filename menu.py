import json


def menu():
    print("Welkom, kies uit de volgende opties:")
    print("[1] Check ip-adressen")
    print("[2] Voeg ip-adres toe")
    print("[3] Verwijder ip-adres")


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
