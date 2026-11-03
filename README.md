# Taller práctico: análisis de datos con Pandas

4.3 Con ventas.info() se observa que la columna "producto" tiene 67 non-null, dando a saber que hay una fila sin producto (V004).

4.6 Con .iloc[2,6] se obtiene el total de la venta V003 porque, como la primera columna se convierte en el índice de la fila, la columna siguiente queda en posición 0. Por ende, la posición 6 es la columna "total". 

5.5 Con ventas.isnull().sum() encontré que hay un producto nulo, o vacío. Con ventas["producto"].fillna("Sin especificar") reemplacé el campo nulo por ese string.

6 El resultado del merge contiene 14 columnas porque ventas tiene 10 columnas y clientes tiene 5. Al unir ambas tablas mediante id_cliente, esta columna compartida aparece una sola vez. Por eso el resultado es 10 + 5 - 1 = 14 columnas.


