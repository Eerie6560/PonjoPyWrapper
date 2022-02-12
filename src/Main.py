import sys
from src.utils.StartupUtil import StartupUtil
from src.managers.EndpointManager import EndpointManager

class Main:

    def __init__(self, key: str):
        self.key = key
        self.endpointManager = EndpointManager(self.key)
        if not StartupUtil().isApiKeyValid():
            print("An invalid API key was provided. Please obtain one by emailing benpetrillo@ponjo.club.")
            sys.exit(0)

    def getEndpointManager(self):
        return self.endpointManager