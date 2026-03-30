from servicios import *
from archivos import *

inventario = []

def menu():
    print("""
1. Add product
2. Show inventory
3. Search product
4. Update product
5. Delete product
6. Statistics
7. Save CSV
8. Load CSV
9. Exit
""")
    return input("Choose option: ")


# Variable de control
running = True

while running:
    opcion = menu()

    if opcion == "1":
        nombre = input("Name: ")
        precio = float(input("Price: "))
        cantidad = int(input("Quantity: "))
        agregar_producto(inventario, nombre, precio, cantidad)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Search name: ")
        producto = buscar_producto(inventario, nombre)
        if producto:
            print(producto)
        else:
            print("Not found")

    elif opcion == "4":
        nombre = input("Product to update: ")
        precio = float(input("New price: "))
        cantidad = int(input("New quantity: "))
        if actualizar_producto(inventario, nombre, precio, cantidad):
            print("Updated")
        else:
            print("Not found")

    elif opcion == "5":
        nombre = input("Product to delete: ")
        if eliminar_producto(inventario, nombre):
            print("Deleted")
        else:
            print("Not found")

    elif opcion == "6":
        stats = calcular_estadisticas(inventario)
        if stats:
            print("Total units:", stats["unidades_totales"])
            print("Total value:", stats["valor_total"])
            print("Most expensive:", stats["producto_mas_caro"])
            print("Most stock:", stats["producto_mayor_stock"])
        else:
            print("No data")

    elif opcion == "7":
        ruta = input("File path: ")
        guardar_csv(inventario, ruta)

    elif opcion == "8":
        ruta = input("File path: ")
        nuevos, errores = cargar_csv(ruta)

        if nuevos:
            decision = input("Overwrite inventory? (S/N): ").upper()

            if decision == "S":
                inventario = nuevos
                print("Inventory replaced.")
            else:
                inventario.extend(nuevos)
                print("Inventory merged.")

        print(f"Loaded: {len(nuevos)} | Errors: {errores}")

    elif opcion == "9":
        print("Goodbye")
        running = False

    else:
        print("Invalid option")