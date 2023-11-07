from http import server
import json
from jinja2 import Template

# ping.py
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


def checkServersToHTML():
    with open("ips.json", "r") as f:
        data = json.load(f)
        ip_data = data["ips"]
        servers = []
        for element in ip_data:
            # loop door ips
            if ping(element) == True:
                online = "online"
            else:
                online = "offline"
            servers.append((element, online))

        with open("template.html") as file:
            template = Template(file.read())

        rendered_html = template.render(items=servers, online=online)

        with open("output.html", "w") as output_file:
            output_file.write(rendered_html)
        print("\n\n")


checkServersToHTML()
