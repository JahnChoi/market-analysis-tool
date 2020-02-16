class EnvironmentNotConfiguredException(Exception):
    """
    Exception raised for an environment not configured with proper environment variables.
    """
    # Prevents '__main__' from being printed with the exception
    __module__ = 'builtins'


class StockSymbolNotValidException(Exception):
    """
    Exception raised for a stock symbol not supported by IEX Cloud API.
    """
    # Prevents '__main__' from being printed with the exception
    __module__ = 'builtins'