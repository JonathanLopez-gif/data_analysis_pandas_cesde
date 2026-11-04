# Taller práctico: análisis de datos con Pandas

## 7. Análisis y agrupaciones

### 1. ¿Qué categoría genera más ingresos?
Tecnología genera los mayores ingresos, con $14.290.000. El criterio utilizado fue la suma de la columna `total`, agrupada por `categoria`.

### 2. ¿Qué canal vende más?
Online es el canal con mayores ingresos, con $14.669.000 y 35 transacciones. El criterio principal utilizado fue el valor total de los ingresos por canal.

### 3. ¿Los clientes VIP compran más que los Regulares?
Sí. Los clientes VIP realizan aproximadamente 1,21 compras por cliente y gastan en promedio $336.083,33. Los clientes Regular realizan aproximadamente 1,08 compras por cliente y gastan $308.611,11. Se compararon los promedios por cliente para evitar distorsiones por la diferencia en el tamaño de los segmentos.

### 4. ¿Qué método de pago es el más usado?
Efectivo es el método más utilizado, con 30 transacciones. El criterio utilizado fue contar las apariciones de cada método mediante `value_counts()`.

### 5. ¿Cuáles son los cinco clientes con más compras?
Los cinco primeros son Nicolas Cardona, Matias Rodriguez, Mia Quintero, Luna Montoya y Luis Perez. Todos tienen dos compras. Se utilizó el gasto total como criterio de desempate.