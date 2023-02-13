# 1
class CountDecorator:
    def __init__(self,f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args)

@CountDecorator
def summa(a,b):
    return a + b


# 2
lis = []
def decorator(f):
    def my_function(*args,**kwargs):
        if f not in lis:
            lis.append(f)
        return f(*args)
    return my_function

@decorator
def mul(a,b):
    return a * b
@decorator
def sub(a,b):
    return a - b


# 3
def decorator(f):
    def decorator_2(self):
        tmp = f(self)
        file = open(f"{self.__class__.__name__}.txt", "w")
        file.write(tmp)
        file.close()
        return tmp
    return decorator_2

class Cat:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    @decorator
    def __str__(self):
        return f"Cat: Name - {self.name}, Age - {self.age}"



# 4
import time
def decorate_function(amount, file_name):
    def decorate_function_2(f):
        def decorate_function_123(*args,**kwargs):
            start = time.time()
            file = open(f"{file_name}.txt", "w")
            for el in range(amount):
                f(*args)
            end = time.time()
            file.write(f"{end - start}\n")
            file.close()

        return decorate_function_123
    return decorate_function_2

@decorate_function(10000,"Ivan")
def pow(a):
    return a ** 2

