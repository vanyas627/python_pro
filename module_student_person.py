class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Name: {self.name}; Surname: {self.surname}"

class Student(Person):
    def __init__(self,name, surname, phone, age):
        super().__init__(name, surname)
        self.phone = phone
        self.age = age

    def __str__(self):
        return f"{super().__str__()}; Phone:{self.phone}; Age: {self.age}."

    def name_surname(self):
        return f"{self.surname} {self.name}"