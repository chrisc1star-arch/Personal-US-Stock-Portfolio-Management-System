"""
utils.py
Contains helper functions for UI and mock data fetching.
Separating these functions fulfills the modular programming requirement.
"""
import random

def get_current_price(symbol: str) -> float:
    """
    Simulates fetching real-time market data from a financial API.
    In a real-world scenario, this would use 'yfinance' or similar libraries.
    """
    # Base mock prices for common tickers
    base_prices = {
        "AAPL": 170.0,
        "TSLA": 200.0,
        "MSFT": 410.0,
        "GOOG": 140.0,
        "NVDA": 850.0
    }
    
    symbol = symbol.upper()
    base_price = base_prices.get(symbol, 100.0) # Default to 100 if unknown
    
    # Introduce a slight random fluctuation (-2% to +2%) to simulate live market
    fluctuation = random.uniform(-0.02, 0.02)
    current_price = base_price * (1 + fluctuation)
    
    return round(current_price, 2)

def print_header(title: str):
    """Utility function to print formatted headers."""
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)

def print_menu():
    """Displays the main application menu."""
    print("\n--- Main Menu ---")
    print("1. View Portfolio Dashboard")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. Deposit Funds")
    print("5. Exit Application")
    print("-----------------")
