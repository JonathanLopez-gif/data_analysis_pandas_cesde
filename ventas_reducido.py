import pandas as pd

ventas_reducido = pd.read_csv("Data/raw/ventas.csv", usecols=["producto", "total"])

print(ventas_reducido)