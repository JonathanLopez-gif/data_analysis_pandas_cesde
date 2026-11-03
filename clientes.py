import pandas as pd

from carga import cargar_datos

clientes, _ = cargar_datos()

print("\nclientes.shape")
print(clientes.shape)

print("\nclientes.info()")
clientes.info() # Devuelve None, por lo que no necesito utilizar print()

print("\nclientes.describe()")
print(clientes.describe())