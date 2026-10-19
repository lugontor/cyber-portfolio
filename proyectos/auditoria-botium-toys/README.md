# Auditoría interna de seguridad: Botium Toys

Práctica educativa del Certificado Profesional de Ciberseguridad de Google en Coursera. Botium Toys es una empresa ficticia. Evaluación documental: no se han realizado pruebas técnicas ni una auditoría real de la empresa.

## Alcance y objetivos

El alcance abarca todo el programa de seguridad, sus activos y los procesos y procedimientos internos relativos a controles y buenas prácticas de cumplimiento. El objetivo es evaluar las medidas existentes e identificar cuáles deben implantarse o reforzarse.

Los activos descritos incluyen equipos de oficina y de empleados, estaciones remotas, productos del almacén y la tienda, sistemas de contabilidad y comercio electrónico, bases de datos, telecomunicaciones, gestión de inventario, red interna, acceso a Internet, almacenamiento de datos y sistemas antiguos.

## Fuentes y método

Se revisaron los tres documentos proporcionados en la actividad:

1. *Botium Toys: Scope, goals, and risk assessment report*.
2. *Control categories*.
3. *Controls and compliance checklist*.

Las respuestas se basan exclusivamente en ese escenario. En controles, “Sí” significa que el informe describe su existencia; las deficiencias se explican por separado. En cumplimiento, “Sí” significa que el escenario respalda la práctica concreta de la plantilla. Estas respuestas no certifican el cumplimiento integral de PCI DSS, GDPR ni SOC.

## Evaluación de riesgos

El informe asigna un riesgo de **8/10** y califica como medio el impacto potencial de perder un activo. La falta de inventario y clasificación limita la fiabilidad de esa valoración del impacto; no debe interpretarse como evidencia de que los activos críticos estén protegidos.

| Personas o recursos afectados | Riesgo y causa |
|---|---|
| Clientes | Exposición de datos personales y de tarjetas por acceso excesivo y ausencia de cifrado. |
| Empleados | Sus cuentas podrían utilizarse para acceder a información innecesaria para su función; las contraseñas débiles y la falta de separación de funciones amplían el impacto de una cuenta comprometida. |
| Datos y operaciones | Pérdida de información y periodos prolongados de interrupción por ausencia de copias y planes de recuperación. |
| Infraestructura | Detección insuficiente de intrusiones y exposición de sistemas antiguos por mantenimiento irregular. |
| Empresa | Posibles pérdidas económicas, consecuencias de incumplimiento y daño reputacional, según los riesgos descritos en el caso. |

## Lista de controles

| Control | ¿Existe? | Evidencia y valoración |
|---|---|---|
| Mínimo privilegio | No | Todos los empleados tienen acceso a los datos internos y podrían acceder a datos personales y de tarjetas. |
| Planes de recuperación ante desastres | No | El informe declara que no existen. |
| Políticas de contraseñas | Sí | Existe una política, pero sus requisitos son débiles y el informe los considera insuficientes. Su existencia no implica eficacia. |
| Separación de funciones | No | El informe indica que no se ha implementado. |
| Cortafuegos | Sí | Filtra tráfico con un conjunto de reglas de seguridad definido. |
| Sistema de detección de intrusiones (IDS) | No | El departamento de TI no ha instalado un IDS. |
| Copias de seguridad | No | No hay copias de datos críticos. |
| Antivirus | Sí | Está instalado y TI lo supervisa regularmente. |
| Supervisión, mantenimiento e intervención manual de sistemas antiguos | Sí | Se supervisan y mantienen, pero no existe un calendario regular y los métodos de intervención no están claros: implantación parcial que requiere mejora. |
| Cifrado | No | El informe declara que no se utiliza para proteger los datos de tarjetas aceptados, procesados, transmitidos y almacenados internamente. |
| Sistema de gestión de contraseñas | No | No existe un sistema centralizado que aplique los requisitos de la política. |
| Cerraduras en oficinas, tienda y almacén | Sí | El local cuenta con cerraduras suficientes. |
| Videovigilancia CCTV | Sí | El local dispone de videovigilancia actualizada. |
| Detección y prevención de incendios | Sí | El informe describe sistemas en funcionamiento. |

**Resultado:** 7 controles presentes y 7 ausentes. Dos de los presentes —política de contraseñas y mantenimiento de sistemas antiguos— tienen deficiencias explícitas. El recuento no es una puntuación de madurez ni pondera la importancia de cada control.

## Lista de buenas prácticas de cumplimiento

### PCI DSS

| Práctica de la plantilla | ¿Se aplica? | Justificación |
|---|---|---|
| Solo usuarios autorizados acceden a datos de tarjetas de clientes | No | El acceso generalizado no está limitado según las funciones o la necesidad de uso. |
| Los datos de tarjetas se almacenan, aceptan, procesan y transmiten en un entorno interno seguro | No | Faltan restricciones de acceso y cifrado; el cortafuegos y el antivirus no compensan estas carencias. |
| Se aplican procedimientos de cifrado para proteger las transacciones y sus datos | No | El informe indica que no se utiliza cifrado. |
| Se adoptan políticas seguras de gestión de contraseñas | No | La política existente es insuficiente y no hay un sistema centralizado que aplique sus requisitos. |

### GDPR / RGPD

| Práctica de la plantilla | ¿Se aplica? | Justificación |
|---|---|---|
| Los datos de clientes de la UE se mantienen privados y seguros | No | El acceso excesivo a datos personales impide considerar garantizada su confidencialidad. |
| Existe un plan para notificar a los clientes de la UE en 72 horas si se comprometen sus datos | Sí | El informe afirma expresamente que existe ese plan. Se evalúa la redacción de la plantilla; esto no demuestra por sí solo el cumplimiento de todas las obligaciones de notificación del RGPD. |
| Los datos se clasifican e inventarían adecuadamente | No | La gestión de activos es inadecuada y el informe pide identificar y clasificar los activos existentes. |
| Se aplican políticas, procedimientos y procesos de privacidad para documentar y mantener los datos | Sí | El informe indica que se han desarrollado y se aplican entre los empleados. Esto no elimina las deficiencias de acceso. |

### SOC, según la plantilla del curso

| Práctica de la plantilla | ¿Se aplica? | Justificación |
|---|---|---|
| Se establecen políticas de acceso de usuarios | No | No se evidencia una política adecuada de acceso por funciones; faltan mínimo privilegio y separación de funciones. |
| Los datos personales sensibles se mantienen confidenciales y privados | No | Todos los empleados pueden acceder a datos internos y potencialmente a información personal sensible. |
| Existen controles para garantizar la integridad de los datos | Sí | El informe declara expresamente que TI ha integrado controles de integridad. No se han probado de forma independiente. |
| Los datos están disponibles para quienes tienen autorización de acceso | Sí | El informe declara que TI ha garantizado la disponibilidad. El exceso de permisos y la falta de recuperación siguen siendo riesgos separados. |

## Recomendaciones para la dirección de TI

Las siguientes prioridades son propuestas para este caso y no representan medidas ya implantadas.

1. **Restringir el acceso a información sensible.** Identificar responsables de los datos, aplicar mínimo privilegio y separar funciones incompatibles. Revisar los permisos de empleados y proveedores.
2. **Proteger los datos y su recuperación.** Implantar cifrado para los datos sensibles almacenados y transmitidos, con gestión de claves; establecer copias de datos críticos y comprobar su restauración; documentar y ensayar un plan de recuperación con responsables y prioridades.
3. **Inventariar y clasificar los activos.** Registrar propietarios, sensibilidad, dependencias y criticidad para revisar el impacto de su pérdida y ordenar las medidas de protección.
4. **Reforzar la autenticación.** Mejorar la política y su aplicación técnica, adoptar gestión centralizada de contraseñas y evaluar autenticación multifactor en accesos sensibles.
5. **Mejorar detección y mantenimiento.** Implantar un IDS con responsables de revisión y respuesta; establecer calendario, procedimientos de intervención y un plan de sustitución o aislamiento para sistemas antiguos.
6. **Revisar las prácticas de cumplimiento.** Verificar con los responsables correspondientes los requisitos aplicables a pagos y datos personales, incluidos destinatarios y condiciones de las notificaciones de incidentes. Mantener las políticas de privacidad, el cortafuegos, el antivirus y las protecciones físicas existentes.

## Autoevaluación de la actividad

| Pregunta | Respuesta | Evidencia |
|---|---|---|
| ¿Se revisaron el alcance, los objetivos y el informe de evaluación de riesgos? | Sí | Apartados de alcance, activos y evaluación de riesgos. |
| ¿Se consideraron los riesgos para clientes, empleados y recursos? | Sí | Tabla de personas y recursos afectados y recomendaciones. |
| ¿Se revisó el documento de categorías de control? | Sí | Se contrastaron los controles administrativos, técnicos y físicos descritos en el material. |
| ¿Se seleccionó Sí o No para cada control? | Sí | 14 controles respondidos y justificados. |
| ¿Se seleccionó Sí o No para cada buena práctica de cumplimiento? | Sí | 12 prácticas respondidas y justificadas. |

## Aprendizajes

La existencia de un control no garantiza que sea suficiente: una política de contraseñas puede existir y seguir siendo débil. También es necesario distinguir disponibilidad actual de capacidad de recuperación y evaluar confidencialidad, integridad y disponibilidad por separado. Esta actividad utiliza revisión documental y clasificación de controles; no incluye pentesting ni explotación de vulnerabilidades.
