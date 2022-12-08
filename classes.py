class Person:
    species='Homosapien'

    def Hello(self):
        print("Hello World")

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hi(self):
     print("Hi my name is" + self.name)

anna = Person("Anna", 184)
print(anna.name)
print(anna.age)
anna.hi() # -> 'Hi my name is Anna'
Kevaughn = Person("Kevaugh, 186")
print(Kevaughn.name)
print(Kevaughn.age)


