# 1. Objetivo del Proyecto

Implementar una solución de automatización para el aprovisionamiento, validación y certificación de cumplimiento de configuración en un router Cisco IOS-XE de la empresa Centro Médico Andino SpA. El objetivo fue aplicar herramientas de automatización de red para reducir errores manuales y verificar el cumplimiento de los requerimientos corporativos.

# 2. Alcance

Se realizó el levantamiento del estado inicial del router, el aprovisionamiento automatizado mediante Ansible, la validación mediante NETCONF y RESTCONF y la generación de un reporte final de compliance. No se consideró la implementación de cambios fuera de los parámetros definidos por el cliente.

# 3. Infraestructura Utilizada

* Router Cisco CSR1000v IOS-XE
* Máquina virtual Kali Linux
* Python 3
* Ansible
* pyATS / Genie
* NETCONF
* RESTCONF
* Git y GitHub

# 4. Tecnologías Empleadas y Justificación

* pyATS/Genie: utilizado para obtener snapshots del estado del equipo y comparar configuraciones.
* Ansible: utilizado para automatizar el aprovisionamiento de configuraciones corporativas.
* NETCONF: utilizado para validar configuraciones mediante consultas basadas en YANG.
* RESTCONF: utilizado para validar configuraciones mediante API REST.

# 5. Configuración Aplicada

* Hostname: RTR-MEDAND
* Loopback0: 10.1.9.1/24
* Descripción WAN: Enlace-WAN-Rancagua
* Banner: ACCESO RESTRINGIDO - MEDAND
* Servidor NTP: 1.1.1.1
* NETCONF habilitado
* RESTCONF habilitado

# 6. Resultados de Validación

NETCONF:

* Hostname validado
* Loopback validada
* WAN validada
* NTP validado
* Resultado: CONFORME

RESTCONF:

* Hostname validado
* Loopback validada
* WAN validada
* NTP validado
* Resultado: CONFORME

# 7. Conclusiones

La configuración corporativa fue aplicada exitosamente al router CSR1000v. Las validaciones mediante NETCONF y RESTCONF confirmaron el cumplimiento de los requerimientos establecidos por el cliente. El equipo quedó preparado para ser entregado al área de operaciones.

