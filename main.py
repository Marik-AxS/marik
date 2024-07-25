
# 4 принципа ООП

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}')
    
    def heritance(self):
        print("I am a person")

# object = Person("John", 30)
# object2 = Person("Alice", 25)
# object.display_info()
# object2.display_info()

# name = "John"
# print(name.index("o"))
        
# Наследование
        
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self.grade = grade
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def heritance(self):
        print("I am a student")

    def study(self):
        print("I am studying")

# object1 = Student("Анатали", 24, 11)
# object2 = Student("Michael", 111, 14)
# object1.display_info()
# object2.display_info()
        
# Множественное наследование
        
class A:
    def method(self):
        print("Method A")

class B:
    def method(self):
        print("Method B")

class C(A, B):
    def method(self):
        print("Method C")

class D(C):
    def method(self):
        print("Method D")

# d = D()
# d.method()
# print(D.mro)
        
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some sound")
    
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
    
class Cat(Animal):
    def make_sound(self):
        print("MeoW!")

# dog = Dog("Haizenberg")
# cat = Cat("Garfild")
# cat.make_sound()
# dog.make_sound()
        

# Инкапсуляция
    
class Car:
    def __init__(self,name) -> None:
        self.name = name
    
    def prova(self):
        print('show prava')

porsche_911_gt3 = Car('german')
porsche_911_gt3.prova()