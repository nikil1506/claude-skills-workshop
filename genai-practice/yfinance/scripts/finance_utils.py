import yfinance as yf


def resolve_symbol(query):
    """Turn a company name or ticker into a Yahoo Finance symbol."""
    query = query.strip()
    try:
        quotes = yf.Search(query, max_results=1).quotes
    except Exception:
        quotes = []
    if quotes:
        return quotes[0]["symbol"]
    return query.upper()
