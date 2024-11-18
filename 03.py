import yfinance as yf
import pandas as pd

# دانلود داده‌ها از یاهو فاینانس
data = yf.download("BTC-USD", start="2015-01-01", end="2022-12-31", interval="1d")

# استخراج روزهای هفته (6 برای یکشنبه، 2 برای چهارشنبه)
data['weekday'] = data.index.weekday

# نمایش تعداد داده‌های یکشنبه و چهارشنبه
sundays = data[data['weekday'] == 6]
wednesdays = data[data['weekday'] == 2]

print(f"تعداد روزهای یکشنبه: {len(sundays)}")
print(f"تعداد روزهای چهارشنبه: {len(wednesdays)}")

transactions = pd.merge(sundays[['Open']], wednesdays[['Close']], left_index=True, right_index=True, suffixes=['_buy', '_sell'])

print(f"تعداد معاملات: {len(transactions)}")
print(transactions.head())

