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
        y = self.ycor() + 20
        if y >= 560:
            y=-560
        self.sety(y)
        print("up"+str(y))
    def movedown(self):
        y= self.ycor() - 20
        if y <= -560:
            y=560
        self.sety(y)
        print("down"+str(y))



    
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
        
class Ball(t.Turtle):
    def __init__(self, position, vector, sped):
        super().__init__()
        self.x, self.y = position
        self.vx, self.vy = vector
        self.sped = sped
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed(0)
        self.penup()
        self.goto(self.x, self.y)
        
    def update(self):
        y= self.ycor() + self.vy*self.sped
        self.sety(y)
        x= self.xcor() + self.vx*self.sped
        self.sety(x)


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
        bol = Ball((0,0),(10,10),1)
        sc.onkeypress(ping.moveup, "Up")
        sc.onkeypress(ping.movedown, "Down")
        #sc.onkeypress(ping.bettermoveup(), "Left")
        #t.onkeypress(ping.bettermovedown(), "Right")
        sc.onkeypress(pogn.movedown, "s")
        sc.onkeypress(pogn.moveup, "w")
        bol.update()
        #sc.onkeypress(pogn.bettermoveup(), "a")
        #sc.onkeypress(pogn.bettermovedown(), "d")
        t.listen()

        t.done()

if __name__ == "__main__":
    game = Pong(400, 400, "tutel", "green")
    game.run()


