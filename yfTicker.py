import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info

info = msft.info
print('Printing msft info: ')
print(info)
print('\n')

# get historical market data
hist = msft.history(period="max")
print('Printing historical market data: ')
print(hist)

# show actions (dividends, splits)
actions = msft.actions
print('Printing msft actuibs: ')
print(actions)
print('\n')

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show major holders
msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# get option chain for specific expiration

# leave like this to get options list
#opt = msft.option_chain('YYYY-MM-DD')

opt = msft.option_chain('2023-03-17')
# data available via: opt.calls, opt.puts