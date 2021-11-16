from datetime import date

"""
11/16/21

Class to store arbitrary stock.
"""


class Stock:
    def __init__(self, symbol: str, price: float, shares: int, date_purchased: date = date.today(),
                 description: str = None):
        self.symbol = symbol.upper()
        self.price = price
        self.shares = shares
        self.date_purchased = date_purchased
        self.market_value = price * shares

        if description:
            self.description = description

    def update_price(self, new_price):
        self.price = new_price

    def update_shares(self, new_shares_amount):
        self.shares = new_shares_amount

    def __str__(self):
        return f"{self.symbol} | ${self.price}, {self.shares} shares, purchased on {self.date_purchased}."


if __name__ == "__main__":
    test_stock = Stock("aapl", 153.12, 10)
    print(test_stock)
