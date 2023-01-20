import logging
logging.basicConfig(filename='example.log', format='[%(asctime)s] [%(levelname)s] => %(message)s', datefmt='%Y-%m-%d %H:%M:%S',level=logging.DEBUG)



class StudentLimitError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return f"{self.msg}"


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


class Group:
    def __init__(self):
        self.lis = []

    def append_student(self, student, limit):
        if student not in self.lis and len(self.lis) <= limit:
            self.lis.append(student)
            logging.info("Added student")
        else:
            raise StudentLimitError("Limit exceeded or the student is already in the group!")


    def delete_student(self, student):
        self.lis.remove(student)


    def find_student(self, surname):
        for el in self.lis:
            if el.surname == surname:
                return (el)

    def __str__(self):
        return f"{[el.name_surname() for el in self.lis]}"


student_1 = Student("Ivan", "Sotsenko", "12345678", "17")
student_2 = Student("Ihor", "Shevchenko", "567098321", "25")
student_3 = Student("Vlad", "Ivanov", "456321678", "19")
student_4 = Student("Volodymyr", "Glushenko", "098765432", "26")
student_5 = Student("Volodymyr", "Zelensky", "662745987", "16")
student_6 = Student("Oleh", "Mudryk", "475213845", "20")

group = Group()
try:
    group.append_student(student_1,10)
    group.append_student(student_2,10)
    group.append_student(student_3,10)

    group.append_student(student_4,10)
    group.append_student(student_5,10)
    group.append_student(student_6,10)
except StudentLimitError as error:
    print(error)

finally:
    print(group)

print(group.find_student("Sotsenko"))