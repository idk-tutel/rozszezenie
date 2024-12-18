import turtle as t

class paddle():
    def __init__(self, position, paddle):
        self.x, self.y = position
        paddle = t.Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.speed(0)
        paddle.penup()
        paddle.goto(self.x, self.y)

    def moveup(self):
        pass
    def moveup(self):
        pass
        
class ball():
    pass
class pong():
    def __init__(self, height, wight, title, bgcolor):
        self.height = height
        self.wight = wight
        self.title = title
        self.bgcolor = bgcolor
        

    def run(self):
        sc = t.Screen()
        sc.setup(wight=self.wight,height=self.height)
        sc.bgcolor(self.bgcolor)
        sc.title(self.title)
        paddle.left = paddle((350, 0))

if __name__ == "pong":
    game = pong(400, 400, "tutel", "green")