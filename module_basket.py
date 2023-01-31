import module_exception

class BasketIterrator:
    def __init__(self, lis):
        self.lis = lis
        self.index = 0

    def __next__(self):
        if self.index < len(self.lis):
            self.index = self.index + 1
            return self.lis[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self

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

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.goods[item]

        if isinstance(item, slice):
            start = 0 if item.start == None else item.start
            stop = len(self.goods) if item.stop == None else item.stop
            step = 1 if item.step == None else item.step
            lis_slice = []
            for i in range(start,stop,step):
                lis_slice.append(self.goods[i])
            return lis_slice
        else:
            raise TypeError

    def __len__(self):
        return len(self.goods)

    def __iter__(self):
        return BasketIterrator(self.goods)


    def __str__(self):
        return f'BASKET:\n Goods - [{",".join(el.name for el in self.goods)}]\n Customer - [{self.customer}]\n Cost for all: {self.cost()} {self.currency} '