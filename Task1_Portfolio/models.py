class Asset:
    def __init__(self, symbol, quantity):
        self.symbol = symbol.upper()
        self._quantity = quantity 

    def get_current_value(self, current_price):
        pass

class Stock(Asset):
    def __init__(self, symbol, quantity, purchase_price):
        super().__init__(symbol, quantity)
        self.purchase_price = purchase_price

    def get_current_value(self, current_price):
        return self._quantity * current_price
        
    def get_profit_loss(self, current_price):
        total_cost = self._quantity * self.purchase_price
        current_value = self.get_current_value(current_price)
        return current_value - total_cost

class Portfolio:
    def __init__(self, owner_name, initial_balance):
        self.owner_name = owner_name
        self.__balance = initial_balance 
        self.__assets = [] 

    def add_asset(self, asset):
        self.__assets.append(asset)
        print(f"Asset added successfully: {asset.symbol}")

    def get_assets(self):
        return self.__assets
        
    def get_balance(self):
        return self.__balance
