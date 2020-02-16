from iexfinance.stocks import Stock
import json


class BasicMarketAnalysis():
    def __init__(self, stock_symbols):
        self._stock_symbols = stock_symbols
        self._iex_stock_obj = Stock(stock_symbols)
        self._key_stats     = self._iex_stock_obj.get_key_stats()

    def __str__(self):
        return json.dumps(self._key_stats, indent=4)