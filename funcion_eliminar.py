def eliminar_producto(inventario, producto):
    if producto in inventario:
        del inventario[producto]
        print(f"Eliminando '{producto}' del inventario...")
    else:
        print(f"Error: el producto '{producto}' no existe en el inventario.")