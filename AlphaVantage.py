import requests
import json
import logging


class AlphaVantage:
    def __init__(self, apikey:str):
        self.base_url = "https://www.alphavantage.co/query"
        self.apikey = apikey

    def balance_sheet(self, symbol:str) -> dict:
        """
        Get the balance sheet of one company

        Param
        ----------
        symbol: The company which is publicly traded
        """
        params = {
            "function": "balance_sheet",
            "symbol": symbol,
            "apikey": self.apikey,
        }
        response = requests.get(self.base_url, params)
        response_data:dict = response.json()
        
        return response_data
    


