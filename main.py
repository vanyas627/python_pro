import module_basket
import module_customer
import module_goods
import module_exception
try:
    goods_1 = module_goods.Goods("Milk", "250", "UAH", "This goods was made in Ukraine")
    goods_2 = module_goods.Goods("Toy", "30", "UAH", "This goods was made in Chine")
except module_exception.PriceError as error:
    print(error)
customer_1 = module_customer.Customer("Ivan", "Sotsenko", "576132897")
try:
    basket = module_basket.Basket("UAH", customer_1,goods_1,goods_1,goods_1,goods_2,goods_2)
    print(goods_1)
    print(goods_2)
    print()
    print(basket)
except NameError:
    print("You entered the wrong price. Try again!")





