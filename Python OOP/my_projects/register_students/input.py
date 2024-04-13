from my_projects.register_students.register import Register

register = Register()
print(register.register_student("SchoolStudent", "HighSchool", "Kaloqn", "Marinov", 10056))
print(register.register_student("SchoolStudent", "HighSchool", "Luchezar", "Bogdanov", 10098))
print(register.register_student("UniversityStudent", "University", "Adelina", "Georgieva", 10999))
print(register.register_student("WrongType", "University", "Vasko", "Kolev", 10999))
print(register.register_student("UniversityStudent", "School", "Hristo", "Ravanov", 10090))
print(register.register_student("UniversityStudent", "University", "Beti", "Vutova", 10999))
print(register.get_info("University"))
print(register.get_info("HighSchool"))
print(register.add_courses(10999, ['Rimsko Chastno', 'Rimsko Publichno']))
print(register.add_courses(10999, ['Rimsko Chastno', 'Rimsko Publichno']))
print(register.add_class(10056, 'A'))
print(register.add_class(10056, 'A'))
print(register.add_class(10098, 'A'))
print(register.add_class(10098, 'A'))
print(register.add_class(10999, 'A'))
print(register.change_classes(10056, 'A', 'B'))
print(register.change_classes(10056, 'B', 'B'))
print(register.change_classes(10098, 'A', 'B'))
print(register.change_classes(10098, 'B', 'B'))
print(register.eject_student(10098))