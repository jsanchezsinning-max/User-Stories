print("INVENTORY")

def enter_product():
    name = input("\nEnter the product´s name: ")
    while not name.replace(" ", "").isalpha(): #replace Sirve para reemplazar una parte de un texto por otra
        print("Error: Only letters are allowed (no numbers or special characters).")
        name = input("\nEnter the product´s name: ")
    return name

def enter_quantity():
    quantity = input("Enter the quantity of the product: ")
    while not quantity.isdigit() or int(quantity) <= 0:
        print("Error: Enter a positive number (no text or negatives).")
        quantity = input("Enter the quantity of the product: ")
    return int(quantity)

def enter_price():
    price = input("Enter the product price: $")
    while not price.isdigit() or int(price) <= 0:
        print("Error: Enter a valid positive price.")
        price = input("Enter the product price: $")
    return int(price)

name = enter_product()
quantity = enter_quantity()
price = enter_price()

final_price = price * quantity

print("\nThe product was successfully added\n")
print("Product name:", name)
print("Product price: $", price)
print("Product quantity:", quantity)
print("Final product value: $", final_price)

