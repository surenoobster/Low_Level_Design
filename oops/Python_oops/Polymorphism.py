class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

shapes = [Circle(), Square()]

for shape in shapes:
    shape.draw()  # Calls respective draw() method
