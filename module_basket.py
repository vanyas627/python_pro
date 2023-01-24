import module_exception
class Basket:
    def __init__(self, currency, customer, *args):
        self.currency = currency
        self.customer = customer
        self.goods = args

    def cost(self):
        summa = 0
        for el in self.goods:
            if int(el.price) <= 0:
                raise module_exception.PriceError(el.price)
            else:
                summa += int(el.price)

        return summa


    def __str__(self):
        return f'BASKET:\n Goods - [{",".join(el.name for el in self.goods)}]\n Customer - [{self.customer}]\n Cost for all: {self.cost()} {self.currency} '