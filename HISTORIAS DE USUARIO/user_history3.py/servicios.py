# servicios.py

# ----------- AGREGAR PRODUCTO -----------
def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto al inventario"""
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)


# ----------- MOSTRAR INVENTARIO -----------
def mostrar_inventario(inventario):
    """Muestra todos los productos"""
    if not inventario:
        print("Inventory is empty.")
    else:
        for p in inventario:
            print(f"Product: {p['nombre']} | Price: {p['precio']} | Quantity: {p['cantidad']}")


# ----------- BUSCAR PRODUCTO -----------
def buscar_producto(inventario, nombre):
    """Busca un producto por nombre"""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


# ----------- ACTUALIZAR PRODUCTO -----------
def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio o cantidad"""
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False


# ----------- ELIMINAR PRODUCTO -----------
def eliminar_producto(inventario, nombre):
    """Elimina un producto"""
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False


# ----------- ESTADÍSTICAS -----------
def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario"""
    if not inventario:
        return None

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }