#stock Portfolio tracker

#hardcoded stock prices
stock_prices = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOG" : 200,
    "MSFT" : 300,

}
total_investment = 0
print("====stock Portfolio Tracker====")

#number of stocks user wants to enter
n = int(input("How many stocks do you want to add?"))

#file to save results
file = open("portfolio.txt","w")

for i in range(n):
    stock_name = input("\Enter stock name :").upper()
    if stock_name in stock_prices:
        quantity = int(input("Enter stock name:"))
        investment = stock_prices[stock_name]*quantity
        total_investment += investment
        print(f"Investment for{stock_name}:${investment}")

        #save to file
        file.write(f"{stock_name}-Quantity:{quantity}-Investment:${investment}\n")

    else:
        print("Stock not available!")

#final total 
print("\nTotal Investment value:$",total_investment)

file.write(f"\nTotal Investment value:${total_investment}")

file.close()
print("\nPortfolio saved successfully in portfolio.txt")

