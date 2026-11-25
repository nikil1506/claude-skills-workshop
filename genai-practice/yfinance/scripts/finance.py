import matplotlib.pyplot as plt
import yfinance as yf

from finance_utils import resolve_symbol


def fmt_money(value):
    if value is None:
        return "N/A"
    if isinstance(value, (int, float)):
        return f"${value:,}"
    return f"${value}"


user_input = input("Enter the stock ticker symbol or a company name (e.g., AAPL, MSFT, META, Apple): ")
ticker_symbol = resolve_symbol(user_input)
print(f"Using ticker: {ticker_symbol}")

ticker = yf.Ticker(ticker_symbol)
data = ticker.history(period="5y")

if data.empty:
    raise SystemExit(f"No price data found for '{user_input}'.")

print(data.to_string())
data['Close'].plot(title=f"{ticker_symbol} Stock Price (Last 5 Years)")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.show()

stock_info = ticker.info

print("--- Key Company Fundamentals & Info ---")
print(f"Company Name: {stock_info.get('longName', 'N/A')}")
print(f"Current Price: {fmt_money(stock_info.get('currentPrice'))}")
print(f"Market Cap: {fmt_money(stock_info.get('marketCap'))}")
print(f"Trailing P/E Ratio: {stock_info.get('trailingPE', 'N/A')}")
print(f"52-Week High: {fmt_money(stock_info.get('fiftyTwoWeekHigh'))}")
print("\n" + "="*50 + "\n")


print("--- Corporate Financials ---")
print("\nAnnual Income Statement (Last Year):")
financials = ticker.financials
if financials.empty:
    print("No annual financials available.")
else:
    print(financials.iloc[:, 0].head())

print("\n--- Upcoming Actions & Earnings ---")
print("Dividends & Splits History:")
print(ticker.actions.tail())

print("\nCalendar Events (Next Earnings Date):")
print(ticker.calendar)
