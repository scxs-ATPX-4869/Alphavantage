from .model import Base, BalanceSheet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import logging

logger = logging.getLogger("BalanceSheetDBManager")
logger.setLevel(logging.DEBUG)

# create console handler and set level to info
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# create file handler and set level to debug
file_handler = logging.FileHandler("log/BalanceSheetDBManager.log")
file_handler.setLevel(logging.DEBUG)

# set logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


class DBManager:
    def __init__(
            self,
            password: str,
            database: str,
            *,
            user: str = "postgres",
            host: str = "localhost",
            port: int = 5432,
                 ):
        DB_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

        self.engine = create_engine(DB_URL, echo=False)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)


    def add_balance_sheet(self, data: dict):
        row = BalanceSheet(
            symbol=data.get("symbol"),
            report_type=data.get("report_type"),
            fiscalDateEnding=DBManager.parse_date(data.get("fiscalDateEnding")),
            reportedCurrency=data.get("reportedCurrency"),
            totalAssets=data.get("totalAssets"),
            totalCurrentAssets=data.get("totalCurrentAssets"),
            cashAndCashEquivalentsAtCarryingValue=data.get("cashAndCashEquivalentsAtCarryingValue"),
            cashAndShortTermInvestments=data.get("cashAndShortTermInvestments"),
            inventory=data.get("inventory"),
            currentNetReceivables=data.get("currentNetReceivables"),
            totalNonCurrentAssets=data.get("totalNonCurrentAssets"),
            propertyPlantEquipment=data.get("propertyPlantEquipment"),
            accumulateDepreciationAmortizationPPE=data.get("accumulateDepreciationAmortizationPPE"),
            intangibleAssets=data.get("intangibleAssets"),
            intangibleAssetsExcludingGoodwill=data.get("intangibleAssetsExcludingGoodwill"),
            goodwill=data.get("goodwill"),
            investments=data.get("investments"),
            longTermInvestments=data.get("longTermInvestments"),
            shortTermInvestments=data.get("shortTermInvestments"),
            otherCurrentAssets=data.get("otherCurrentAssets"),
            otherNonCurrentAssets=data.get("otherNonCurrentAssets"),
            totalLiabilities=data.get("totalLiabilities"),
            totalCurrentLiabilities=data.get("totalCurrentLiabilities"),
            currentAccountsPayable=data.get("currentAccountsPayable"),
            deferredRevenue=data.get("deferredRevenue"),
            currentDebt=data.get("currentDebt"),
            shortTermDebt=data.get("shortTermDebt"),
            totalNonCurrentLiabilities=data.get("totalNonCurrentLiabilities"),
            capitalLeaseObligations=data.get("capitalLeaseObligations"),
            longTermDebt=data.get("longTermDebt"),
            currentLongTermDebt=data.get("currentLongTermDebt"),
            longTermDebtNoncurrent=data.get("longTermDebtNoncurrent"),
            shortLongTermDebtTotal=data.get("shortLongTermDebtTotal"),
            otherCurrentLiabilities=data.get("otherCurrentLiabilities"),
            otherNonCurrentLiabilities=data.get("otherNonCurrentLiabilities"),
            totalShareholderEquity=data.get("totalShareholderEquity"),
            treasuryStock=data.get("treasuryStock"),
            retainedEarnings=data.get("retainedEarnings"),
            commonStock=data.get("commonStock"),
            commonStockSharesOutstanding=data.get("commonStockSharesOutstanding"),
        )
        self.session.add(row)
        logger.info(f"Added balance sheet for symbol: {data.get('symbol')}")

    def commit(self):
        self.session.commit()
        logger.info("Successfully committed the session to the database.")

    @staticmethod
    def parse_date(date_str):
        """
        Parse date string to date object
        """
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except Exception:
            return None





