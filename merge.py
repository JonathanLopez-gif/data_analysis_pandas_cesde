from pathlib import Path

PROCESSED = Path(__file__).parent / "Data" / "processed"

# TODO 6: escribir las validaciones y devolver True o False.

def validar_premerge(clientes, ventas):
    """Revisa que el merge se pueda hacer. Devuelve True si todo está bien, False si no."""

    print("\nVALIDACIONES PRE-MERGE")
    
    # 1. Que exista la columna "id_cliente" en los dos dataframes.
    if "id_cliente" not in clientes.columns:
        print("ERROR: 'id_cliente' no está en clientes.")
        return False
    if "id_cliente" not in ventas.columns:
        print("ERROR: 'id_cliente' no está en ventas.")
        return False
    print("OK: 'id_cliente' existe en ambas tablas.")

    # 2. Que "id_cliente" no esté repetido en clientes.
    duplicados = clientes["id_cliente"].duplicated().sum()
    print(f"Duplicados en clientes: {duplicados}")
    if duplicados > 0:
        print("ERROR: existen clientes duplicados.")
        return False
    print("OK: no existen clientes duplicados.")
    
    # 3. Que "id_cliente" tenga el mismo tipo en los dos dataframes.
    tipo_clientes = clientes["id_cliente"].dtype
    tipo_ventas = ventas["id_cliente"].dtype
    print(f"Tipo en clientes: {tipo_clientes}, Tipo en ventas: {tipo_ventas}")
    if tipo_clientes != tipo_ventas:
        print("ERROR: los tipos de datos no coinciden.")
        return False
    print("OK: los tipos de datos coinciden.")

    # 4. Cuántas ventas no tienen cliente asociado (esto solo se informa, no falla).
    ventas_sin_cliente = ventas["id_cliente"].isin(clientes["id_cliente"]).sum()
    print(f"Ventas sin cliente asociado: {ventas_sin_cliente}")

    print("VALIDACIONES PRE-MERGE COMPLETADAS\n")
    
    return True

 # TODO 7: validar con validar_premerge(), hacer el merge, guardar el CSV y devolver el dataframe.

def unir(clientes, ventas):
    """Une ventas con clientes usando "id_cliente" y guarda el resultado en Data/processed/merge.csv."""

    # Validar antes de hacer el merge.
    if not validar_premerge(clientes, ventas):
        print("ERROR: No se puede hacer el merge debido a errores de validación.")
        return None

    """
    Usar pd.merge(...) o ventas.merge(...).
    Usar how="left" para no perder ventas.
    Usar validate="m:1" para confirmar que cada venta tiene un solo cliente.
    Guardar con df.to_csv(...) en PROCESSED / "merge.csv".
    """
    df = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")
    PROCESSED.mkdir(parents=True, exist_ok=True)  # Crear carpeta si no existe.
    df.to_csv(PROCESSED / "merge.csv", index=False) # No guardar el índice como una columna adicional.

    print("RESULTADO DEL MERGE")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Archivo guardado en: {PROCESSED / 'merge.csv'}")
    print("\nPrimeras filas:")
    print(df.head())

    return df
