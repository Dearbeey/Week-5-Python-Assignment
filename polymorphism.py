class Animal:
    def move(self):
        print("The animal is moving")

class Dog(Animal):
    def move(self):
        print("The dog is running") 

class Fish(Animal):
    def move(self):
        print("The fish is swimming")  

class Snake(Animal):
    def move(self):
        print("The snake is slithering")

animals = [Dog(), Fish(), Snake()]
for animal in animals:
    animal.move()                         