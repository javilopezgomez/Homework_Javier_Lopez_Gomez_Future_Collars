#Homework - Simple Accounting System / Warehouse

balance = 100.0
products = {"bananas": {"price": 1.50, "quantity": 50},
            "apples": {"price": 1.20, "quantity": 100},
            "pears": {"price": 1, "quantity": 100},
            "oranges": {"price": 0.70, "quantity": 150},
            "watermelons": {"price": 2.50, "quantity": 25}
}
log = []

while True:
    print("What would you like to do? Choose from the following list: \n")
    print("Balance \n"
          "Sale \n"
          "Purchase \n"
          "Account \n"
          "List \n"
          "Warehouse \n"
          "Review \n"
          "End \n")

    command = input("Command: ").lower()

    if command == "balance":
        print(f"Current balance: {balance}")
        while True:
            try:
                amount = float(input("Add an amount: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        balance += amount
        log.append(("balance", amount))
        print(f"Balance updated. Current balance: {balance}")

    elif command == "sale":
        while True:
            product_sold = str(input("Product sold: ")).lower()
            if product_sold in products:
                break
            else:
                print("Product was not found. Enter a correct product.")

        while True:
            price_sold = float(input(f"Price of the product sold "
                                     f"(recommended price for this product is {products[product_sold]["price"]}): "))
            if price_sold > 0:
                break
            else:
                print("Invalid amount. Please, enter a correct price.")

        while True:
            quantity_sold = int(input("Quantity of product sold: "))
            if quantity_sold <= 0:
                print("Invalid amount. Please enter a correct number.")
                continue
            if quantity_sold > products[product_sold]["quantity"]:
                print(f"There are not enough {product_sold}. Enter a correct quantity.")
                continue
            break

        earning = price_sold * quantity_sold
        balance += earning
        products[product_sold]["quantity"] -= quantity_sold
        log.append(("sale", product_sold, earning))
        print(f"Sale recorded. Current balance: {balance} \n")

    elif command == "purchase":
        while True:
            product_purchased = str(input("Name of the product purchased: ")).lower()
            if product_purchased in products:
                break
            else:
                print("Product was not found. Enter a correct product.")

        while True:
            price_purchased = float(input(f"Price of the product sold "
                                     f"(recommended price for this product is {products[product_purchased]["price"]}): "))
            if price_purchased > 0:
                break
            else:
                print("Invalid amount. Please, enter a correct price.")

        while True:
            quantity_purchased = int(input("Quantity purchased: "))
            if quantity_purchased <= 0:
                print("Invalid amount. Please enter a correct number.")
                continue
            else:
                break

        expense = price_purchased * quantity_purchased
        balance -= expense
        products[product_purchased]["quantity"] += quantity_purchased
        log.append(("purchase", product_purchased, expense))
        print(f"Purchase recorded. Current balance: {balance} \n")

    elif command == "account":
        print(f"This is the current account balance: {balance}")

    elif command == "list":
        print("This is the current inventory: \n")
        for fruit, information in products.items():
            print(f"{fruit} -> Price: {information["price"]}, Quantity: {information["quantity"]}")
        print("\n")

    elif command == "warehouse":
        while True:
            search_warehouse = str(input("Which product do you want to search?: ")).lower()
            if search_warehouse in products:
                info = products[search_warehouse]
                print(f"Price: {info["price"]}, Quantity: {info["quantity"]} \n")
                break
            else:
                print("Product not found.")

    elif command == "review":
        while True:
            if len(log) == 0:
                print("There have not been operations recorded yet.")
                break

            review_from = input("From: ")
            review_to = input("To: ")
            if review_from == "" and review_to == "":
                for all_log in log:
                    print(all_log)
                break

            elif review_from != "" and review_to != "":
                review_from = int(review_from)
                review_to = int(review_to)
                if 0 <= review_from < len(log) and 0 <= review_to < len(log):
                    for i in range(review_from, review_to + 1):
                        print(log[i])
                break

            else:
                print("Invalid indexes. Please enter a correct index.")

    elif command == "end":
        print("The session has ended.")
        break

    else:
        print("The command is not recognized. Please, try again.")