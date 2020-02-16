from iexfinance.account import get_usage, get_metadata
import json


class IEXUsage():
    def __init__(self):
        self._usage = get_usage()
        self._metadata = get_metadata()
    
    def __str__(self):
        aggregate_account = {'usage': self._usage, 'metadata': self._metadata}
        return json.dumps(aggregate_account, indent=4)