class Shape:
    def area(self):
        print("Area:", 0)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print("Area:", self.length ** 2)

shape = Shape()
shape.area()  

square = Square(5)
square.area()  
