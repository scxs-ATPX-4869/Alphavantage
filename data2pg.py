import json
from sqlalchemy import create_engine, Column, Integer, String, BigInteger, Date
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from datetime import datetime

DB_URL = "postgresql+psycopg2://postgres:password@localhost:5432/financial_data"

engine = create_engine(DB_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

# ORM Model
class BalanceSheet(Base):
    __tablename__ = "balance_sheet"
    
    # column of database
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(20)) # 公司的股票名称
    report_type = Column(String(20)) # 年报或季报
    fiscalDateEnding = Column(Date) # 财报报告结束日期
    reportedCurrency = Column(String(10)) # 财报货币
    totalAssets = Column(BigInteger) # 总资产
    totalCurrentAssets = Column(BigInteger) # 流动资产总额
    cashAndCashEquivalentsAtCarryingValue = Column(BigInteger) # 按账面价值计算的有价证券及现金等价物
    cashAndShortTermInvestments = Column(BigInteger) # 现金和有价证券投资
    inventory = Column(BigInteger) # 库存
    currentNetReceivables = Column(BigInteger) # 当前应收账款
    totalNonCurrentAssets = Column(BigInteger) # 总非流动资产
    propertyPlantEquipment = Column(BigInteger) # 不动产、厂房及设备
    accumulateDepreciationAmortizationPPE = Column(BigInteger) # 累计折旧摊销固定资产
    intangibleAssets = Column(BigInteger) # 无形资产
    intangibleAssetsExcludingGoodwill = Column(BigInteger) # 不包括商誉的无形资产
    goodwill = Column(BigInteger) # 商誉
    investments = Column(BigInteger) # 投资
    longTermInvestments = Column(BigInteger) # 长期投资
    shortTermInvestments = Column(BigInteger) # 短期投资
    otherCurrentAssets = Column(BigInteger) # 其他流动资产
    otherNonCurrentAssets = Column(BigInteger) # 其他非流动资产
    totalLiabilities = Column(BigInteger) # 总负债
    totalCurrentLiabilities = Column(BigInteger) # 总流动负债
    currentAccountsPayable = Column(BigInteger) # 应付账款
    deferredRevenue = Column(BigInteger) # 递延收入
    currentDebt = Column(BigInteger) # 短期债务：企业在一年内到期的负债，包括短期借款、应付票据、应付账款等
    shortTermDebt = Column(BigInteger) # 短期负债：在一年或更短时间内到期的债务
    totalNonCurrentLiabilities = Column(BigInteger) # 总非流动负债
    capitalLeaseObligations = Column(BigInteger) # 资本租赁义务
    longTermDebt = Column(BigInteger) # 长期负债
    currentLongTermDebt = Column(BigInteger) # 当前长期负债
    longTermDebtNoncurrent = Column(BigInteger) # 长期非流动债务
    shortLongTermDebtTotal = Column(BigInteger) # 短期长期债务总额
    otherCurrentLiabilities = Column(BigInteger) # 其他流动负债
    otherNonCurrentLiabilities = Column(BigInteger) # 其他非流动负债
    totalShareholderEquity = Column(BigInteger) # 股东权益总额
    treasuryStock = Column(BigInteger) # 国库股票：被公司回购并作为资产持有的股票
    retainedEarnings = Column(BigInteger) # 留存收益
    commonStock = Column(BigInteger) # 普通股
    commonStockSharesOutstanding = Column(BigInteger) # 流通在外的普通股股数

    
def clean_value(data):
    if data in (None, "", "None"):
        return None
    if isinstance(data, str) and data.isdigit():
        return int(data)
    return data

def clean_dict(d:dict):
    return {k: clean_value(d) for k, d in d.items()}

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except Exception:
        return None
    
with open("D:\python_project\NVDA_balance_sheet.json", "r", encoding="utf-8") as f:
    data = json.load(f)

symbol = data.get("symbol", "")
# insert quarterly reports
for report in data.get("quarterlyReports", []):
    reprot_clean = clean_dict(report)

    row = BalanceSheet(
        symbol=symbol,
        report_type="quarterly",
        fiscalDateEnding=parse_date(reprot_clean.get("fiscalDateEnding")),
        reportedCurrency=reprot_clean.get("reportedCurrency"),
        totalAssets=reprot_clean.get("totalAssets"),
        totalCurrentAssets=reprot_clean.get("totalCurrentAssets"),
        cashAndCashEquivalentsAtCarryingValue=reprot_clean.get("cashAndCashEquivalentsAtCarryingValue"),
        cashAndShortTermInvestments=reprot_clean.get("cashAndShortTermInvestments"),
        inventory=reprot_clean.get("inventory"),
        currentNetReceivables=reprot_clean.get("currentNetReceivables"),
        totalNonCurrentAssets=reprot_clean.get("totalNonCurrentAssets"),
        propertyPlantEquipment=reprot_clean.get("propertyPlantEquipment"),
        accumulateDepreciationAmortizationPPE=reprot_clean.get("accumulateDepreciationAmortizationPPE"),
        intangibleAssets=reprot_clean.get("intangibleAssets"),
        intangibleAssetsExcludingGoodwill=reprot_clean.get("intangibleAssetsExcludingGoodwill"),
        goodwill=reprot_clean.get("goodwill"),
        investments=reprot_clean.get("investments"),
        longTermInvestments=reprot_clean.get("longTermInvestments"),
        shortTermInvestments=reprot_clean.get("shortTermInvestments"),
        otherCurrentAssets=reprot_clean.get("otherCurrentAssets"),
        otherNonCurrentAssets=reprot_clean.get("otherNonCurrentAssets"),
        totalLiabilities=reprot_clean.get("totalLiabilities"),
        totalCurrentLiabilities=reprot_clean.get("totalCurrentLiabilities"),
        currentAccountsPayable=reprot_clean.get("currentAccountsPayable"),
        deferredRevenue=reprot_clean.get("deferredRevenue"),
        currentDebt=reprot_clean.get("currentDebt"),
        shortTermDebt=reprot_clean.get("shortTermDebt"),
        totalNonCurrentLiabilities=reprot_clean.get("totalNonCurrentLiabilities"),
        capitalLeaseObligations=reprot_clean.get("capitalLeaseObligations"),
        longTermDebt=reprot_clean.get("longTermDebt"),
        currentLongTermDebt=reprot_clean.get("currentLongTermDebt"),
        longTermDebtNoncurrent=reprot_clean.get("longTermDebtNoncurrent"),
        shortLongTermDebtTotal=reprot_clean.get("shortLongTermDebtTotal"),
        otherCurrentLiabilities=reprot_clean.get("otherCurrentLiabilities"),
        otherNonCurrentLiabilities=reprot_clean.get("otherNonCurrentLiabilities"),
        totalShareholderEquity=reprot_clean.get("totalShareholderEquity"),
        treasuryStock=reprot_clean.get("treasuryStock"),
        retainedEarnings=reprot_clean.get("retainedEarnings"),
        commonStock=reprot_clean.get("commonStock"),
        commonStockSharesOutstanding=reprot_clean.get("commonStockSharesOutstanding"),
        )
    session.add(row)

session.commit()
session.close()

print("Data inserted successfully.")


