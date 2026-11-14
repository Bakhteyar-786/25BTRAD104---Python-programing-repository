# SALES DATA ANALYZER
# Each product is a dictionary stored inside a list:
# {"name": "Pen", "price": 10.0, "quantity": 50}      Revenue = price * quantity

products = []

while True:
    print("\n--- SALES DATA ANALYZER ---")
    print("1. Add product sales")
    print("2. Update a product (replace price and quantity)")
    print("3. Show sales summary")
    print("4. Load sample data (for testing)")
    print("0. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter product name: ").strip()
        price = float(input("Enter price per unit: "))
        quantity = int(input("Enter quantity sold: "))
        if name == "" or price < 0 or quantity < 0:
            print("Invalid input.")
        else:
            found = False
            for p in products:
                if p["name"].lower() == name.lower():
                    found = True
                    p["quantity"] = p["quantity"] + quantity
                    p["price"] = price
                    print(p["name"], "already existed: quantity added, price updated.")
            if not found:
                products.append({"name": name, "price": price, "quantity": quantity})
                print(name, "added.")

    elif choice == "2":
        name = input("Enter product name: ").strip()
        price = float(input("Enter new price per unit: "))
        quantity = int(input("Enter new quantity sold: "))
        found = False
        for p in products:
            if p["name"].lower() == name.lower():
                found = True
                if price < 0 or quantity < 0:
                    print("Invalid input.")
                else:
                    p["price"] = price
                    p["quantity"] = quantity
                    print("Product updated.")
        if not found:
            print("Product not found.")

    elif choice == "3":
        if len(products) == 0:
            print("No product data yet.")
        else:
            # list comprehensions
            revenues = [p["price"] * p["quantity"] for p in products]
            quantities = [p["quantity"] for p in products]
            total_sales = sum(revenues)

            print("\nProduct | Price | Quantity | Revenue | Share of total")
            print("-" * 55)
            for i in range(len(products)):
                if total_sales > 0:
                    share = revenues[i] / total_sales * 100
                else:
                    share = 0.0
                print(products[i]["name"], "|", products[i]["price"], "|",
                      products[i]["quantity"], "|", round(revenues[i], 2), "|",
                      round(share, 1), "%")
            print("-" * 55)
            print("Total sales:", round(total_sales, 2))

            top_quantity = max(quantities)
            print("\nHighest-selling product(s) (by quantity):")
            for p in products:
                if p["quantity"] == top_quantity:
                    print(" ", p["name"], "-", top_quantity, "units")

            top_revenue = max(revenues)
            low_revenue = min(revenues)
            print("Highest revenue product(s):")
            for i in range(len(products)):
                if revenues[i] == top_revenue:
                    print(" ", products[i]["name"], "-", round(revenues[i], 2))
            print("Lowest revenue product(s):")
            for i in range(len(products)):
                if revenues[i] == low_revenue:
                    print(" ", products[i]["name"], "-", round(revenues[i], 2))

    elif choice == "4":
        products = [
            {"name": "Pen",      "price": 10.0, "quantity": 50},   # revenue 500
            {"name": "Notebook", "price": 45.0, "quantity": 20},   # revenue 900
            {"name": "Eraser",   "price": 5.0,  "quantity": 80},   # revenue 400
            {"name": "Pencil",   "price": 4.0,  "quantity": 80}    # revenue 320
        ]
        print("Sample data loaded.")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
