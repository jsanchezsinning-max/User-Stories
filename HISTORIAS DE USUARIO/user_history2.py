inventory = []

# This function displays the menu

def menu():
    option = ""

    while option != "1" and option != "2" and option != "3" and option != "4":

        print("MENU")
        print("""
            1. Add product
            2. View Inventory
            3. Calculate statistics
            4. Exit
                """)
        option = input("Choose an Option: ")
        if option != "1" and option != "2" and option != "3" and option != "4":
            print("Invalid option, try again.\n")

    return option

# This function ensures that the user can only enter text when I ask for the product name

def validate_name():
    name = input("Enter product name: ")
    while not name.replace(" ", "").isalpha():
        print("Error: Only letters allowed.")
        name = input("Enter product name: ")
    return name

# This function ensures that the user can only enter int when I ask for the product price and quantity

def validate_num(message):
    value = input(message)
    while not value.isdigit() or int(value) <= 0:
        print("Error: Enter a positive number.")
        value = input(message)
    return int(value)

# THIS FUNCTION IS TO ADD A NEW PRODUCT 

def add_product(inventory):
    print("\n========== ADD NEW PRODUCT ==========")

    name = validate_name()
    price = validate_num("Enter Price: $")
    quantity = validate_num("Enter Quantity: ")

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)
    print("Product added successfully!\n")

# THIS FUNCTION IS TO VIEW THE INVENTORY

def view_inventory(inventory):
    print("\n========== INVENTORY ==========")

    if len(inventory) == 0:
        print("Inventory in empty.\n")
    else:
        for product in inventory:
            print("Product:", product["name"],
                  "| Price:", product["price"],
                  "| Quantity:", product["quantity"])
        print()

# THIS FUNCTION IS TO CALCULATE THE STATISTICS

def calculate_statistics(inventory):
    print("\n========== STATISTICS ==========")

    if len(inventory) == 0:
        print("No products to calculate.\n")
    else:
        final_price = 0

        for product in inventory:
            final_price += product["price"] * product["quantity"]

        total_products = len(inventory)

        print("Total inventory value: $",final_price)
        print("Total products registered: ",total_products)

# MAIN PROGRAM

running = True

while running:
    option = menu()

    if option == "1":
        add_product(inventory)

    elif option == "2":
        view_inventory(inventory)
    
    elif option == "3":
        calculate_statistics(inventory)

    elif option == "4":
        print("See you soon!!!")
        running = False

# ----------- REVIEW -----------

# Este programa permite gestionar un inventario básico.
# El usuario puede agregar productos, ver el inventario y calcular estadísticas.
# Se utilizan listas para almacenar datos y diccionarios para representar cada producto.
# También se aplican estructuras de control como condicionales y bucles.
