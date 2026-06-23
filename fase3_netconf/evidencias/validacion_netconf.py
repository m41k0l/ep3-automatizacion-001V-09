from ncclient import manager
from datetime import datetime

ROUTER = "192.168.56.103"
USER = "cisco"
PASS = "cisco123!"

print("="*60)
print("VALIDACION NETCONF")
print("Alumno: Maikol Luis Mamani Segobia")
print("Codigo: 001V-09")
print("Fecha:", datetime.now())
print("="*60)

with manager.connect(
    host=ROUTER,
    port=830,
    username=USER,
    password=PASS,
    hostkey_verify=False
) as m:

    print("\n[OK] Conexion NETCONF establecida")

    filtro = """
    <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
    </filter>
    """

    respuesta = m.get_config("running", filtro)

    xml = respuesta.xml

    with open("rpc_reply_raw.xml", "w") as f:
        f.write(xml)

    checks = 0

    if "RTR-MEDAND" in xml:
        print("[OK] Hostname corporativo")
        checks += 1

    if "10.1.9.1" in xml:
        print("[OK] Loopback configurada")
        checks += 1

    if "Enlace-WAN-Rancagua" in xml:
        print("[OK] Descripcion WAN")
        checks += 1

    if "1.1.1.1" in xml:
        print("[OK] Servidor NTP")
        checks += 1

    if m.connected:
        print("[OK] NETCONF habilitado")
        checks += 1

    print(f"\nResultado: {checks}/5 OK")

    if checks == 5:
        print("CONFORME")
    else:
        print("NO CONFORME")
