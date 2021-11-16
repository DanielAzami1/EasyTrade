import Stock
from datetime import date, datetime

"""
11/16/21

Class to store constructed portfolios.
"""


class Portfolio:
    def __init__(self, name: str, constituents: list[Stock], nav: float, date_created: date = date.today(),
                 last_updated=datetime.today()):
        self.name = name
        self.constituents = constituents
        self.num_stocks = len(constituents)
        self.nav = nav
        self.date_created = date_created
        self.last_updated = last_updated

        self.transactions = Transactions(self)

    def print_constituents(self):
        print(f"Constituents of portfolio {self.name}:\n")
        for stock in self.constituents:
            print(" " + stock)
        print(f"\n{self.num_stocks} stocks in portfolio.")

    def buy_stock(self, new_stock: Stock):
        print(f"Executing buy order for {str(new_stock)}.")
        self.constituents.append(new_stock)
        self.num_stocks += 1
        self.nav += new_stock.market_value
        self.last_updated = datetime.today()

        self.transactions.session_transactions.append(Order("BUY", new_stock))

        print(f"Portfolio {self.name} updated.")

    def sell_stock(self, stock: Stock):
        print(f"Executing sell order for {str(stock)}.")
        self.constituents.remove(stock)
        self.num_stocks -= 1
        self.nav -= stock.market_value
        self.last_updated = datetime.today()

        self.transactions.session_transactions.append(Order("SELL", stock))

        print(f"Portfolio {self.name} updated.")

    def update_nav(self):
        pass


class Order:
    def __init__(self, direction: str, stock: Stock, timestamp: datetime = datetime.today()):
        if direction not in ["BUY", "SELL"]:
            raise ValueError("Bad input; direction for order must be either BUY or SELL.")
        self.direction = direction.uppper()
        self.stock = stock
        self.timestamp = timestamp

    def format_for_save(self):
        return {
            "Timestamp": self.timestamp,
            "Direction": self.direction,
            "Symbol": self.stock.symbol,
            "Price": self.stock.price,
            "Shares": self.stock.shares,
        }


class Transactions:
    def __init__(self, portfolio: Portfolio):
        self.portfolio = Portfolio
        self.session_transactions = []

    def add_order(self, order: Order):
        self.session_transactions.append(order)
        print(f"{order.direction} order for {order.stock.shares} shares of {order.stock.symbol} recorded.")

    def __str__(self):
        return f"{len(self.session_transactions)} orders executed so far."


