import math
class Rectangle:
    def __init__(self, length, widht):
        self.length = length
        self.widht = widht

    def get_area(self):
        return self.length * self.widht

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __add__(self, other):
        return Rectangle(self.length + other.length, self.widht + other.widht)

    def __mul__(self, other):
        return self.get_area() * other

    def __str__(self):
        return f"Length: {self.length}\nWidht: {self.widht}\n Area: {self.get_area()}"

class Rational:
    def __init__(self,num,den):
        if den == 0:
            raise ValueError("Denominator can't be a zero")
        self.num = num
        self.den = den

    def __gt__(self, other):
        return self.num / self.den > other.num / other.den

    def __eq__(self, other):
        return self.num / self.den == other.num / other.den

    def __lt__(self, other):
        return self.num / self.den < other.num / other.den

    def __add__(self, other):
        return Rational((self.num * (math.lcm(self.den,other.den) // self.den)) + (other.num * (math.lcm(self.den,other.den) // other.den)),math.lcm(self.den,other.den))

    def __mul__(self, other):
        return Rational(self.num * other.num, self.den * other.den)

    def __sub__(self, other):
        return Rational((self.num * (math.lcm(self.den,other.den) // self.den)) - (other.num * (math.lcm(self.den,other.den) // other.den)),math.lcm(self.den,other.den))

    def __str__(self):
        if self.den > 0 and self.num < 0:
            if self.num < self.den and self.num % self.den:
                return f"{int(self.num / self.den)} {self.num - (self.den * int(self.num / self.den))}/{self.den}"
            if not self.num % self.den:
                return f"{self.num // self.den}"
            if math.gcd(self.num, self. den) > 1:
                return f"{self.num // math.gcd(self.num, self. den)} / {self.den // math.gcd(self.num, self. den)}"
            else:
                return f"{self.num}/{self.den}"
        if self.den < 0 and self.num > 0:
            if self.num > self.den and self.num % self.den:
                return f"{int(self.num / self.den)} {self.num - (self.den * int(self.num / self.den))}/{self.den}"
            if not self.num % self.den:
                return f"{self.num // self.den}"
            if math.gcd(self.num, self. den) > 1:
                return f"{self.num // math.gcd(self.num, self. den)} / {self.den // math.gcd(self.num, self. den)}"
            else:
                return f"{self.num}/{self.den}"
        if self.num < 0 and self.den < 0:
            if self.num < self.den and self.num % self.den:
                return f"{self.num // self.den} {self.num - (self.den * (self.num // self.den))}/{self.den}"
            if not self.num % self.den:
                return f"{self.num // self.den}"
            if math.gcd(self.num, self. den) > 1:
                return f"{self.num // math.gcd(self.num, self. den)} / {self.den // math.gcd(self.num, self. den)}"
            else:
                return f"{self.num}/{self.den}"
        else:
            if self.num > self.den and self.num % self.den:
                return f"{self.num // self.den} {self.num - (self.den * (self.num // self.den))}/{self.den}"
            if not self.num % self.den:
                return f"{self.num // self.den}"
            if math.gcd(self.num, self. den) > 1:
                return f"{self.num // math.gcd(self.num, self. den)} / {self.den // math.gcd(self.num, self. den)}"
            else:
                return f"{self.num}/{self.den}"


rectangle_1 = Rectangle(5,8)
rectangle_2 = Rectangle(4,9)
print(rectangle_1 > rectangle_2)
print(rectangle_1 + rectangle_2)
print(rectangle_2 * 3)
print()
print()


number_1 = Rational(9,-1)
number_2 = Rational(8,-8)
print(number_1 > number_2)
print(number_2)
print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)


