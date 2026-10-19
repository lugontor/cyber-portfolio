# Informe de incidente: denegación de servicio mediante inundación ICMP

Actividad del curso 3 del Certificado Profesional de Ciberseguridad de Google. Caso simulado de una empresa multimedia que ofrece diseño web, diseño gráfico y marketing en redes sociales.

## Resumen del incidente

La empresa sufrió un ataque de denegación de servicio (DoS) mediante una avalancha de paquetes ICMP que dejó los servicios de su red interna sin responder durante dos horas. El tráfico legítimo no pudo acceder a los recursos de red porque un cortafuegos sin configurar adecuadamente permitió el paso del tráfico del atacante.

El equipo de gestión de incidentes bloqueó los paquetes ICMP entrantes, dejó fuera de línea los servicios no críticos y restableció los servicios críticos. Tras investigar la causa, el equipo implementó una regla de limitación de tasa de ICMP, comprobaciones de IP de origen para detectar posibles direcciones falsificadas, supervisión de tráfico y un IDS/IPS con filtros para tráfico sospechoso.

El impacto confirmado afecta a la disponibilidad de la red. El escenario no aporta pruebas de robo de información, alteración de datos ni compromiso de los equipos finales.

## Método y límites

El análisis sigue las cinco funciones solicitadas en la actividad: Identificar, Proteger, Detectar, Responder y Recuperar. Se utiliza la estructura del NIST CSF presentada en el curso, sin afirmar que sea una evaluación completa del marco.

La única fuente recibida es el escenario de la actividad. No se han facilitado registros, capturas de tráfico, inventario de equipos, direcciones IP, fechas exactas, la plantilla descargable ni el ejemplo de solución. Se distinguen los hechos descritos de las medidas propuestas; no se han realizado pruebas técnicas.

## 1. Identificar

| Elemento | Hallazgo basado en el escenario |
|---|---|
| Tipo de ataque | DoS mediante inundación ICMP o ICMP flood. No hay evidencia para clasificarlo como ataque distribuido (DDoS). |
| Vector de entrada | Tráfico ICMP entrante que atravesó un cortafuegos sin la configuración necesaria para limitarlo. |
| Causa identificada | Configuración insuficiente del cortafuegos frente a la avalancha de paquetes. |
| Recurso afectado | Capacidad de la red interna para atender tráfico legítimo y permitir el acceso a sus recursos. |
| Servicios afectados | Los servicios de red dejaron de responder; los no críticos se desconectaron como medida de contención y se restablecieron los críticos. El escenario no identifica aplicaciones concretas. |
| Dispositivos implicados | El cortafuegos es el dispositivo de control identificado. No se enumeran routers, switches, servidores ni estaciones de trabajo concretos afectados o comprometidos. |
| Duración e impacto | Dos horas de interrupción; los usuarios no podían acceder a los recursos de red mediante el tráfico normal. |
| Origen y alcance desconocidos | No se proporciona IP de origen, número de emisores, volumen de tráfico ni identidad del atacante. La comprobación de IP implantada después no prueba que este ataque utilizara suplantación. |

**Acciones propuestas para completar la identificación:** mantener un inventario de dispositivos, servicios y dependencias; asignar responsables y prioridad de recuperación; revisar periódicamente reglas de cortafuegos y privilegios administrativos; documentar el tráfico habitual y las necesidades legítimas de ICMP. Conservar las configuraciones previas y posteriores al incidente para analizar la brecha de control.

## 2. Proteger

### Medidas ya implantadas según el caso

- Regla de cortafuegos para limitar la tasa de paquetes ICMP entrantes.
- Verificación de la dirección IP de origen para identificar posibles paquetes con direcciones falsificadas.
- Supervisión de red y sistema IDS/IPS para reconocer y filtrar tráfico sospechoso.

### Plan de mejora propuesto

| Acción | Responsable propuesto | Comprobación de eficacia |
|---|---|---|
| Revisar y documentar las reglas del cortafuegos, restringiendo tráfico innecesario y limitando ICMP según las necesidades de la red | Administración de red | Prueba autorizada y controlada que confirme el filtrado y el funcionamiento del tráfico legítimo. |
| Ajustar las comprobaciones de origen a la topología y rutas válidas | Administración de red | Revisar registros de descartes y comprobar que no se bloquean rutas legítimas. Una IP aparentemente válida no demuestra que el tráfico sea benigno. |
| Proteger el acceso administrativo con permisos mínimos, autenticación reforzada y registro de cambios | TI y seguridad | Revisión de cuentas y trazabilidad de modificaciones. |
| Mantener copias verificadas de configuraciones de dispositivos y un procedimiento de reversión | Administración de red | Recuperación de una configuración conocida en un entorno de prueba. |
| Formar al personal de TI y establecer revisión y aprobación de cambios | Responsable de seguridad | Simulación de respuesta y revisión de cambios documentados. |
| Acordar un procedimiento de mitigación con el proveedor de conectividad | Responsable de TI y proveedor | Confirmar contactos, criterios de escalado y opciones de filtrado aguas arriba si el enlace se satura. |

El bloqueo total de ICMP se recoge como contención aplicada durante el incidente. Para la operación habitual se propone filtrado selectivo y limitación de tasa, validando las funciones legítimas de diagnóstico y señalización de errores de red.

## 3. Detectar

1. **Supervisar el tráfico continuamente.** Establecer una línea base de paquetes ICMP por segundo, ancho de banda, orígenes, destinos y tipos de mensaje; generar alertas ante aumentos anómalos sostenidos.
2. **Correlacionar señales.** Relacionar alertas del IDS/IPS y registros del cortafuegos con pérdida de paquetes, latencia, errores de acceso, disponibilidad de servicios y uso de recursos del dispositivo.
3. **Vigilar accesos y cambios.** Registrar inicios de sesión administrativos, fallos de autenticación, creación de cuentas y cambios de reglas; investigar actividad que no corresponda a usuarios autorizados o cambios aprobados. Estas son medidas preventivas adicionales, no evidencias de que hubiera cuentas comprometidas.
4. **Centralizar y conservar evidencias.** Reunir registros con marcas temporales sincronizadas y, cuando sea viable, muestras de tráfico con acceso restringido para permitir la investigación.
5. **Ajustar alertas.** Definir umbrales según la capacidad y el comportamiento real de la red, asignar responsables y probar las alertas para reducir falsos positivos.

**Criterio propuesto de investigación:** un aumento de ICMP acompañado de degradación del servicio o alertas de filtrado debe abrir un incidente para su validación. No se fijan umbrales numéricos sin conocer la capacidad de la infraestructura.

## 4. Responder

### Respuesta observada en el incidente

El equipo bloqueó ICMP entrante, desconectó temporalmente servicios no críticos y restableció los servicios críticos. La investigación posterior identificó la configuración del cortafuegos como la debilidad aprovechada y dio lugar a los controles descritos en el resumen.

### Procedimiento propuesto para futuros incidentes

1. **Validar y activar el proceso.** Confirmar si las alertas corresponden a tráfico hostil y evaluar qué servicios han perdido disponibilidad. Designar un coordinador y avisar a TI, seguridad y responsables de negocio.
2. **Registrar y preservar.** Documentar la hora de detección, síntomas, servicios afectados y decisiones; conservar registros del cortafuegos, IDS/IPS, métricas de tráfico, muestras disponibles y configuraciones antes y después de los cambios. Evitar que la recopilación retrase una contención urgente.
3. **Contener.** Aplicar filtrado temporal y limitación de tasa al tráfico malicioso; priorizar servicios críticos y reducir cargas no esenciales. Aislar dispositivos solo si aparecen indicios de compromiso, pues una inundación de tráfico no lo demuestra por sí sola.
4. **Escalar cuando sea necesario.** Si la capacidad del enlace se satura, solicitar mitigación al proveedor de conectividad; los filtros locales pueden resultar insuficientes cuando la congestión se produce antes de llegar a la red.
5. **Neutralizar y corregir.** Ajustar la configuración vulnerable, comprobar que el tráfico dañino queda mitigado y validar que las reglas permiten las comunicaciones necesarias.
6. **Comunicar.** Informar a las partes afectadas del impacto, las acciones y el estado de recuperación mediante un canal disponible. Registrar responsables y decisiones.
7. **Revisar lo aprendido.** Analizar la causa, los tiempos de detección y contención y la eficacia de los controles; asignar mejoras con responsables y verificar su cierre.

## 5. Recuperar

1. Confirmar que el tráfico hostil ha cesado o está contenido y que las métricas de red se han estabilizado.
2. Verificar la configuración del cortafuegos, el funcionamiento del IDS/IPS y la capacidad de la red; recuperar configuraciones conocidas si se detectaron cambios incorrectos.
3. Restablecer primero los servicios críticos según las prioridades del negocio y validar conectividad y acceso de usuarios autorizados con los responsables de cada servicio.
4. Reactivar los servicios no críticos de forma gradual, comprobando que no reaparecen la saturación ni los fallos.
5. Recuperar inmediatamente la información operativa necesaria: inventario de servicios y dependencias, configuraciones válidas, contactos de respuesta y registros del incidente. Restaurar datos desde copias únicamente si se verifica pérdida o corrupción; el escenario no documenta ninguna.
6. Revisar las restricciones temporales y sustituirlas por controles permanentes probados cuando proceda.
7. Mantener supervisión reforzada durante un periodo acordado según el riesgo y confirmar con el negocio que se ha recuperado el servicio.
8. Cerrar el incidente cuando los servicios requeridos funcionen, las medidas estén verificadas y queden documentadas las evidencias, las acciones pendientes y sus responsables.

## Autoevaluación

| Criterio | Resultado | Evidencia en el informe |
|---|---|---|
| Incluye un resumen del incidente | Sí | Causa, duración, impacto y respuesta en el resumen. |
| Identifica tipo de ataque y alcance, incluidos sistemas o dispositivos afectados | Sí | Sección Identificar: DoS por ICMP, red y servicios afectados, cortafuegos implicado y límites de la información disponible. |
| Ofrece un plan para proteger la red | Sí | Medidas existentes y plan de mejora en Proteger. |
| Describe métodos de detección futura | Sí | Supervisión, correlación, alertas y seguimiento de accesos en Detectar. |
| Describe un proceso de respuesta a incidentes similares | Sí | Procedimiento de validación, contención, análisis, comunicación y mejora en Responder. |
| Enumera procedimientos de recuperación | Sí | Restauración gradual, validaciones y criterios de cierre en Recuperar. |

Los seis criterios están cubiertos en esta revisión. La comparación con el ejemplo del curso queda pendiente porque ese material no se ha facilitado.

## Aprendizajes

Este caso muestra cómo una configuración insuficiente puede afectar a la disponibilidad de toda una red. La respuesta requiere combinar filtrado, detección, coordinación y recuperación comprobada, distinguiendo los hechos observados de las hipótesis y las mejoras propuestas.
