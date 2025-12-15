from libs.AlphaVantage import AlphaVantage
from libs.BalanceSheetDBMange import DBManager
import tomllib
import json
from pathlib import Path

CONFIG_PATH = Path("config/config.toml")

with open(CONFIG_PATH, "rb") as f:
    config = tomllib.load(f)
API_KEY = config.get("ALPHAVANTAGE_API_KEY", "")
DB_PASSWORD = config.get("DB_PASSWORD", "")
DATABASE_NAME = config.get("DATABASE_NAME", "")


alv = AlphaVantage(apikey=API_KEY)
# dbm = DBManager(password=DB_PASSWORD, database=DATABASE_NAME)

# balance_sheets = alv.balance_sheet(symbol="AAPL")
# for reprot in balance_sheets:
#     dbm.add_balance_sheet(reprot)
# dbm.commit()


apple_overview = alv.overview(symbol="AAPL")
with open("apple_overview.json", "w") as f:
    f.write(json.dumps(apple_overview, indent=2, ensure_ascii=False))
