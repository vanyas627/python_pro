import module_exception
import logging
logging.basicConfig(filename='example.log', format='[%(asctime)s] [%(levelname)s] => %(message)s', datefmt='%Y-%m-%d %H:%M:%S',level=logging.DEBUG)

class GroupIterrator:
    def __init__(self,lis):
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

class Group:
    def __init__(self,limit):
        self.lis = []
        self.limit = limit

    def append_student(self, student):
        if len(self.lis) >= self.limit:
            raise module_exception.StudentLimitError("Limit exceeded!!")
        if student in self.lis:
            raise ValueError(f"Student: {student.name_surname()} is already in the group!")
        else:
            self.lis.append(student)
            logging.info("Added student")


    def delete_student(self, student):
        self.lis.remove(student)


    def find_student(self, surname):
        for el in self.lis:
            if el.surname == surname:
                return (el)

    def __iter__(self):
        return GroupIterrator(self.lis)

    def __str__(self):
        return f"{[el.name_surname() for el in self.lis]}"