import yfinance as yf
import pandas as pd

# سرمایه اولیه
initial_capital = 1000
capital = initial_capital

# دانلود داده‌ها از یاهو فاینانس
data = yf.download("BTC-USD", start="2015-01-01", end="2022-12-31", interval="1d")

# استخراج روزهای هفته (6 برای یکشنبه، 2 برای چهارشنبه)
data['weekday'] = data.index.weekday

# داده‌های یکشنبه (خرید) و چهارشنبه (فروش)
sundays = data[data['weekday'] == 6]
wednesdays = data[data['weekday'] == 2]

# ترکیب داده‌های یکشنبه (خرید) و چهارشنبه (فروش)
transactions = pd.merge(sundays[['Open']], wednesdays[['Close']], left_index=True, right_index=True, suffixes=['_buy', '_sell'])

# متغیر برای ذخیره مقدار بیت‌کوین خریداری‌شده
btc_held = 0

# شبیه‌سازی معاملات
for index, row in transactions.iterrows():
    # خرید بیت‌کوین در یکشنبه
    btc_bought = capital / row['Open_buy']
    # فروش بیت‌کوین در چهارشنبه
    capital = btc_bought * row['Close_sell']

# محاسبه سود یا زیان نهایی
profit_or_loss = capital - initial_capital

# نمایش نتیجه
print(f"sarmaye nahaii: {capital:.2f} dolar ")
if profit_or_loss > 0:
    print(f"shoma sood kardin: {profit_or_loss:.2f} dolar ")
else:
    print(f"shoma zarar kardin :{profit_or_loss:.2f} dolar ")
