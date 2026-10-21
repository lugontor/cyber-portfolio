# Algoritmo para la actualización de archivos en Python

## Descripción del proyecto

En este escenario educativo, trabajo como profesional de seguridad de una empresa de atención sanitaria que controla el acceso a una subred restringida mediante una lista de direcciones IP permitidas. Esta subred permite acceder a contenido relacionado con registros personales de pacientes. He desarrollado un algoritmo en Python que lee el archivo de permitidos, identifica las direcciones incluidas en una lista de eliminación y las retira. Finalmente, el algoritmo guarda la lista revisada en el mismo archivo para mantener actualizado el registro de accesos autorizados.

## Alcance y materiales

Esta actividad reproduce el procedimiento solicitado con código escrito, una alternativa a las capturas de pantalla admitida en el enunciado. Los datos de ejemplo son ficticios y no representan empleados, pacientes ni infraestructura real. No se han proporcionado los archivos originales del laboratorio ni las nueve preguntas finales; la comprobación usa datos propios y la tabla de autoevaluación revisa los requisitos disponibles.

- [Código ejecutable](actualizar_lista.py)
- [Lista de permitidos de ejemplo](allow_list.txt)
- [Resultado esperado del ejemplo](resultado_esperado.txt)

El archivo de entrada contiene una IP por línea, sin encabezados ni duplicados. La lista `remove_list` se define en el código y representa las direcciones cuyo acceso debe revocarse. Actualizar este archivo es la tarea del ejercicio: por sí solo, el script no modifica reglas de firewall ni demuestra una revocación efectiva en una red real.

## 1. Abrir el archivo que contiene la lista de permitidos

```python
import_file = "allow_list.txt"

with open(import_file, "r", encoding="utf-8") as file:
    ip_addresses = file.read()
```

La asignación `=` guarda el nombre del archivo como cadena en la variable `import_file`. La función `open()` abre ese archivo; el modo `"r"` indica lectura y `encoding="utf-8"` establece la codificación del texto. La sentencia `with` administra el contexto del archivo y lo cierra automáticamente al salir del bloque, incluso si se produce una excepción dentro de él. La palabra clave `as` asigna el objeto de archivo a `file`; los dos puntos y la sangría delimitan las instrucciones que se ejecutan dentro del contexto.

## 2. Leer el contenido del archivo

```python
with open(import_file, "r", encoding="utf-8") as file:
    ip_addresses = file.read()
```

El método `.read()`, llamado sobre `file`, lee todo el contenido y lo devuelve como una cadena. La asignación almacena esa cadena en `ip_addresses`, incluidos los saltos de línea. La lectura se realiza dentro del bloque `with`, mientras el archivo está abierto; después del cierre, la variable conserva el texto en memoria.

## 3. Convertir la cadena en una lista

```python
ip_addresses = ip_addresses.split()
```

El método `.split()` sin argumentos divide la cadena por espacios en blanco, incluidos saltos de línea y tabulaciones. Devuelve una lista de cadenas, en la que cada elemento representa una dirección IP, y omite los espacios en blanco consecutivos. Al reasignar el resultado, `ip_addresses` pasa de contener una cadena a contener una lista que puede modificarse.

## 4. Iterar a través de la lista de eliminados

```python
remove_list = ["192.0.2.20", "198.51.100.30", "203.0.113.99"]

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)
```

Los corchetes definen la lista `remove_list`. El encabezado `for element in remove_list:` recorre sus elementos y asigna cada dirección, sucesivamente, a la variable `element`. La palabra clave `in` del encabezado indica la colección que se recorre. El cuerpo con sangría se ejecuta una vez por cada dirección de esa lista.

## 5. Eliminar direcciones IP que están en la lista de eliminación

```python
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)
```

La sentencia condicional `if` comprueba si la dirección actual está en `ip_addresses`; aquí, `in` realiza una prueba de pertenencia. Cuando la condición es verdadera, `.remove(element)` elimina la primera aparición de esa dirección de la lista. Si la dirección no existe, se omite la eliminación, evitando el `ValueError` que produciría intentar eliminar un elemento ausente. Se recorre `remove_list`, mientras se modifica una lista diferente, `ip_addresses`.

**Aplicar `.remove()` de esta manera es posible porque no hay duplicados en la lista `ip_addresses`.** Si hubiera duplicados, una sola llamada no eliminaría todas las apariciones; habría que validar esa condición o adaptar el algoritmo. Las IP se comparan como cadenas exactas; este ejercicio no valida su formato ni normaliza representaciones equivalentes.

## 6. Actualizar el archivo con la lista revisada de direcciones IP

```python
ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w", encoding="utf-8") as file:
    file.write(ip_addresses)
```

El método `.join()` une las cadenas de la lista usando el separador sobre el que se invoca. En este caso, `"\n"` coloca cada IP en una línea distinta y el resultado se reasigna a `ip_addresses`, que vuelve a ser una cadena. Una segunda sentencia `with` abre el archivo en modo `"w"`, que reemplaza su contenido anterior, y `.write()` escribe la cadena revisada. Al finalizar el bloque, el archivo se cierra automáticamente; si la lista queda vacía, se escribe una cadena vacía.

El modo `"w"` trunca el archivo al abrirlo: para esta práctica se usa únicamente la copia de ejemplo. En un entorno operativo, una copia de seguridad y una escritura mediante archivo temporal permitirían reducir el riesgo de pérdida de datos ante un fallo.

## Código completo

El siguiente código también está disponible en [actualizar_lista.py](actualizar_lista.py).

```python
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
```

## Ejemplo reproducible y verificación

Desde la carpeta del proyecto, ejecutar `python3 actualizar_lista.py`. El nombre relativo `allow_list.txt` se resuelve desde la carpeta de trabajo actual, por lo que se debe ejecutar allí. El script sobrescribe la lista de ejemplo; para repetir el caso inicial, hay que restaurar su contenido.

**Entrada ficticia:**

```text
192.0.2.10
192.0.2.20
198.51.100.30
203.0.113.40
```

**Lista de eliminación:** `192.0.2.20`, `198.51.100.30` y `203.0.113.99`.

**Resultado esperado:**

```text
192.0.2.10
203.0.113.40
```

Las dos direcciones presentes en ambas listas se eliminan y las demás conservan su orden. La dirección `203.0.113.99` no estaba en el archivo y no provoca un error. La cadena escrita no añade un salto de línea al final.

La verificación local ejecutó el código en archivos temporales y comprobó seis casos: el ejemplo anterior, ninguna coincidencia, eliminación de todas las IP, archivo vacío, separadores en blanco variados y repetición de la ejecución. En todos los casos, el contenido escrito coincidió con el esperado. Estas pruebas verifican el comportamiento con datos ficticios, no la ejecución del laboratorio de Coursera.

## Autoevaluación de los requisitos disponibles

| Criterio | Evidencia |
|---|---|
| Descripción inicial de tres a cinco frases | Cuatro frases en la descripción del proyecto. |
| Capturas o versiones escritas del código | Fragmentos por paso y código completo ejecutable. |
| Explicación de sintaxis, funciones y palabras clave | Asignaciones, sangría, dos puntos, variables y métodos explicados. |
| Uso de `with` y `open()` | Apertura, modos de acceso y cierre automático en los pasos 1 y 6. |
| Uso de `.read()` y `.write()` | Lectura y sustitución del contenido en los pasos 2 y 6. |
| Conversión mediante `.split()` | Paso 3. |
| Recorrido mediante `for` | Paso 4, con `element` y `remove_list`. |
| Condicional, `.remove()` y ausencia de duplicados | Paso 5. |
| Uso de `"\n".join()` y resumen de cuatro a seis frases | Paso 6 y resumen final de cinco frases. |

Esta tabla comprueba el enunciado recibido; no sustituye las nueve preguntas de la plataforma, cuyo texto no estaba incluido.

## Resumen

El algoritmo abre la lista de permitidos mediante `with` y `open()`, y obtiene su contenido con `.read()`. A continuación, `.split()` convierte el texto en una lista de direcciones IP. Un bucle `for` recorre `remove_list` y una condición de pertenencia permite eliminar con `.remove()` las direcciones presentes, bajo el supuesto de que no hay duplicados. Después, `"\n".join()` reconstruye el texto y `.write()` guarda el resultado en el archivo original. Esta práctica demuestra cómo automatizar el mantenimiento de una lista de acceso mediante lectura de archivos, procesamiento de listas, condiciones y escritura en Python.
