import basic_helper
from model import BasicMarketAnalysis
from iex_usage import IEXUsage

# Suppress warnings for social sentiment endpoint
import warnings
warnings.filterwarnings("ignore")

# Configure environment with appropriate environment variables
basic_helper.configure_environment('config.ini')

# Prompt user for stock symbols
stock_symbols = basic_helper.input_stock_symbols()

# Run basic model sentiment analysis
model = BasicMarketAnalysis(stock_symbols)
model.analyze_social_sentiment()
model.relevant_stocks()
print(model)

# Get IEX account usage
print('IEX Cloud Usage:')
usage = IEXUsage()
print(usage)