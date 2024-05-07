# You have been provided with stock market data, where each data point is a tuple containing a company's stock symbol, the date,
# and the closing price. Your task is to write a function to find the average closing price of a specified stock.


stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]
def average_stock(stock_data,stock_name):
    stock_count = 0
    stock_total = 0
    for stock in stock_data:
        if stock[0] == stock_name:
            stock_count += 1
            stock_total += stock[2]
    average_price = stock_total / stock_count
    print(average_price)
    return average_price

average_stock(stock_data, "AAPL")