import pandas as pd

from carga import cargar_datos

_, ventas = cargar_datos()

print("\nventas.shape")
print(ventas.shape)

print("\nventas.info()")
ventas.info() # Devuelve None, por lo que no necesito utilizar print()

print("\nventas.describe()")
print(ventas.describe())