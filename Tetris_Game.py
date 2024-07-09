import turtle
import random

SCALE = 31

class Game:
    def __init__(self):
        self.occupied = []
        for i in range(20):
            new = []
            for j in range(10):
                new.append(False)
            self.occupied.append(new)      
                       
        turtle.setup(SCALE*12+20, SCALE*22+20)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)
        self.active = Block()
        #These three lines must always be at the BOTTOM of __init__
        turtle.ontimer(self.gameloop, 300) 
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')    
        turtle.onkeypress(self.move_down, 'Down') 
        turtle.update()
        turtle.listen()
        turtle.mainloop()
        
            
    def gameloop(self):
        if self.active.valid(0, -1, self.occupied) is False:
            for i in self.active.squares:
                self.occupied[i.ycor()][i.xcor()] = True
            new_block = Block()
            self.active = new_block
        else:
            self.active.move(0,-1)
        turtle.update()
        turtle.ontimer(self.gameloop, 300)
            
            
                             
    def move_left(self):
        if self.active.valid(-1,0, self.occupied):
            self.active.move(-1, 0)
            turtle.update()
    def move_right(self):
        if self.active.valid(1,0, self.occupied):
            self.active.move(1, 0)
            turtle.update()
    def move_down(self):        
        if self.active.valid(0,-1, self.occupied):
            self.active.move(0, -1)
            turtle.update()
       
            
        


class Square(turtle.Turtle):
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.shapesize(SCALE/20)
        self.speed(0)
        self.fillcolor(color)
        self.pencolor('gray')
        self.penup()
        self.goto(x,y)


               

class Block:
    def __init__(self):
        
        rblock = random.randint(1, 7)
        
        if rblock == 1:       
            self.squares = []
            self.squares.append(Square(3, 18, 'cyan'))
            self.squares.append(Square(4, 18, 'cyan'))
            self.squares.append(Square(5, 18, 'cyan'))
            self.squares.append(Square(6, 18, 'cyan'))
        elif rblock == 2:       
            self.squares = []
            self.squares.append(Square(4, 19, 'blue'))
            self.squares.append(Square(4, 18, 'blue'))
            self.squares.append(Square(5, 18, 'blue'))
            self.squares.append(Square(6, 18, 'blue'))
        elif rblock == 3:       
            self.squares = []
            self.squares.append(Square(3, 18, 'orange'))
            self.squares.append(Square(4, 18, 'orange'))
            self.squares.append(Square(5, 18, 'orange'))
            self.squares.append(Square(5, 19, 'orange'))
        elif rblock == 4:     
            self.squares = []
            self.squares.append(Square(4, 19, 'yellow'))
            self.squares.append(Square(4, 20, 'yellow'))
            self.squares.append(Square(5, 20, 'yellow'))
            self.squares.append(Square(5, 19, 'yellow'))
        elif rblock == 5: 
            self.squares = []
            self.squares.append(Square(3, 18, 'green'))
            self.squares.append(Square(4, 18, 'green'))
            self.squares.append(Square(4, 19, 'green'))
            self.squares.append(Square(5, 19, 'green'))
        elif rblock == 6: 
            self.squares = []
            self.squares.append(Square(4, 19, 'purple'))
            self.squares.append(Square(5, 19, 'purple'))
            self.squares.append(Square(5, 20, 'purple'))
            self.squares.append(Square(6, 19, 'purple'))
        elif rblock == 7: 
            self.squares = []
            self.squares.append(Square(3, 19, 'red'))
            self.squares.append(Square(4, 18, 'red'))
            self.squares.append(Square(4, 19, 'red'))
            self.squares.append(Square(5, 18, 'red'))
      
                        
    def move(self, dx, dy):
       for i in self.squares:
            x = i.xcor() + dx
            y = i.ycor() + dy
            i.goto(x, y)
    def valid(self, dx, dy, occupied):
        for i in self.squares:
            x = i.xcor() + dx
            y = i.ycor() + dy
            if x < 0 or x > 9 or y < 0:
                return False
            if occupied[y][x] is True:
                return False
        return True
            
    
    
    
if __name__ == '__main__':
    Game()    
    

    
    
           
           
