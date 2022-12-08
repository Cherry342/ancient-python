class Person:
    species='Homosapien'

    def Hello(self):
        print("Hello World")

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hi(self):
     print("Hi my name is" + self.name)
class Teacher(Person):
    role='teacher'
    def hi(self):
        print ("Hi my name is Mr." + self.name)
forlenza = Teacher("Forlenza", 185)
print(forlenza.role)

class Student(Person):
    role='student'
Kevaughn = Student("Kevaughn", 168)
print(Kevaughn.role)

forlenza.hi()
anna = Person("Anna", 184)
print(anna.name)
print(anna.age)
anna.hi() # -> 'Hi my name is Anna'
Kevaughn = Person("Kevaugh, 186")
print(Kevaughn.name)
print(Kevaughn.age)


