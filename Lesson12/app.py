from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

stock = {"Bananas": 50,
        "Apples": 100,
        "Pears": 100,
        "Oranges": 150,
        "Watermelons": 25
}
balance = 100.0

def save_history(line):
    with open("history.txt", "a") as f:
        f.write(line + "\n")

@app.route('/')
def index():
    return render_template("index.html", stock=stock, balance=balance)

@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    global balance

    if request.method == "POST":
        try:
            product = request.form["product_name"].capitalize()
            price = float(request.form["unit_price"])
            quantity = int(request.form["number_pieces"])

            if price <= 0 or quantity <= 0:
                raise ValueError("Invalid values")

            total_cost = price * quantity

            stock[product] = stock.get(product, 0) + quantity

            balance -= total_cost

            save_history(f"Purchase,{product},{quantity},-{total_cost}")

            return redirect(url_for("index"))

        except Exception:
            return "Error: Invalid input data"

    return render_template("purchase.html")

@app.route("/sale", methods=["GET", "POST"])
def sale():
    global balance

    if request.method == "POST":
        try:
            product = request.form["product_name"].capitalize()
            price = float(request.form["unit_price"])
            quantity = int(request.form["number_pieces"])

            if product not in stock or stock[product] < quantity:
                return f"Error: There are not enough {product}"

            total_income = price * quantity

            stock[product] -= quantity
            balance += total_income

            save_history(f"Sale,{product},{quantity},{total_income}")

            return redirect(url_for("index"))

        except Exception:
            return "Error: Invalid input data"

    return render_template("sale.html")

@app.route("/balance", methods=["GET", "POST"])
def change_balance():
    global balance

    if request.method == "POST":
        try:
            operation = request.form["operation"]
            amount = float(request.form["amount"])

            if amount <= 0:
                raise ValueError("Invalid amount")

            if operation == "add":
                balance += amount
                save_history(f"Balance Add,,,{amount}")
            elif operation == "subtract":
                balance -= amount
                save_history(f"Balance Subtract,,,-{amount}")
            else:
                return "Error: Invalid operation"

            return redirect(url_for("index"))

        except Exception:
            return "Error: Invalid input data"

    return render_template("balance.html")

@app.route("/history/")
def history():
    try:
        with open("history.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    lines = [line.strip() for line in lines]

    line_from = request.args.get("from", type=int)
    line_to = request.args.get("to", type=int)

    if line_from is not None and line_to is not None:
        lines = lines[line_from-1:line_to]

    history_data = [line.split(",") for line in lines]

    return render_template("history.html", history_data=history_data)

if __name__ == "__main__":
    app.run()