import module_student_person
import module_group
import module_exception

student_1 = module_student_person.Student("Ivan", "Sotsenko", "12345678", "17")
student_2 = module_student_person.Student("Ihor", "Shevchenko", "567098321", "25")
student_3 = module_student_person.Student("Vlad", "Ivanov", "456321678", "19")
student_4 = module_student_person.Student("Volodymyr", "Glushenko", "098765432", "26")
student_5 = module_student_person.Student("Volodymyr", "Zelensky", "662745987", "16")
student_6 = module_student_person.Student("Oleh", "Mudryk", "475213845", "20")

group = module_group.Group(8)
try:
    group.append_student(student_1)
    group.append_student(student_2)
    group.append_student(student_3)
    group.append_student(student_4)
    group.append_student(student_5)
    group.append_student(student_6)
except module_exception.StudentLimitError as error:
    print(error)
except ValueError as error:
    print(error)
finally:
    print(group)

print(group.find_student("Sotsenko"))
for el in group:
    print(el)

