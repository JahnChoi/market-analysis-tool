import configparser
import decorators
from globals import SANDBOX_MODE, IEX_API_VERSION, IEX_TOKEN
import os

def configure_environment(config_file):
    """
    Configures the environment with the given configuration file to properly call the IEX Cloud API.
    """
    # Read configuration file
    config = configparser.ConfigParser()
    config.read(config_file)

    # Set globals
    global SANDBOX_MODE, IEX_API_VERSION, IEX_TOKEN
    SANDBOX_MODE    = config['DEFAULT'].getboolean('SandboxMode')
    IEX_API_VERSION = 'iexcloud-sandbox' if SANDBOX_MODE else 'v1'
    IEX_TOKEN       = config['DEFAULT']['IEXTokenSandbox'].strip() if SANDBOX_MODE else config['DEFAULT']['IEXToken'].strip()

    # Set environment variables
    os.environ['IEX_API_VERSION'] = IEX_API_VERSION
    os.environ['IEX_TOKEN']       = IEX_TOKEN


@decorators.verify_environment
def input_stock_symbols():
    """
    Prompts the user for comma delimited stock symbol(s).
    """
    raw_input_str = input('Enter stock symbols to analyze (comma delimited): ')
    stock_symbols = [symbol.strip().upper() for symbol in raw_input_str.split(',')]
    return stock_symbols