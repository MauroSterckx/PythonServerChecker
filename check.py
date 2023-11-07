import json
from ping import ping


def checkServers():
    with open("ips.json", "r") as f:
        data = json.load(f)
        ip_data = data["ips"]
        print("Volgende ip-adressen worden gecheckt:")
        for element in ip_data:
            # loop door ips
            print(f"+ {element}")
            if ping(element) == True:
                print(f"  - {element} is online")
        print("\n\n")
