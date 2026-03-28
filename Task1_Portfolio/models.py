"""
models.py
This module contains the core Object-Oriented representations of financial assets and the portfolio.
It strictly implements Encapsulation, Inheritance, and Polymorphism.
"""

class Asset:
    """
    Base class representing a generic financial asset.
    Demonstrates Inheritance as specific asset types will inherit from this class.
    """
    def __init__(self, symbol: str, quantity: float):
        self.symbol = symbol.upper()
        # Protected attribute: Encapsulation
        self._quantity = quantity 

    def get_current_value(self, current_price: float) -> float:
        """
        Calculates the current value of the asset.
        This method is intended to be overridden by subclasses (Polymorphism).
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def get_quantity(self) -> float:
        return self._quantity

    def reduce_quantity(self, amount: float):
        if amount <= self._quantity:
            self._quantity -= amount
        else:
            raise ValueError("Insufficient quantity to reduce.")

    def add_quantity(self, amount: float):
        self._quantity += amount


class Stock(Asset):
    """
    Represents a specific type of asset: Stock.
    Inherits from the Asset base class.
    """
    def __init__(self, symbol: str, quantity: float, average_cost: float):
        super().__init__(symbol, quantity)
        self.average_cost = average_cost

    def get_current_value(self, current_price: float) -> float:
        """
        Overrides the base method to provide stock-specific valuation.
        Demonstrates Polymorphism.
        """
        return self._quantity * current_price
        
    def get_profit_loss(self, current_price: float) -> float:
        """Calculates unrealized profit or loss based on average cost."""
        total_cost = self._quantity * self.average_cost
        return self.get_current_value(current_price) - total_cost


class Portfolio:
    """
    Manages a collection of assets and the account balance.
    Demonstrates strict Encapsulation by hiding balance and asset list.
    """
    def __init__(self, owner_name: str, initial_balance: float):
        self.owner_name = owner_name
        # Private attributes to prevent unauthorized modifications
        self.__balance = initial_balance 
        self.__assets = {} # Dictionary mapping symbol to Stock object

    def get_balance(self) -> float:
        """Getter for the private balance."""
        return self.__balance

    def deposit(self, amount: float):
        """Allows safe modification of the private balance."""
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def buy_stock(self, symbol: str, quantity: float, price: float) -> bool:
        """Executes a buy order, updates assets and deducts balance."""
        total_cost = quantity * price
        if total_cost > self.__balance:
            print(f"Transaction Failed: Insufficient funds. Required: ${total_cost:.2f}, Available: ${self.__balance:.2f}")
            return False
            
        self.__balance -= total_cost
        symbol = symbol.upper()
        
        if symbol in self.__assets:
            # Update existing stock position (average down/up)
            stock = self.__assets[symbol]
            total_existing_cost = stock.get_quantity() * stock.average_cost
            new_total_cost = total_existing_cost + total_cost
            new_quantity = stock.get_quantity() + quantity
            stock.average_cost = new_total_cost / new_quantity
            stock.add_quantity(quantity)
        else:
            # Add new stock position
            self.__assets[symbol] = Stock(symbol, quantity, price)
            
        print(f"Successfully bought {quantity} shares of {symbol} at ${price:.2f}.")
        return True

    def sell_stock(self, symbol: str, quantity: float, price: float) -> bool:
        """Executes a sell order, updates assets and adds to balance."""
        symbol = symbol.upper()
        if symbol not in self.__assets:
            print(f"Transaction Failed: You do not own {symbol}.")
            return False
            
        stock = self.__assets[symbol]
        if quantity > stock.get_quantity():
            print(f"Transaction Failed: You only own {stock.get_quantity()} shares of {symbol}.")
            return False
            
        # Execute sell
        revenue = quantity * price
        self.__balance += revenue
        stock.reduce_quantity(quantity)
        
        # Remove asset from portfolio if quantity hits zero
        if stock.get_quantity() == 0:
            del self.__assets[symbol]
            
        print(f"Successfully sold {quantity} shares of {symbol} at ${price:.2f}.")
        return True

    def get_all_assets(self) -> list:
        """Returns a list of all currently held assets."""
        return list(self.__assets.values())
