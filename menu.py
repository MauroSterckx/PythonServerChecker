import json


def menu():
    with open('ips.json', 'r') as f:
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
            with open("ips.json" , "w") as f:
                json.dump({"ips" : ip_data}, f, indent=4)
            break
