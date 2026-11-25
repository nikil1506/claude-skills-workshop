import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

from finance_utils import resolve_symbol

user_input = input("Enter two or more tickers or company names, separated by commas (e.g., AAPL, Microsoft, META): ")
queries = [q for q in (s.strip() for s in user_input.split(",")) if q]
if len(queries) < 2:
    raise SystemExit("Please enter at least two companies or tickers.")

closes = {}
for q in queries:
    symbol = resolve_symbol(q)
    history = yf.Ticker(symbol).history(period="5y")
    if history.empty:
        print(f"Skipping '{q}' ({symbol}): no price data found.")
        continue
    closes[symbol] = history["Close"]

if len(closes) < 2:
    raise SystemExit("Need price data for at least two companies to compare.")

prices = pd.DataFrame(closes).dropna()
normalized = (prices / prices.iloc[0] - 1) * 100

summary = pd.DataFrame({
    "Start Price": prices.iloc[0].round(2),
    "End Price": prices.iloc[-1].round(2),
    "5Y Return (%)": normalized.iloc[-1].round(2),
    "High": prices.max().round(2),
    "Low": prices.min().round(2),
}).sort_values("5Y Return (%)", ascending=False)

print("--- 5-Year Comparison ---")
print(summary.to_string())

normalized.plot(title="5-Year Normalized Return (%)")
plt.xlabel("Date")
plt.ylabel("Return (%)")
plt.axhline(0, color="gray", linewidth=0.8)
plt.legend(title="Ticker")
plt.show()
