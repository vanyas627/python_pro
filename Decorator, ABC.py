# 1
lis = []
def decorator(cls):
    def add_cls(*args, **kwargs):
        if cls not in lis:
            lis.append(cls)
        return cls(*args,**kwargs)
    return add_cls

# 2
class Decorator:
    def __init__(self, strng):
        self.strng = strng

    def __call__(self, cls):
        def str(*args,**kwargs):
            return f"{self.strng} {cls(*args,**kwargs)}"
        return str

# 3
class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    @staticmethod
    def summa(box1,box2):
        return box1.volume() + box2.volume()


    def __str__(self):
        return  f"Box - [x - {self.x}, y - {self.y}, z - {self.z}]"

box1 = Box(4,2,6)
box2 = Box(5,3,4)

# 4
class MyDescriptor:
    def __init__(self,strng):
        self.strng = strng

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        raise AttributeError()

    def __delete__(self, instance):
        raise AttributeError()


class Dog2:
    def __init__(self, name, age, color):

        self.__name = name
        self.__age = age
        self.__color = color
    name = MyDescriptor("name")
    age = MyDescriptor("age")
    color = MyDescriptor("color")

    def __str__(self):
        return f"Dog: Name - {self.name}, Age - {self.age}, Color - {self.color}"

# 5
class Desritpion:
    def __init__(self, name):
        self.name = name


    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError
        else:
            instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError()

# 6
from datetime import datetime

class Dog:
    file_name = "Ivan"

    def __init__(self, name, age, color, file_name):
        self.name = name
        self.age = age
        self.color = color


    def __getattr__(self, item):
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            return None

    def __setattr__(self, key, value):
        start = datetime.now().time()
        self.__dict__[key] = value
        file = open(f"{self.file_name}.txt", "a")
        file.write(f"{start}: {key} - {value}\n")
        file.close()

    def __str__(self):
        return f"Dog: Name - {self.name}, Age - {self.age}, Color - {self.color}"

# 7
import abc
class Abstraction(abc.ABC):
    @abc.abstractmethod
    def simple_number(self, num):
        if not isinstance(num, int):
            return False
        for i in range(2, num):
            if not num % i:
                return False
        return True

