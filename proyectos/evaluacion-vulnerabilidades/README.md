# Evaluación de vulnerabilidades: base de datos expuesta a Internet

Práctica educativa del Certificado Profesional de Ciberseguridad de Google. Evaluación documental de una empresa ficticia de comercio electrónico.

## Descripción del sistema

La empresa utiliza un servidor remoto de base de datos que sus empleados, distribuidos por distintos países, consultan regularmente para identificar clientes potenciales. El escenario indica que la base de datos lleva tres años abierta al público.

La plantilla describe un servidor con un procesador potente, 128 GB de memoria, Linux en su versión más reciente según el caso y un gestor MySQL. Utiliza conectividad estable mediante IPv4, interactúa con otros servidores y dispone de conexiones cifradas SSL/TLS; no se especifican versiones ni configuración criptográfica. La exposición pública no demuestra por sí sola acceso anónimo, permisos de modificación ni un compromiso previo; no se han recibido registros ni una matriz de permisos.

## Alcance

Conforme a la plantilla, la evaluación se centra en los controles de acceso actuales del sistema durante tres meses: junio a agosto de 20XX. Se conserva el año ficticio del ejercicio; no se sustituye por un periodo real. Se analizan los efectos del acceso indebido sobre la confidencialidad, integridad y disponibilidad; las copias y la recuperación se consideran medidas complementarias de mitigación del impacto. No se han realizado pruebas de penetración, escaneos ni revisión de seguridad física.

## Propósito

El servidor de base de datos permite al personal remoto consultar información para identificar clientes potenciales y apoyar la actividad comercial. Evaluar su exposición pública ayuda a priorizar medidas que protejan la confidencialidad, integridad y disponibilidad de esos datos. Un acceso indebido podría revelar información comercial, alterar registros o interrumpir las consultas que necesitan los empleados. El análisis busca orientar decisiones de inversión y reducir esos riesgos sin desactivar innecesariamente un servicio del que depende el negocio.

## Método de valoración

Se utiliza una evaluación cualitativa con puntuaciones ordinales, no probabilidades estadísticas. Los conceptos de fuentes de amenaza, eventos, probabilidad e impacto se apoyan en [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final). La escala y la multiplicación siguientes son la simplificación solicitada por la actividad, no una fórmula universal prescrita por NIST.

**Horizonte de evaluación:** junio–agosto de 20XX, conforme a la plantilla. Las puntuaciones son estimaciones preliminares y deben revisarse al conocer los controles.

| Puntuación | Probabilidad | Gravedad |
|---|---|---|
| 1 — Baja | Evento poco plausible con la información disponible o con barreras eficaces verificadas. | Impacto limitado y recuperación sencilla, sin interrupción importante del trabajo. |
| 2 — Media | Evento plausible que depende de condiciones o capacidades aún no verificadas. | Afectación significativa pero acotada a información u operaciones. |
| 3 — Alta | Exposición y condiciones conocidas favorecen especialmente el evento. | Exposición amplia de datos, pérdida importante de integridad o interrupción considerable de una función crítica. |

**Riesgo = probabilidad × gravedad**, entre 1 y 9. Para priorizar en este informe se consideran 1–2 bajo, 3–4 medio y 6–9 alto; no todos los enteros se pueden obtener con esta multiplicación. Estas bandas son una convención del proyecto y no una certificación.

## Evaluación de riesgos

| Fuente de amenaza potencial | Evento que podría iniciar | Condiciones necesarias o incertidumbres | Probabilidad | Gravedad | Riesgo |
|---|---|---|---:|---:|---:|
| Actor externo con motivación económica | Obtener acceso no autorizado y extraer registros de clientes potenciales. | La exposición permite alcanzar el servicio; la extracción requeriría acceso indebido por credenciales comprometidas, configuración insegura u otra vulnerabilidad no confirmada. | 2 | 3 | 6 — Alto |
| Empleado con acceso legítimo e intención maliciosa | Exportar masivamente y divulgar información comercial fuera de su finalidad autorizada. | Los empleados consultan datos, pero se desconocen los permisos, límites de exportación y controles de supervisión. | 2 | 3 | 6 — Alto |
| Empleado autorizado que comete un error operativo | Modificar o eliminar registros por error al utilizar una cuenta con permisos excesivos. | El evento requiere permisos de escritura que no se han confirmado; debe revisarse si las cuentas de consulta pueden modificar datos. | 2 | 3 | 6 — Alto |

### Justificación de las puntuaciones

- **Extracción externa:** el servicio público presenta una oportunidad de ataque, pero no se conoce una vía efectiva de acceso a datos. Por ello, la probabilidad se mantiene en 2; una extracción amplia podría perjudicar seriamente la confidencialidad y el negocio, lo que justifica gravedad 3.
- **Divulgación interna:** el acceso habitual de empleados hace plausible el abuso de consulta o exportación, sin asumir que todos tengan acceso ilimitado. Su probabilidad se estima en 2 y su gravedad en 3 por la posible pérdida amplia de información comercial.
- **Modificación accidental:** los errores humanos son plausibles, pero el daño depende de permisos de escritura aún no verificados; se asigna probabilidad 2. Una modificación o eliminación amplia podría comprometer la integridad e impedir el trabajo comercial, por lo que se estima gravedad 3. Si las cuentas son de solo lectura, esta valoración debe reducirse.

La igualdad de puntuaciones refleja la incertidumbre, no que las amenazas sean idénticas. Tres años de exposición aumentan la necesidad de investigar el historial, pero no prueban una filtración ni permiten calcular una frecuencia real de ataque.

## Enfoque

He seleccionado una fuente externa y dos internas porque la exposición pública y el acceso habitual de empleados generan riesgos tanto de abuso como de error. Los eventos cubren divulgación, modificación y eliminación de información, vinculando el análisis al alcance de los controles de acceso. Asigno probabilidades medias porque faltan evidencias sobre autenticación, permisos y controles, y gravedades altas por una posible afectación amplia del servicio o sus datos. Las puntuaciones sirven para priorizar controles y deben revisarse al obtener evidencia técnica, no para afirmar que esos eventos ya ocurrieron.

## Remediación

Retiraría la exposición pública directa y habilitaría acceso privado mediante un canal remoto autenticado, manteniendo las consultas necesarias para el negocio. Aplicaría mínimo privilegio y el modelo AAA, con cuentas individuales, autorización por funciones, registros de actividad y MFA en el acceso remoto y administrativo. Revisaría el cifrado existente para exigir TLS seguro, protegería las claves y evaluaría cifrado del almacenamiento, sin asumir que las conexiones carecen de protección. Separaría cuentas de consulta y escritura, supervisaría exportaciones y cambios, y comprobaría las copias y los controles antes de estimar el riesgo residual.

## Plan de aplicación y verificación

Son propuestas para este caso; no medidas ya ejecutadas.

| Prioridad | Acción | Responsable propuesto | Evidencia de cierre |
|---|---|---|---|
| Inmediata | Confirmar la exposición y restringir el acceso directo desde Internet mediante reglas de red y acceso privado. Probar primero la ruta autorizada para el personal remoto. | Administración de red y base de datos | Comprobación autorizada de que un origen no permitido no alcanza el servicio y un empleado autorizado sí puede trabajar. |
| Inmediata | Revisar registros disponibles del periodo de exposición y preservar evidencias. Activar respuesta a incidentes si aparecen indicios de acceso indebido. | Equipo de seguridad | Revisión documentada de accesos, exportaciones y anomalías; ausencia de registros no equivale a ausencia de compromiso. |
| Alta | Inventariar cuentas y permisos; retirar accesos innecesarios, separar funciones y restringir exportaciones según el puesto. | Responsable de datos y administrador | Matriz de autorización revisada y pruebas con cuentas de distintos roles. |
| Alta | Aplicar MFA en la vía de acceso remoto y en administración, integrar AAA y revisar credenciales o secretos expuestos. | Gestión de identidades y TI | Acceso individual trazable, pruebas de MFA y revocación de cuentas. |
| Alta | Revisar SSL/TLS existente, exigir TLS seguro y validar certificados; evaluar cifrado en reposo, claves y configuración del motor. | Administración de base de datos | Validación de conexiones cifradas, permisos sobre claves y revisión de configuración y versiones. |
| Alta | Alertar sobre exportaciones inusuales, fallos de autenticación y modificaciones masivas; restringir operaciones de escritura a los roles que las necesitan. | Seguridad y operaciones | Alertas probadas y verificación de que las cuentas de consulta no pueden modificar ni eliminar registros. |
| Alta | Implantar copias separadas del sistema y probar restauración; acordar prioridades y objetivos de recuperación con el negocio. | Operaciones y responsable de negocio | Restauración verificada y procedimiento de recuperación documentado. |

Los controles se complementan como defensa en profundidad. El cifrado no evita que una cuenta con permiso de lectura extraiga datos; la restricción de red, la autorización, los límites de exportación y la supervisión siguen siendo necesarios. No se asigna una puntuación residual reducida hasta verificar la implantación y eficacia de las medidas.

## Autoevaluación

| Criterio | Resultado | Evidencia |
|---|---|---|
| Propósito claro y valor de la evaluación para la empresa | Sí | Vincula el servidor con la actividad comercial y el coste de su interrupción. |
| Considera fuentes de amenaza | Sí | Actor externo económico, empleado malicioso y empleado que comete un error operativo. |
| Los eventos pueden ser iniciados por sus fuentes | Sí | Cada fila vincula capacidad, acceso y evento, explicitando las condiciones no verificadas. |
| Incluye probabilidad, gravedad y riesgo por fuente | Sí | Tres filas con puntuaciones 1–3 y cálculo del producto. |
| Explica el enfoque y propone remediación | Sí | Enfoque cualitativo y controles alineados con los riesgos, con verificaciones de cierre. |

Las secciones Propósito, Enfoque y Remediación tienen cuatro frases y entre 60 y 100 palabras cada una. Los cinco criterios están cubiertos y la descripción técnica y el alcance se han contrastado con la plantilla facilitada. Las puntuaciones siguen siendo estimaciones documentales, pendientes de una validación técnica en un caso real.

## Referencias y límites

- Instrucciones y escenario facilitados por el usuario.
- [Plantilla del curso: descripción técnica, alcance y apartados](https://docs.google.com/document/d/1GYQchjHbuWYhl1VLb6jBuCJRsXSDjc9msoOAQPxq_wQ/template/preview). Los textos orientativos de enfoque y remediación se han adaptado al escenario de trabajo remoto; el análisis de riesgos es de elaboración propia.
- [NIST SP 800-30 Rev. 1 — publicación oficial](https://csrc.nist.gov/pubs/sp/800/30/r1/final).
- [Guía completa: fuentes, eventos, probabilidad, impacto y riesgo](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf), apéndices D, E, G, H e I.

No se ha recibido el extracto adaptado del curso ni su modelo de solución. El análisis y las puntuaciones son propios de esta práctica y no representan una auditoría técnica de un sistema real.
