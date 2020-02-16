import basic_helper
from model import BasicMarketAnalysis
from iex_usage import IEXUsage


# Configure environment with appropriate environment variables
basic_helper.configure_environment('config.ini')

# Prompt user for stock symbols
stock_symbols = basic_helper.input_stock_symbols()

# Run basic model
model = BasicMarketAnalysis(stock_symbols)
print(model)

# Get IEX account usage
# usage = IEXUsage()
# print(usage)