def get_mock_price(symbol):
    mock_prices = {
        "AAPL": 170.50,
        "TSLA": 200.20,
        "MSFT": 410.00,
        "GOOG": 140.30
    }
    return mock_prices.get(symbol.upper(), 100.0)

def print_separator():
    print("-" * 50)
