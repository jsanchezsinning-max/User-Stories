# archivos.py

def guardar_csv(inventario, ruta, incluir_header=True):
    """Guarda el inventario en CSV"""
    if not inventario:
        print("Inventory is empty, nothing to save.")
        return

    try:
        with open(ruta, "w", encoding="utf-8") as file:
            if incluir_header:
                file.write("nombre,precio,cantidad\n")

            for p in inventario:
                file.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

        print(f"Inventory saved in: {ruta}")

    except Exception as e:
        print("Error saving file:", e)


def cargar_csv(ruta):
    """Carga inventario desde CSV"""
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as file:
            lineas = file.readlines()

        if not lineas:
            print("Empty file.")
            return [], 0

        header = lineas[0].strip()
        if header != "nombre,precio,cantidad":
            print("Invalid header.")
            return [], 0

        for linea in lineas[1:]:
            try:
                nombre, precio, cantidad = linea.strip().split(",")

                precio = float(precio)
                cantidad = int(cantidad)

                if precio < 0 or cantidad < 0:
                    raise ValueError

                inventario.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })

            except:
                errores += 1

        return inventario, errores

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error loading file:", e)

    return [], 0