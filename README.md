# Taller práctico: análisis de datos con Pandas

**Estudiante:** Jonathan López Vergara 
**Proyecto:** Análisis de ventas y clientes  
**Lenguaje:** Python  
**Librerías:** Pandas y Matplotlib

## 1. Descripción del proyecto

Este proyecto permite cargar, limpiar, unir, analizar y visualizar información de clientes y ventas mediante Pandas.

El programa funciona desde una aplicación de consola con un menú de opciones.

## 2. Estructura del proyecto

- `main.py`: menú principal.
- `carga.py`: carga los archivos CSV.
- `limpieza.py`: limpieza de datos.
- `merge.py`: validación y unión de los DataFrames.
- `analisis.py`: análisis y agrupaciones.
- `graficos.py`: generación de gráficos.
- `exploracion.py`: ejercicios de indexación y concatenación.
- `Data/raw/`: archivos originales.
- `Data/processed/`: resultados procesados y gráficos.

## 3. Resultados de la limpieza y unión

Se identificó un registro sin producto en el archivo de ventas. Se reemplazó el valor nulo por el texto `Sin especificar`, conservando la transacción y su información económica.

Posteriormente, se unieron los DataFrames de clientes y ventas utilizando la columna `id_cliente` y un `left join`.

El resultado esperado del merge es de 68 filas y 14 columnas.

## 4. Análisis de negocio

### Pregunta 1. ¿Qué categoría genera más ingresos?

**Resultado del análisis:**

```text
categoria
Tecnologia    14290000
Hogar          3653000
Papeleria       749000
Accesorios      484000
```

**Respuesta:** Tecnología es la categoría que genera más ingresos, con $14.290.000.

**Criterio utilizado:** Se agruparon las ventas por categoría utilizando `groupby()`, se sumó la columna `total` y se ordenaron los resultados de mayor a menor.

### Pregunta 2. ¿Qué canal vende más?

**Resultado del análisis:**

```text
         ventas  ingresos
Online       35  14669000
Tienda       33   4507000
```

**Respuesta:** El canal Online genera mayores ingresos, con $14.669.000 y 35 transacciones.

**Criterio utilizado:** Se agruparon las ventas por canal y se calcularon dos indicadores: cantidad de transacciones e ingresos totales. La comparación principal se realizó por ingresos.

### Pregunta 3. ¿Los clientes VIP compran más que los Regulares?

**Resultado del análisis:**

| Segmento | Clientes | Compras | Gasto total | Compras por cliente | Gasto por cliente |
|---|---:|---:|---:|---:|---:|
| Regular | 36 | 39 | $11.110.000 | 1,08 | $308.611,11 |
| VIP | 24 | 29 | $8.066.000 | 1,21 | $336.083,33 |

**Respuesta:** Sí. Los clientes VIP realizan más compras y gastan más dinero en promedio por cliente que los clientes Regulares.

**Criterio utilizado:** Se compararon los promedios de compras y gasto por cliente, utilizando `nunique()` para contar los clientes diferentes. Esto evita comparar directamente segmentos con cantidades distintas de clientes.

### Pregunta 4. ¿Qué método de pago es el más usado?

**Resultado del análisis:**

```text
metodo_pago
Efectivo         30
Tarjeta          25
Transferencia    13
```

**Respuesta:** Efectivo es el método de pago más utilizado, con 30 transacciones.

**Criterio utilizado:** Se utilizó `value_counts()` para contar la frecuencia de cada método de pago.

### Pregunta 5. ¿Cuáles son los cinco clientes con más compras?

**Resultado del análisis:**

| ID cliente | Nombre | Compras | Gasto total |
|---:|---|---:|---:|
| 21 | Nicolas Cardona | 2 | $2.515.000 |
| 35 | Matias Rodriguez | 2 | $1.278.000 |
| 52 | Mia Quintero | 2 | $1.090.000 |
| 58 | Luna Montoya | 2 | $1.007.000 |
| 3 | Luis Perez | 2 | $730.000 |

**Respuesta:** Los cinco clientes anteriores lideran el ranking, todos con dos compras.

**Criterio utilizado:** Se agruparon las ventas por identificador y nombre del cliente, se contaron las compras y se sumó el gasto total. Se ordenó primero por cantidad de compras y luego por gasto total como criterio de desempate.

## 5. Gráficos generados

El proyecto genera dos gráficos de barras:

1. `ventas_por_categoria.png`: representa los ingresos por categoría.
2. `ventas_por_canal.png`: representa los ingresos por canal de venta.

Ambos archivos se almacenan en `Data/processed/graficos/`.

## 6. Conceptos de Pandas utilizados

Durante el desarrollo se utilizaron los siguientes conceptos:

- `read_csv()`: lectura de archivos CSV.
- `shape`, `info()` y `describe()`: exploración de datos.
- `loc` e `iloc`: selección de filas y columnas.
- `fillna()`: tratamiento de valores nulos.
- `drop_duplicates()`: eliminación de duplicados.
- `pd.to_datetime()`: conversión de fechas.
- `pd.concat()`: concatenación de DataFrames.
- `merge()`: unión de tablas.
- `groupby()` y `agg()`: agrupación y agregación.
- `value_counts()` y `nunique()`: conteo de valores.
- Matplotlib: visualización de resultados.

## 7. Ejecución del proyecto

Instalar las dependencias:

```bash
pip install pandas matplotlib
```

Ejecutar el programa:

```bash
python main.py
```

Seguir las opciones del menú en orden:

1. Cargar datos.
2. Limpiar datos.
3. Validar y unir.
4. Analizar resultados.
5. Generar gráficos.

## 8. Conclusión

El desarrollo permitió aplicar herramientas de Pandas para transformar datos originales en información útil para la toma de decisiones. Se identificaron las categorías y canales con mayores ingresos, se comparó el comportamiento de los segmentos de clientes y se identificaron los métodos de pago y clientes más relevantes.

También se aplicaron técnicas de limpieza, validación, unión, agrupación y visualización de datos.
