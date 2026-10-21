"""Actividad educativa: actualizar una lista de IP permitidas.
Ejecutar desde esta carpeta: python3 actualizar_lista.py
Los datos incluidos son ficticios y el archivo allow_list.txt se sobrescribe.
"""

import_file = "allow_list.txt"
remove_list = ["192.0.2.20", "198.51.100.30", "203.0.113.99"]

# Leer el archivo y convertir su contenido en una lista.
with open(import_file, "r", encoding="utf-8") as file:
    ip_addresses = file.read()

ip_addresses = ip_addresses.split()

# La lista de permitidos no contiene duplicados.
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Guardar las IP restantes, una por línea.
ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w", encoding="utf-8") as file:
    file.write(ip_addresses)
