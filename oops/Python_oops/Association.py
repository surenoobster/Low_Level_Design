class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name

    def associate_with(self, teacher ,name):
        print(f"{self.name} is learning from {teacher.name}")

t1 = Teacher("Dr. Smith")
s1 = Student("Alice")

s1.associate_with(t1 ,s1)

#Or

class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name

    def associate_with(self, teacher):
        print(f"{self.name} is learning from {teacher.name}")

t1 = Teacher("Dr. Smith")
s1 = Student("Alice")

s1.associate_with(t1)

