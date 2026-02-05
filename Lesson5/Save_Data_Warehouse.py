

def save_data(balance, products, log):

    with open("Balance Database.txt", "w") as fd_balance:
        fd_balance.write(str(balance))

    with open("Products Database.txt", "w") as fd_products:
        fd_products.write("name,price,quantity\n")

        for name, info in products.items():
            line = f"{name},{info['price']},{info['quantity']}\n"
            fd_products.write(line)

    with open("Log Database.txt", "w") as fd_log:
        for entry in log:
            line = ",".join(map(str, entry)) + "\n"
            fd_log.write(line)