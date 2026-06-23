import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime

ROUTER = "192.168.56.103"
USER = "cisco"
PASS = "cisco123!"

headers = {
    "Accept": "application/yang-data+json"
}

print("=" * 60)
print("VALIDACION RESTCONF")
print("Alumno: Maikol Luis Mamani Segobia")
print("Codigo: 001V-09")
print("Fecha:", datetime.now())
print("=" * 60)

checks = 0

# HOSTNAME
url = f"https://{ROUTER}/restconf/data/Cisco-IOS-XE-native:native/hostname"

r = requests.get(
    url,
    headers=headers,
    auth=HTTPBasicAuth(USER, PASS),
    verify=False
)

open("responses/get_hostname.json", "w").write(r.text)

if "RTR-MEDAND" in r.text:
    print("[OK] Hostname")
    checks += 1

# LOOPBACK
url = f"https://{ROUTER}/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=0"

r = requests.get(
    url,
    headers=headers,
    auth=HTTPBasicAuth(USER, PASS),
    verify=False
)

open("responses/get_loopback.json", "w").write(r.text)

if "10.1.9.1" in r.text:
    print("[OK] Loopback")
    checks += 1

# INTERFACES
url = f"https://{ROUTER}/restconf/data/Cisco-IOS-XE-native:native/interface"

r = requests.get(
    url,
    headers=headers,
    auth=HTTPBasicAuth(USER, PASS),
    verify=False
)

open("responses/get_interfaces.json", "w").write(r.text)

if "Enlace-WAN-Rancagua" in r.text:
    print("[OK] WAN")
    checks += 1

# NTP
url = f"https://{ROUTER}/restconf/data/Cisco-IOS-XE-native:native/ntp"

r = requests.get(
    url,
    headers=headers,
    auth=HTTPBasicAuth(USER, PASS),
    verify=False
)

open("responses/get_ntp.json", "w").write(r.text)

if "1.1.1.1" in r.text:
    print("[OK] NTP")
    checks += 1

print()
print(f"Resultado: {checks}/4 OK")

if checks == 4:
    print("CONFORME")
else:
    print("NO CONFORME")
