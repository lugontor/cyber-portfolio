# Aplicar filtros a consultas SQL

## Descripción del proyecto

En este escenario educativo, el equipo de seguridad necesita investigar intentos de inicio de sesión y seleccionar equipos de empleados para aplicar actualizaciones. El objetivo es consultar las tablas `log_in_attempts` y `employees` utilizando filtros de fecha, hora, patrones y condiciones lógicas. Las seis consultas siguientes permiten delimitar los registros que requieren revisión sin modificar los datos originales.

## Alcance y estado

Se incluyen versiones mecanografiadas de las consultas, permitidas por las instrucciones del curso. No se han recibido la base de datos, sus resultados ni el documento «Formatos de tablas»: las salidas descritas son **resultados esperados**, no resultados de ejecución.

Para `log_in_attempts` se utilizan las columnas indicadas por el escenario: `login_time`, `success`, `login_date` y `country`. Para `employees` se propone la variante en inglés `department`, `office`, `East-`, `Finance`, `Sales` e `IT`; debe confirmarse en el laboratorio, porque el texto recibido traduce esos identificadores y valores al español. Si la tabla realmente utiliza `departamento`, `oficina`, `Este-`, `Finanzas`, `Ventas` y `Tecnología de la información`, se deben usar los nombres y valores exactos correspondientes.

Las consultas suponen columnas de fecha y hora con tipos adecuados o formatos normalizados `YYYY-MM-DD` y `HH:MM:SS`. No se atribuyen cantidades de filas, identidades ni hallazgos de seguridad sin disponer de los datos.

## 1. Intentos fallidos después de las 18:00

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00:00'
  AND success = 0;
```

`SELECT *` recupera todas las columnas de los registros seleccionados. `WHERE` restringe el resultado a los intentos cuya hora sea posterior a las 18:00 y cuyo valor de éxito sea 0, que el escenario define como fallo. El operador `AND` exige que se cumplan ambas condiciones.

**Resultado esperado:** únicamente intentos fallidos posteriores a las 18:00:00, sin incluir los ocurridos exactamente a esa hora. Los intentos exitosos quedan excluidos aunque sucedan fuera del horario laboral. Estos registros son candidatos a investigación, no una prueba suficiente de ataque.

## 2. Intentos de inicio de sesión en fechas concretas

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09'
   OR login_date = '2022-05-08';
```

El operador `OR` permite seleccionar registros que cumplan cualquiera de las dos condiciones. Se utiliza el formato de fecha año-mes-día para representar las fechas solicitadas.

**Resultado esperado:** todos los intentos del 8 y del 9 de mayo de 2022, tanto exitosos como fallidos y a cualquier hora. Los registros de otros días quedan fuera del resultado.

## 3. Intentos de inicio de sesión fuera de México

```sql
SELECT *
FROM log_in_attempts
WHERE NOT (country LIKE 'MEX%');
```

`LIKE` busca un patrón y `%` representa cero o más caracteres. Así, `MEX%` coincide tanto con `MEX` como con `MEXICO`, las dos formas mencionadas por la actividad. `NOT` invierte la condición para excluir las coincidencias.

**Resultado esperado:** los intentos cuyo país registrado no comience por `MEX`, según las reglas de comparación del motor. El patrón también excluiría cualquier otro valor con ese prefijo, por lo que se ajusta aquí a las etiquetas descritas en el ejercicio.

Un valor `NULL` en `country` no se incluye: en SQL la condición queda desconocida y no pasa el filtro. Si existen países sin identificar, deben revisarse por separado mediante `WHERE country IS NULL`; no se puede afirmar que se encuentren fuera de México. El campo de país tampoco demuestra por sí solo la ubicación física del atacante.

## 4. Empleados de Marketing en el edificio Este

Variante propuesta para el esquema en inglés:

```sql
SELECT *
FROM employees
WHERE department = 'Marketing'
  AND office LIKE 'East-%';
```

`AND` combina el departamento con la ubicación. El patrón `East-%` selecciona oficinas cuyo nombre empieza por `East-`, como `East-170` y `East-320`.

**Resultado esperado:** únicamente los empleados de Marketing cuyas oficinas pertenecen al edificio Este, según la convención de nombres de la tabla. Se excluyen otros departamentos y las oficinas de otros edificios.

Si el esquema y los valores están en español, la consulta correspondiente sería:

```sql
SELECT *
FROM employees
WHERE departamento = 'Marketing'
  AND oficina LIKE 'Este-%';
```

Se debe elegir una de las variantes después de comprobar el esquema; no se presupone que ambas funcionen en la misma base de datos.

## 5. Empleados de Finanzas o Ventas

```sql
SELECT *
FROM employees
WHERE department = 'Finance'
   OR department = 'Sales';
```

`OR` incluye a empleados que pertenezcan a cualquiera de los dos departamentos. No se usa `AND`, porque en una fila con un único departamento no puede ser simultáneamente `Finance` y `Sales`.

**Resultado esperado:** empleados de Finanzas o Ventas, sin restricción de edificio, para identificar los registros asociados a la actualización de seguridad. Si el esquema está traducido, se sustituye `department` por `departamento` y los valores por `Finanzas` y `Ventas`.

## 6. Empleados que no pertenecen a TI

```sql
SELECT *
FROM employees
WHERE NOT (department = 'IT');
```

La condición interior selecciona el departamento de TI y `NOT` la niega. Se excluye a sus empleados porque, según el escenario, ya han recibido la actualización.

**Resultado esperado:** empleados cuyo departamento conocido sea distinto de `IT`. En el esquema traducido, la condición sería `NOT (departamento = 'Tecnología de la información')`, si ese es el valor exacto almacenado.

Si el departamento es `NULL`, la fila queda fuera del resultado y debe investigarse por separado. Seleccionar empleados no confirma que sus equipos se hayan actualizado: la consulta prepara el conjunto a revisar, pero no realiza la actualización.

## Revisión de operadores y comprobaciones

| Elemento | Uso en este proyecto |
|---|---|
| `LIKE` y `%` | Buscar prefijos en países y oficinas. |
| `>` en horas | Seleccionar intentos estrictamente posteriores a las 18:00. |
| `=` en fechas | Recuperar los dos días solicitados. |
| `AND` | Exigir simultáneamente fallo y hora, o departamento y edificio. |
| `OR` | Aceptar cualquiera de dos fechas o departamentos. |
| `NOT` | Excluir países coincidentes con un patrón o un departamento concreto. |

Antes de ejecutar, se deben confirmar los nombres de columnas, los tipos y los valores exactos del laboratorio. Después se deben registrar los resultados, comprobar casos de frontera como las 18:00:00 y revisar los valores nulos. Si se combinan `AND` y `OR` en una consulta futura, conviene usar paréntesis para expresar con claridad la agrupación deseada.

## Autoevaluación del documento

| Criterio | Estado |
|---|---|
| Incluye capturas o versiones mecanografiadas del código | Sí: consultas escritas. |
| Incluye una descripción del proyecto al principio | Sí: tres frases. |
| Explica las consultas y sus resultados | Sí: resultados esperados; ejecución con datos del curso pendiente. |
| Incluye un resumen al final | Sí: tres frases. |
| Explica el uso de LIKE | Sí: patrones de países y oficinas. |
| Explica el filtrado por fechas y horas | Sí: consultas 1 y 2. |
| Explica AND y OR para varias condiciones | Sí: consultas 1, 2, 4 y 5. |
| Explica NOT en los filtros | Sí: consultas 3 y 6, con el tratamiento de NULL. |

El contenido cubre los ocho criterios de documentación. La verificación del esquema, de las salidas reales y la comparación con el ejemplo del curso quedan pendientes de recibir esos materiales.

## Resumen

Las seis consultas muestran cómo utilizar filtros SQL para investigar accesos y seleccionar empleados en función de las necesidades de seguridad. Se combinan fechas, horas, patrones y operadores lógicos para delimitar los registros relevantes y se explican los casos que quedan excluidos. La comprobación con la base de datos del laboratorio permitirá validar el esquema y documentar las salidas reales antes de presentar la ejecución como verificada.
