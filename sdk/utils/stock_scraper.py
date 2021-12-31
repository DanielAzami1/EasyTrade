import requests
from bs4 import BeautifulSoup

"""
11/16/21

Class for StockScraper object, used to pull constituents list for various indexes (defined in index_url_map).
"""

class StockScraper:
    def __init__(self, index: str):
        self.index = index
        self.index_url_map = {
            "SNP500": self.get_stocklist_snp500,
            "SNP600": self.get_stocklist_snp600,
            "NASDAQ100": self.get_stocklist_nasdaq100,
            "FTSE100": self.get_stocklist_ftse100,
            "RUSSELL": self.get_stocklist_russell
        }
        self.constituents_list = self.index_url_map[self.index]()

    @staticmethod
    def get_stocklist_snp500():
        """Returns a dictionary containing a list of stocks scraped from Wikipedia's SNP500 index
        constitutents list. The dictionary key-value pairs are stored for simplicity as
        {asset name : ticker}"""
        URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        page = requests.get(URL).text
        soup = BeautifulSoup(page, features='html.parser')
        stocklist = {}
        stock_table = soup.find("table", id="constituents")
        stock_table_data = stock_table.tbody.find_all("tr")
        for row in stock_table_data:
            cells = row.find_all('a')
            stocklist[cells[1].find(text=True)] = cells[0].find(text=True)
        stocklist.pop("SEC filings")
        return stocklist

    @staticmethod
    def get_stocklist_snp600():
        URL = "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies"
        page = requests.get(URL).text
        soup = BeautifulSoup(page, features='html.parser')
        stocklist = {}
        stock_table = soup.find("table", {"class": "wikitable sortable"})
        stock_table_data = stock_table.find_all("tr")

        for row in stock_table_data:
            ticker = row.find_all('td')
            if len(ticker) < 2:
                continue
            stocklist[ticker[0].text.rstrip()] = ticker[1].text.rstrip()
        return stocklist

    @staticmethod
    def get_stocklist_nasdaq100():
        URL = "https://en.wikipedia.org/wiki/NASDAQ-100"
        page = requests.get(URL).text
        soup = BeautifulSoup(page, features='html.parser')
        stocklist = {}
        stock_table = soup.find("table", id="constituents")
        stock_table_data = stock_table.tbody.find_all("tr")
        for row in stock_table_data:
            ticker = row.find_all('td')
            if len(ticker) < 4:
                continue
            stocklist[ticker[0].text] = ticker[1].text
        return stocklist

    @staticmethod
    def get_stocklist_ftse100():
        URL = "https://en.wikipedia.org/wiki/FTSE_100_Index"
        page = requests.get(URL).text
        soup = BeautifulSoup(page, features='html.parser')
        stocklist = {}
        stock_table = soup.find("table", id="constituents")
        stock_table_data = stock_table.tbody.find_all("tr")
        for row in stock_table_data:
            ticker = row.find_all('td')
            if len(ticker) < 3:
                continue
            stocklist[ticker[0].text] = ticker[1].text
        return stocklist

    @staticmethod
    def get_stocklist_russell():
        URL = "https://en.wikipedia.org/wiki/Russell_1000_Index"
        page = requests.get(URL).text
        soup = BeautifulSoup(page, features='html.parser')
        stocklist = {}
        stock_table = soup.find("table", {"class": "wikitable sortable"})
        stock_table_data = stock_table.find_all("tr")

        for row in stock_table_data:
            ticker = row.find_all('td')
            if len(ticker) < 2:
                continue
            stocklist[ticker[0].text] = ticker[1].text.rstrip()
        return stocklist


if __name__ == "__main__":
    stocklist_test = StockScraper("NASDAQ100")
    stocklist_test = stocklist_test.constituents_list
    print(stocklist_test)
