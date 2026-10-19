# Gestión de permisos de archivos en Linux

## Descripción del proyecto

En este escenario educativo, el equipo de investigación necesita revisar los permisos de sus archivos y directorios para ajustarlos a las autorizaciones de la organización. El objetivo es utilizar `ls -la` para examinar los permisos y `chmod` para retirar accesos innecesarios, proteger un archivo archivado y restringir el directorio de borradores a su propietario. Esta versión documenta el procedimiento y los resultados esperados; queda pendiente incorporar los permisos originales del laboratorio para verificar los cambios.

## Estado y materiales

**Estado: procedimiento preparado; verificación del laboratorio pendiente.**

Se han recibido las instrucciones, pero no el documento «Permisos de archivo actuales» ni salidas o capturas del laboratorio. Los bloques siguientes son versiones mecanografiadas de comandos propuestos y ejemplos didácticos claramente identificados, no una transcripción de comandos ejecutados. Se parte de la ubicación en el directorio `projects` del laboratorio; su ruta absoluta no se ha proporcionado.

## Comprobar detalles de archivos y directorios

Desde el directorio `projects`:

```bash
pwd
ls -la
ls -ld drafts
```

- `pwd` permite confirmar el directorio de trabajo antes de modificar permisos.
- `ls -la` combina el formato largo (`-l`) con la inclusión de entradas ocultas (`-a`). Muestra permisos, número de enlaces, propietario, grupo, tamaño, fecha y nombre.
- `ls -ld drafts` muestra los permisos del propio directorio `drafts`; sin `-d`, normalmente se listaría su contenido.
- Las entradas `.` y `..` representan el directorio actual y el superior. Un nombre que comienza por punto, como `.project_x.txt`, queda oculto en un listado ordinario; eso no constituye protección de acceso.

**Evidencia pendiente:** incorporar el listado inicial completo para identificar todos los archivos y sus permisos reales, incluidos el propietario `researcher2`, el grupo y los archivos ocultos.

## Interpretar la cadena de 10 caracteres

Ejemplo didáctico de un archivo regular con escritura para otros:

```text
-rw-rw-rw-
```

| Posición | Carácter del ejemplo | Significado |
|---|---|---|
| 1 | `-` | Archivo regular; `d` indicaría un directorio. |
| 2 | `r` | El propietario puede leer. |
| 3 | `w` | El propietario puede escribir. |
| 4 | `-` | El propietario no tiene permiso de ejecución. |
| 5 | `r` | El grupo puede leer. |
| 6 | `w` | El grupo puede escribir. |
| 7 | `-` | El grupo no tiene permiso de ejecución. |
| 8 | `r` | Otros usuarios pueden leer. |
| 9 | `w` | Otros usuarios pueden escribir. |
| 10 | `-` | Otros usuarios no tienen permiso de ejecución. |

Los tres bloques se refieren al propietario (`u`), grupo (`g`) y otros usuarios (`o`). En archivos regulares, `r` permite leer, `w` modificar el contenido y `x` ejecutar. En directorios, `r` permite listar nombres, `w` modificar entradas y `x` atravesar el directorio y acceder a sus entradas, sujeto a los demás permisos necesarios.

## Cambiar permisos de archivo

La organización prohíbe la escritura de otros usuarios en los archivos. Primero es necesario identificar qué archivos tienen el carácter `w` en la novena posición; sus nombres no aparecen en las instrucciones recibidas.

Desde `projects`, este comando de consulta identifica los archivos regulares directamente contenidos en él con escritura para otros, incluidos los ocultos:

```bash
find . -maxdepth 1 -type f -perm -0002 -print
```

**Salida esperada:** las rutas de los archivos que requieren corrección, o ninguna línea si no hay coincidencias. No se conocen aún los nombres reales.

Para cada archivo identificado se utiliza `chmod o-w`. Ejemplo de sintaxis, donde debe sustituirse `ARCHIVO_IDENTIFICADO` por el nombre obtenido:

```bash
chmod o-w -- ARCHIVO_IDENTIFICADO
ls -l -- ARCHIVO_IDENTIFICADO
```

`o` selecciona otros usuarios, `-` retira un permiso y `w` representa escritura. La operación conserva los demás permisos. Si el archivo tuviera la cadena didáctica `-rw-rw-rw-`, el resultado esperado sería `-rw-rw-r--`.

`chmod` normalmente no imprime salida cuando tiene éxito; el listado posterior permite comprobar el resultado. Un error debe investigarse antes de dar por realizado el cambio. La consulta con `-maxdepth 1` no inspecciona los archivos de subdirectorios; deben revisarse por separado si forman parte del alcance.

## Cambiar los permisos de un archivo oculto

El archivo archivado `.project_x.txt` debe permitir lectura al propietario y al grupo, sin escritura para nadie. Se propone también retirar cualquier ejecución y el acceso de otros usuarios para establecer un estado explícito:

```bash
ls -l .project_x.txt
chmod u=r,g=r,o= .project_x.txt
ls -l .project_x.txt
```

- `u=r` asigna únicamente lectura al propietario.
- `g=r` asigna únicamente lectura al grupo.
- `o=` retira todos los permisos de otros usuarios.
- El operador `=` establece exactamente los permisos indicados.

La forma numérica equivalente es `chmod 440 .project_x.txt`: lectura vale 4, escritura 2 y ejecución 1.

**Cadena final esperada:**

```text
-r--r-----
```

Esta configuración cumple la lectura de propietario y grupo y elimina la escritura para los tres grupos de permisos. El punto inicial del nombre no cambia cómo funciona `chmod`.

## Cambiar los permisos del directorio

El escenario indica que `researcher2` es el propietario y debe ser el único usuario ordinario con acceso a `drafts` y su contenido.

```bash
ls -ld drafts
chmod u=rwx,go= drafts
ls -ld drafts
```

`u=rwx` permite al propietario listar, modificar y atravesar el directorio. `go=` elimina los permisos del grupo y de otros usuarios. Su equivalente numérico es `chmod 700 drafts`.

**Cadena final esperada:**

```text
drwx------
```

En el modelo básico de permisos del ejercicio, retirar el acceso al directorio impide que grupo y otros accedan a sus archivos a través de esa ruta, aunque los permisos individuales de estos archivos no se modifican. Se debe comprobar que el propietario sea realmente `researcher2`; estas restricciones no impiden el acceso de un administrador con privilegios suficientes.

## Verificación final propuesta

```bash
ls -la
ls -ld drafts
find . -maxdepth 1 -type f -perm -0002 -print
```

Se debe confirmar que:

- Ningún archivo regular revisado permita escritura a otros usuarios.
- `.project_x.txt` muestre `-r--r-----`.
- `drafts` muestre `drwx------` y pertenezca a `researcher2`.
- Los permisos de lectura y trabajo necesarios para el equipo se conserven en el resto de los archivos.

Estas comprobaciones están pendientes de realizarse con los datos del laboratorio.

## Revisión de los ocho criterios

| Criterio | Estado de esta versión |
|---|---|
| Capturas o versiones mecanografiadas de comandos | Incluye comandos mecanografiados; no se presentan como ejecutados. |
| Descripción del proyecto al principio | Incluida, en tres frases. |
| Explicación de comandos y salida | Incluida; se distinguen ejemplos y resultados esperados de evidencia real. |
| Resumen al final | Incluido, en tres frases. |
| Uso de chmod | Explicado con notación simbólica y equivalencias numéricas. |
| Comprobación con ls -la | Explicada al inicio y en la verificación final. |
| Interpretación de la cadena de 10 caracteres | Desglosada posición por posición. |
| Archivos ocultos y directorios | Explicados y tratados en secciones propias. |

Para cerrar la actividad faltan los permisos iniciales reales, el nombre del archivo que requiere retirar escritura a otros y la comprobación final. También queda pendiente comparar con el modelo del curso, que no se ha facilitado.

## Resumen

El procedimiento documenta cómo examinar permisos con `ls -la` e interpretar sus diez caracteres para distinguir los accesos del propietario, grupo y otros usuarios. Propone utilizar `chmod` para retirar escritura no autorizada, dejar un archivo oculto en modo de solo lectura y limitar un directorio a su propietario. La validación con los permisos reales del laboratorio permitirá confirmar que los cambios cumplen las autorizaciones del equipo de investigación.
