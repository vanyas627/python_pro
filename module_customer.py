class Customer:
    def __init__(self,name, surname, phone_number ):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"Name: {self.name}; Surname: {self.surname}; Phone number: {self.phone_number}"