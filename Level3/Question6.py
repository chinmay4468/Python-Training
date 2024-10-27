# Single inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):  
    def sound(self):
        print(f"{self.name} barks.")

class Engine:
    def start(self):
        print("Engine starts.")

class Wheels:
    def rotate(self):
        print("Wheels are rotating.")

class Car(Engine, Wheels): 
    def drive(self):
        self.start()
        self.rotate()
        print("Car is driving.")

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I am {self.name}.")

class Employee(Person):  
    def __init__(self, name, job_title):
        super().__init__(name)
        self.job_title = job_title

    def work(self):
        print(f"{self.name} works as a {self.job_title}.")

class Manager(Employee): 
    def delegate(self):
        print(f"{self.name}, the {self.job_title}, is delegating tasks.")


dog = Dog("Buddy")
dog.sound()  

car = Car()
car.drive()

manager = Manager("Alice", "Manager")
manager.introduce()   
manager.work()        
manager.delegate()    
