# Diario del gestor de incidentes

Registro de análisis de escenarios del Certificado Profesional de Ciberseguridad de Google. Las entradas son prácticas educativas y no representan investigaciones realizadas en organizaciones reales.

## Entrada 1 — Ransomware en una clínica sanitaria

**Fecha de la anotación:** 19 de octubre de 2026.  
**Número de entrada:** 1.

### Descripción

Documentación y análisis de un incidente de ransomware en una pequeña clínica estadounidense de atención primaria. El ataque comenzó mediante correos de phishing dirigidos con un archivo adjunto malicioso y provocó el cifrado de archivos críticos, la pérdida de acceso a registros médicos y la interrupción de las operaciones.

### Herramientas utilizadas

No se utilizaron herramientas de análisis técnico: esta entrada se basa en la revisión del escenario proporcionado. No se facilitaron registros, muestras de malware, correos originales ni imágenes forenses.

### Las 5 W

| Pregunta | Detalles de la investigación documental |
|---|---|
| **¿Quién causó el incidente? — Who** | Un grupo organizado de ciberdelincuentes, descrito en el escenario como conocido por atacar organizaciones de sanidad y transporte. No se proporciona su nombre ni evidencia técnica para verificar su identidad. |
| **¿Qué ocurrió? — What** | Los atacantes desplegaron ransomware que cifró archivos críticos, impidiendo que los empleados accedieran a registros médicos y programas necesarios para trabajar. Apareció una nota que exigía una gran suma de dinero a cambio de una clave de descifrado, y la clínica apagó sus sistemas y solicitó asistencia externa. |
| **¿Cuándo ocurrió? — When** | El incidente se manifestó un martes por la mañana, aproximadamente a las 9:00. El escenario no especifica la fecha exacta, la zona horaria, el momento del acceso inicial ni la duración total de la interrupción. |
| **¿Dónde ocurrió? — Where** | En la red y los sistemas informáticos de una pequeña clínica sanitaria de atención primaria situada en Estados Unidos. No se identifican su ciudad, sus servidores ni el número exacto de equipos afectados. |
| **¿Por qué ocurrió? — Why** | El escenario atribuye el acceso inicial a correos de phishing dirigidos cuyo adjunto malicioso instaló malware tras descargarse, permitiendo el posterior despliegue de ransomware. La exigencia de dinero indica una motivación de extorsión; no se describen los controles existentes ni la causa técnica concreta que permitió ejecutar el adjunto. |

### Notas adicionales

¿Existían copias de seguridad aisladas y verificadas para recuperar los registros médicos, y qué procedimiento de continuidad permitía atender a los pacientes mientras los sistemas estaban fuera de servicio? También investigaría si se produjo extracción de datos antes del cifrado, ya que el escenario no la confirma y el cifrado por sí solo no demuestra una filtración.

## Autoevaluación de la entrada

| Criterio | Comprobación |
|---|---|
| Entrada fechada y numerada | Sí: fecha real de documentación y entrada 1. |
| Descripción incluida | Sí: identifica el incidente y su impacto operativo. |
| Detalles mediante las 5 W | Sí: cada pregunta tiene una respuesta de una o dos frases y señala los datos desconocidos. |
| Pensamientos o preguntas adicionales | Sí: dos frases sobre recuperación, continuidad y posible extracción de datos. |
| Corrección gramatical, ortográfica y de puntuación | Texto revisado. |

La fecha de documentación no se presenta como la fecha del ataque. No se afirma que se hayan usado herramientas, restaurado archivos, pagado un rescate o verificado una filtración; esos hechos no constan en el escenario.

## Fuente y continuidad del diario

Fuente: instrucciones y escenario de la actividad facilitados por el usuario. La plantilla descargable y el modelo de solución no se han proporcionado; esta entrada reproduce los campos solicitados en las instrucciones.

Las siguientes actividades se incorporarán como entradas consecutivas, conservando la fecha real de cada anotación y distinguiendo observaciones, hipótesis y cuestiones pendientes.
