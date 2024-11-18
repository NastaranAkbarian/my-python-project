import yfinance as yf
import pandas as pd

# سرمایه اولیه
initial_capital = 1000
capital = initial_capital

# دانلود داده‌ها از یاهو فاینانس
data = yf.download("BTC-USD", start="2015-01-01", end="2022-12-31", interval="1d")

# استخراج روزهای هفته (6 برای یکشنبه، 2 برای چهارشنبه)
data['weekday'] = data.index.weekday

# داده‌های یکشنبه و چهارشنبه
sundays = data[data['weekday'] == 6]
wednesdays = data[data['weekday'] == 2]

# جفت کردن داده‌های یکشنبه و چهارشنبه که فاصله‌شان کمتر از 3 روز است (یکشنبه و چهارشنبه همان هفته)
valid_transactions = []

for sunday_date, sunday_row in sundays.iterrows():
    # جستجو برای چهارشنبه همان هفته
    potential_wednesdays = wednesdays[wednesdays.index > sunday_date]

    # اگر پیدا کردیم چهارشنبه در فاصله 3 روز بعد از یکشنبه
    for wednesday_date, wednesday_row in potential_wednesdays.iterrows():
        if (wednesday_date - sunday_date).days <= 3:
            valid_transactions.append((sunday_row['Open'], wednesday_row['Close']))

# اگر هیچ معامله معتبر پیدا نکردیم، پیامی نمایش بده
if not valid_transactions:
    print("هیچ معامله‌ای پیدا نشد.")
else:
    # شبیه‌سازی معاملات
    capital = float(initial_capital)  # اطمینان از اینکه capital عددی (float) است
    for buy_price, sell_price in valid_transactions:
        # خرید بیت‌کوین در یکشنبه
        # فقط استخراج مقادیر عددی از Series
        btc_bought = capital / float(buy_price)
        # فروش بیت‌کوین در چهارشنبه
        capital = btc_bought * float(sell_price)

    # نمایش مقادیر intermediate برای بررسی
    print(f"مقدار نهایی capital: {capital}")

    # محاسبه سود یا زیان نهایی
    profit_or_loss = capital - initial_capital
    print(f"مقدار سود/زیان: {profit_or_loss}")

    # اطمینان از اینکه capital عددی است
    if isinstance(capital, float):  # اطمینان از اینکه capital عددی (float) است
        print(f"sarmaye nahaii: {capital:.2f} dolar ")
    else:
        print(f"اشتباه در محاسبات: نوع capital صحیح نیست.")

    # اطمینان از اینکه profit_or_loss عددی است
    if isinstance(profit_or_loss, (int, float)):  # بررسی نوع داده
        if profit_or_loss > 0:
            print(f"shoma sood kardin: {profit_or_loss:.2f} dolar ")
        else:
            print(f"shoma zarar kardin :{profit_or_loss:.2f} dolar ")
    else:
        print("خطا: مقدار سود یا زیان صحیح نیست.")
