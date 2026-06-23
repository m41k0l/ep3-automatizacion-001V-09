from datetime import datetime
import os

ALUMNO = "Maikol Luis Mamani Segobia"
CODIGO = "001V-09"

netconf_ok = False
restconf_ok = False
diff_ok = False

try:
    with open("../fase3_netconf/evidencias/output_validacion_netconf.txt") as f:
        netconf_ok = "CONFORME" in f.read()
except:
    pass

try:
    with open("../fase4_restconf/evidencias/output_validacion_restconf.txt") as f:
        restconf_ok = "CONFORME" in f.read()
except:
    pass

if os.path.exists("evidencias/diff_001V-09"):
    diff_ok = True

resultado = "CONFORME" if (netconf_ok and restconf_ok and diff_ok) else "NO CONFORME"

archivo = f"evidencias/certificado_compliance_{CODIGO}.txt"

with open(archivo, "w") as f:
    f.write("="*50 + "\n")
    f.write("CERTIFICADO DE COMPLIANCE\n")
    f.write("="*50 + "\n")
    f.write(f"Alumno: {ALUMNO}\n")
    f.write(f"Codigo: {CODIGO}\n")
    f.write(f"Fecha: {datetime.now()}\n\n")
    f.write(f"NETCONF: {'CONFORME' if netconf_ok else 'NO CONFORME'}\n")
    f.write(f"RESTCONF: {'CONFORME' if restconf_ok else 'NO CONFORME'}\n")
    f.write(f"COMPLIANCE: {resultado}\n")

print("Resultado:", resultado)
print("Certificado generado:", archivo)
