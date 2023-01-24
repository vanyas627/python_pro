import module_exception
class Goods:
    def __init__(self,name,price,currency,description):
        if int(price) <= 0:
            raise module_exception.PriceError(f"Wrong price:{price} UAH")

        self.name = name
        self.price = price
        self.currency = currency
        self.description = description

    def __str__(self):
        return f"Goods name: {self.name}, Price: {self.price} {self.currency} Description: {self.description}"