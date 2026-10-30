products = ["Rice", "Sugar", "Wheat"]

for product in products:
    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming stock: "))
    dispatched = int(input("Enter dispatched stock: "))

    closing = opening + incoming - dispatched

    print("Product:", product)
    print("Closing Stock =", closing)

    if closing < 0:
        print("Stock shortage detected")
    else:
        print("Stock is available")