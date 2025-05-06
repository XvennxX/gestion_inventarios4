def actualizar_producto(inventario, producto, nueva_cantidad):
    if producto in inventario:
        inventario[producto] = nueva_cantidad
        print(f"✅ Producto '{producto}' actualizado a {nueva_cantidad} unidades.")
    else:
        print(f"⚠️ El producto '{producto}' no existe en el inventario.")