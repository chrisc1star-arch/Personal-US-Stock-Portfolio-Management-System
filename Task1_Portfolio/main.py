"""
main.py
The entry point of the Personal US Stock Portfolio Management System.
Provides an interactive command-line interface (CLI) for the user.
"""
from models import Portfolio
from utils import get_current_price, print_header, print_menu

def view_dashboard(portfolio: Portfolio):
    """Retrieves and displays the current state of the portfolio."""
    print_header("PORTFOLIO DASHBOARD")
    print(f"Account Owner: {portfolio.owner_name}")
    print(f"Available Cash Balance: ${portfolio.get_balance():.2f}\n")
    
    assets = portfolio.get_all_assets()
    if not assets:
        print("Your portfolio is currently empty.")
        return

    total_stock_value = 0.0
    print(f"{'Symbol':<8} | {'Shares':<8} | {'Avg Cost':<10} | {'Current':<10} | {'Market Val':<12} | {'P&L':<10}")
    print("-" * 70)
    
    for stock in assets:
        current_price = get_current_price(stock.symbol)
        
        # Polymorphic method call
        market_value = stock.get_current_value(current_price)
        pnl = stock.get_profit_loss(current_price)
        
        total_stock_value += market_value
        
        # Format P&L with sign
        pnl_str = f"+${pnl:.2f}" if pnl >= 0 else f"-${abs(pnl):.2f}"
        
        print(f"{stock.symbol:<8} | {stock.get_quantity():<8.2f} | ${stock.average_cost:<9.2f} | ${current_price:<9.2f} | ${market_value:<11.2f} | {pnl_str:<10}")

    print("-" * 70)
    total_assets = portfolio.get_balance() + total_stock_value
    print(f"Total Stock Value: ${total_stock_value:.2f}")
    print(f"Total Account Net Worth: ${total_assets:.2f}")


def main():
    print_header("Welcome to Personal Portfolio Manager")
    
    # Initialize the portfolio
    user_name = input("Enter your name to open an account: ")
    my_portfolio = Portfolio(owner_name=user_name, initial_balance=10000.0)
    print(f"\nAccount created successfully. Initial deposit: $10,000.00")

    while True:
        print_menu()
        choice = input("Select an action (1-5): ")

        if choice == '1':
            view_dashboard(my_portfolio)
            
        elif choice == '2':
            print_header("BUY STOCK")
            symbol = input("Enter stock ticker (e.g., AAPL): ").upper()
            try:
                quantity = float(input(f"Enter number of shares to buy: "))
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                current_price = get_current_price(symbol)
                print(f"Current market price for {symbol} is ${current_price:.2f}.")
                confirm = input("Confirm purchase? (y/n): ")
                if confirm.lower() == 'y':
                    my_portfolio.buy_stock(symbol, quantity, current_price)
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '3':
            print_header("SELL STOCK")
            symbol = input("Enter stock ticker to sell: ").upper()
            try:
                quantity = float(input(f"Enter number of shares to sell: "))
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                current_price = get_current_price(symbol)
                print(f"Current market price for {symbol} is ${current_price:.2f}.")
                confirm = input("Confirm sale? (y/n): ")
                if confirm.lower() == 'y':
                    my_portfolio.sell_stock(symbol, quantity, current_price)
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == '4':
            print_header("DEPOSIT FUNDS")
            try:
                amount = float(input("Enter amount to deposit: $"))
                if my_portfolio.deposit(amount):
                    print(f"Successfully deposited ${amount:.2f}.")
                else:
                    print("Deposit amount must be positive.")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '5':
            print("\nThank you for using Personal Portfolio Manager. Goodbye!")
            break
            
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
    print_separator()

if __name__ == "__main__":
    main()
