from sqlalchemy import Column, Integer, String, BigInteger, Date
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class BalanceSheet(Base):
    __tablename__ = "balance_sheet"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(20))
    report_type = Column(String(20))
    fiscalDateEnding = Column(Date)
    reportedCurrency = Column(String(10))
    totalAssets = Column(BigInteger)
    totalCurrentAssets = Column(BigInteger)
    cashAndCashEquivalentsAtCarryingValue = Column(BigInteger)
    cashAndShortTermInvestments = Column(BigInteger)
    inventory = Column(BigInteger)
    currentNetReceivables = Column(BigInteger)
    totalNonCurrentAssets = Column(BigInteger)
    propertyPlantEquipment = Column(BigInteger)
    accumulateDepreciationAmortizationPPE = Column(BigInteger)
    intangibleAssets = Column(BigInteger)
    intangibleAssetsExcludingGoodwill = Column(BigInteger)
    goodwill = Column(BigInteger)
    investments = Column(BigInteger)
    longTermInvestments = Column(BigInteger)
    shortTermInvestments = Column(BigInteger)
    otherCurrentAssets = Column(BigInteger)
    otherNonCurrentAssets = Column(BigInteger)
    totalLiabilities = Column(BigInteger)
    totalCurrentLiabilities = Column(BigInteger)
    currentAccountsPayable = Column(BigInteger)
    deferredRevenue = Column(BigInteger)
    currentDebt = Column(BigInteger)
    shortTermDebt = Column(BigInteger)
    totalNonCurrentLiabilities = Column(BigInteger)
    capitalLeaseObligations = Column(BigInteger)
    longTermDebt = Column(BigInteger)
    currentLongTermDebt = Column(BigInteger)
    longTermDebtNoncurrent = Column(BigInteger)
    shortLongTermDebtTotal = Column(BigInteger)
    otherCurrentLiabilities = Column(BigInteger)
    otherNonCurrentLiabilities = Column(BigInteger)
    totalShareholderEquity = Column(BigInteger)
    treasuryStock = Column(BigInteger)
    retainedEarnings = Column(BigInteger)
    commonStock = Column(BigInteger)
    commonStockSharesOutstanding = Column(BigInteger)

class CahsFlow(Base):
    __tablename__ = "cash_flow"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(20))
    report_type = Column(String(20))




class IncomeStatement(Base):
    __tablename__ = "income_statement"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(20))
    report_type = Column(String(20))



