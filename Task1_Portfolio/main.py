from models import Stock, Portfolio
from utils import get_mock_price, print_separator

def main():
    print_separator()
    print("Personal Portfolio Management System")
    print_separator()

    my_portfolio = Portfolio(owner_name="HKMU Student", initial_balance=10000.0)
    print(f"User: {my_portfolio.owner_name} | Initial Balance: ${my_portfolio.get_balance()}")

    stock1 = Stock(symbol="AAPL", quantity=10, purchase_price=165.0)
    stock2 = Stock(symbol="TSLA", quantity=5, purchase_price=210.0)
    
    my_portfolio.add_asset(stock1)
    my_portfolio.add_asset(stock2)
    
    print_separator()
    print("--- Current Portfolio Status ---")
    
    total_portfolio_value = 0.0
    
    for asset in my_portfolio.get_assets():
        current_price = get_mock_price(asset.symbol)
        
        current_value = asset.get_current_value(current_price)
        pnl = asset.get_profit_loss(current_price)
        
        total_portfolio_value += current_value
        
        print(f"Stock: {asset.symbol}")
        print(f"  Quantity: {asset._quantity} | Current Price: ${current_price}")
        print(f"  Market Value: ${current_value:.2f}")
        print(f"  Unrealized P&L: ${pnl:.2f}\n")

    print_separator()
    print(f"Total Portfolio Value: ${total_portfolio_value:.2f}")
    print_separator()

if __name__ == "__main__":
    main()
