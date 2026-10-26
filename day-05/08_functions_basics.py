# Creating (defining) functions

def place_order(item):
    print(f"Item placed is: {item}")
    print("Order placed")


def getOrder():
    print("Preparing Order")
    return "Collect Your Order"


def calculate_total(item):
    base_price = 25.5
    totalprice = (base_price + len(item)) * 1.15
    return totalprice


myfood = input("What would you like: ")

place_order(myfood)

print("")

print(getOrder())

order_total = calculate_total(myfood)

print(f"Your order costs: R{order_total:.2f}")

print("")