class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
# Example usage
rect = Rectangle(5, 3)
print("Area:", rect.area())        
print("Perimeter:", rect.perimeter())


class Hello:
    def __init__(self,name):
        self.name = name
        print("Happy Radha-Ashthami",name)

Hello("Krishna")

class Student:
    def __init__(self,name,city,country):
        self.name=name
        self._city=city
        self.__country=country
    def show (self):
        print(f"my name is {self.name} , my city is {self._city} , my country is {self.__country}")

ankit = Student ("Aman","Mumbai","India")
# print(ankit)

print(ankit.name)
print(ankit._city)

# print(ankit.__country)

class Base:
    def __init__(self):
        self.__hidden = "I'm hidden"

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__hidden = "I'm also hidden"

b = Base()
d = Derived()

print(b._Base__hidden)  # Outputs: I'm hidden
print(d._Derived__hidden)  # Outputs: I'm also hidden



# inheritence
class Animal:
    def __init__(self,name):
        self.name=name
    def speak (self):
        print(f"{self.name} makes sound")

class dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

class cat(Animal):
    def speak(self):
        print(f"{self.name} meaow")

    


