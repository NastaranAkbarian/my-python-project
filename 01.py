import yfinance as yf
import pandas as pd

initial_capital=1000
capital=initial_capital


data = yf.download("BTC-USD", start="2015-01-01",end="2022-12-31", interval="1d")


data ['weekday']= data.index.weekday

mondays = data[data['weekday']==0]
wednesdays = data[data['weekday']==2]

transactions = pd.merge(mondays[['Open']]
                        ,wednesdays[['Close']]
                        ,left_index=True
                        ,right_index=True
                        ,suffixes=['_buy','_sell']
                        )

for index, row in transactions.iterrows():
    btc_bought = capital / row['Open_buy']
    capital = btc_bought * row['Close_sell']

profit_or_loss = capital - initial_capital

print(f"sarmaye nahaii: {capital:.2f} dolar ")
if profit_or_loss > 0:
    print(f"shoma sood kardin: {profit_or_loss:.2f} dolar ")
else:
    print(f"shoma zarar kardin :{profit_or_loss:.2f} dolar ")

# print(data.head())

# print(data.info())