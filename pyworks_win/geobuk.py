import turtle

class Geobuk(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(2, 2)

    def draw_bar(self, height, width=40):
        self.left(90)
        self.forward(height)
        self.right(90)
        self.forward(width)
        self.right(90)
        self.forward(height)
        self.left(90)

    def histogram(self, data, mag=2, x0=-200, y0=-150):
        self.penup()
        self.goto(x0, y0)
        self.pendown()
        self.begin_fill()
        for i in range(10):
            self.draw_bar(data[i] * mag)
        self.goto(x0, y0)