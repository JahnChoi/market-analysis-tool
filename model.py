from iexfinance.altdata import get_social_sentiment
from iexfinance.stocks import Stock, get_historical_data
from datetime import date, timedelta
import json
import time


class BasicMarketAnalysis():
    def __init__(self, stock_symbols):
        self._stock_symbols      = stock_symbols
        self._iex_stock_obj      = Stock(stock_symbols)
        self._company_names      = self._iex_stock_obj.get_company_name()
        self._final_analysis_str = '\n\n'
        # self._key_stats          = self._iex_stock_obj.get_key_stats()

    def __str__(self):
        return self._final_analysis_str

    def analyze_social_sentiment(self):
        self._final_analysis_str += 'Public Twitter sentiment analysis (-1.0 to 1.0)...\n'
        for symbol in self._stock_symbols:
            sentiment_data = get_social_sentiment(symbol)
            sentiment_value = sentiment_data['sentiment']
            if sentiment_value > 0.5:
                self._final_analysis_str += symbol.upper() + ' BULLISH with public Twitter sentiment value of ' + str(sentiment_value) + '\n'
            else:
                self._final_analysis_str += symbol.upper() + ' BEARISH with public Twitter sentiment value of ' + str(sentiment_value) + '\n'
        self._final_analysis_str += '\n\n'

    def analyze_historical_data(self):
        today = date.today()
        datetime_five_years_ago = today - timedelta(days=7) #1825
        return get_historical_data(self._stock_symbols, datetime_five_years_ago, today, filter='changeOverTime')

    def relevant_stocks(self):
        self._final_analysis_str += 'Relevant stocks to keep in mind...\n'
        if(len(self._stock_symbols) == 1):
            relevant_stocks_list = self._iex_stock_obj.get_relevant_stocks()['symbols']
            for symbol in relevant_stocks_list:
                self._final_analysis_str += symbol.upper() + ' '
        else:
            relevant_stocks = self._iex_stock_obj.get_relevant_stocks()
            for symbol, company in zip(self._stock_symbols, self._company_names.values()):
                self._final_analysis_str += company + ': '
                for relevant_symbol in relevant_stocks[symbol.upper()]['symbols']:
                    self._final_analysis_str += relevant_symbol + ' '
                self._final_analysis_str += '\n'
        self._final_analysis_str += '\n\n'