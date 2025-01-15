import turtle as t
on=True
class Paddle(t.Turtle):
    def __init__(self, position):
        super().__init__()
        self.a = 0
        self.x, self.y = position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed(0)
        self.penup()
        self.goto(self.x, self.y)
        

    def moveup(self):
        y = t.ycor()+20
        self.sety(y)
        print("up")
    def movedown(self):
        y=t.ycor() - 20
        self.sety(y)
        print("down")



    
    #def bettermoveup(self):
    #    self.a += 20
    #    self.sety(self.a)
    #    self.penup()
    #    self.goto(self.x, self.y)
    #def bettermovedown(self):
    #    self.a -= 20
    #    self.sety(self.a)
    #    self.penup()
    #    self.goto(self.x, self.y)
        
class Ball():
    pass

class Pong():
    def __init__(self, height, width, title, bgcolor):
        self.height = height
        self.width = width
        self.title = title
        self.bgcolor = bgcolor
        
        

    def run(self):
        sc = t.Screen()
        sc.setup(width=self.width,height=self.height)
        sc.bgcolor(self.bgcolor)
        sc.title(self.title)
        ping = Paddle((-400, 0))
        pogn = Paddle((400, 0))
        sc.listen()
        sc.onkeypress(ping.moveup(), "Up")
        sc.onkeypress(ping.movedown(), "Down")
        #sc.onkeypress(ping.bettermoveup(), "Left")
        #sc.onkeypress(ping.bettermovedown(), "Right")
        sc.onkeypress(pogn.moveup(), "w")
        sc.onkeypress(pogn.movedown(), "s")
        #sc.onkeypress(pogn.bettermoveup(), "a")
        #sc.onkeypress(pogn.bettermovedown(), "d")

        t.done()

if __name__ == "__main__":
    game = Pong(400, 400, "tutel", "green")
    game.run()


