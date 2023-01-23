class PriceError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"{self.msg}"

class Goods:
    def __init__(self,name,price,currency,description):
        self.name = name
        self.price = price
        self.currency = currency
        self.description = description

        if int(self.price) <= 0:
            raise PriceError(self.price)

    def __str__(self):
        return f"Goods name: {self.name}, Price: {self.price} {self.currency} Description: {self.description}"


class Customer:
    def __init__(self,name, surname, phone_number ):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"Name: {self.name}; Surname: {self.surname}; Phone number: {self.phone_number}"

class Basket:
    def __init__(self, currency, customer, *args):
        self.currency = currency
        self.customer = customer
        self.goods = args

    def cost(self):
        summa = 0
        for el in self.goods:
            if int(el.price) <= 0:
                raise PriceError("Wrong price!")
            else:
                summa += int(el.price)

        return summa


    def __str__(self):
        return f'BASKET:\n Goods - [{",".join(el.name for el in self.goods)}]\n Customer - [{self.customer}]\n Cost for all: {self.cost()} {self.currency} '

goods_1 = Goods("Milk", "50", "UAH", "This goods was made in Ukraine")
goods_2 = Goods("Toy", "-60", "UAH", "This goods was made in Chine")
customer_1 = Customer("Ivan", "Sotsenko", "576132897")
basket = Basket("UAH", customer_1,goods_1,goods_1,goods_1,goods_2,goods_2)

try:
    print(goods_1)
    print(goods_2)
except PriceError as error:
    print(error)

print()
print(basket)

