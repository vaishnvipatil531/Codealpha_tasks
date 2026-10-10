stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:

    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be positive.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print("Stock Price:", price)
    print("Investment:", investment)

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment =", total_investment)

with open("portfolio_report.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("======================\n")
    file.write("Total Investment = " + str(total_investment))

print("Report saved as portfolio_report.txt")