

def load_data():
    try:
        with open('Balance Database.txt', 'r') as fd_balance:
            balance = float(fd_balance.read())

        products = {}
        with open('Products Database.txt', 'r') as fd_products:
            fd_products_lines = fd_products.readlines()

        for line in fd_products_lines[1:]:
            line = line.strip()

            if line == "":
                continue

            name, price, quantity = line.split(',')

            products[name] = {
                'price': float(price),
                'quantity': int(quantity)
            }

        log = []
        with open('Log Database.txt', 'r') as fd_log:
            fd_log_lines = fd_log.readlines()

        for line in fd_log_lines:
            line = line.strip()

            if line == "":
                continue
            activity = line.split(',')
            log.append(tuple(activity))

        return balance, products, log

    except (FileNotFoundError, ValueError, OSError):
        print("Data could not be found.")
        return 100.0, {}, []