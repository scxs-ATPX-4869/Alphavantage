import requests
import logging

logger = logging.getLogger("AlphaVantage")
logger.setLevel(logging.DEBUG)

# create console handler and set level to info
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# create file handler and set level to debug
file_handler = logging.FileHandler("log/AlphaVantage.log")
file_handler.setLevel(logging.DEBUG)

# set logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


class AlphaVantage:
    def __init__(self, apikey:str):
        self.base_url = "https://www.alphavantage.co/query"
        self.apikey = apikey

    def balance_sheet(self, symbol:str) -> list[dict]:
        """
        Get the balance sheet of one company

        Param
        ----------
        `symbol`: The company which is publicly traded

        Return
        ----------
        List of dict, which contains quarterly reports with updated report_type
        """
        params = {
            "function": "balance_sheet",
            "symbol": symbol,
            "apikey": self.apikey,
        }
        response = requests.get(self.base_url, params)
        if response.ok:
            logger.info(f"Successfully fetched balance sheet for symbol: {symbol}")
        else:
            logger.error(f"Failed to fetch balance sheet for symbol: {symbol} with status code: {response.status_code}")
        response_data:dict = response.json()
        
        return self._parse_balance_sheet(response_data)
        
    @staticmethod
    def clean_value(data):
        """
        Clean the input value by converting it to an appropriate type or None
        """
        if data in (None, "", "None"):
            return None
        if isinstance(data, str) and data.isdigit():
            return int(data)
        return data
    
    @staticmethod
    def clean_dict(d:dict):
        """
        Clean the input dictionary by applying clean_value to each value
        """
        return {k: AlphaVantage.clean_value(d) for k, d in d.items()}
    
    def _parse_balance_sheet(self, data: dict) -> list[dict]:
        """
        Parse balance sheet data. And add symbol and report_type fields

        :return:
        List of dict, which contains quarterly reports with updated report_type
        """
        symbol = data.get("symbol", "")
        # get date of annual reports
        annual_dates: list = []
        for annual_report in data.get("annualReports", []):
            annual_dates.append(annual_report.get("fiscalDateEnding"))
        # parse quarterly reports
        balance_sheets: list = []
        for quarterly_report in data.get("quarterlyReports", []):
            report_clean = self.clean_dict(quarterly_report)
            report_clean["symbol"] = symbol
            if report_clean.get("fiscalDateEnding") in annual_dates: # update report_type to annually if fiscalDateEnding is in annual_dates
                report_clean["report_type"] = "annually"
            else:
                report_clean["report_type"] = "quarterly"
            balance_sheets.append(report_clean)
        return balance_sheets
    



    


