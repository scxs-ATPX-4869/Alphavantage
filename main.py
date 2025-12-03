from libs.AlphaVantage import AlphaVantage
from libs.BalanceSheetDBMange import DBManager
import tomllib

with open("config.toml", "rb") as f:
    config = tomllib.load(f)
API_KEY = config.get("ALPHAVANTAGE_API_KEY", "")
DB_PASSWORD = config.get("DB_PASSWORD", "")
DATABASE_NAME = config.get("DATABASE_NAME", "")


alv = AlphaVantage(apikey=API_KEY)
dbm = DBManager(password=DB_PASSWORD, database=DATABASE_NAME)

balance_sheets = alv.balance_sheet(symbol="AAPL")
for reprot in balance_sheets:
    dbm.add_balance_sheet(reprot)
dbm.commit()



