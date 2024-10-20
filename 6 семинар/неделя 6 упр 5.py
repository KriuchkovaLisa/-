from random import *
from tkinter import *
from tkinter import ttk
import numpy as np



WIDTH = 1000
HEIGHT = 800
a, b, c =np.random.choice(range(256), size=3)
collor_ball = '#%02x%02x%02x' % (a, b, c)

class Balls:
    def __init__(self):
        self.R = randint(10, 50) 
        self.x = randint(self.R, WIDTH - self.R) 
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (30, 30) 
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill= "green") 

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0: 
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0: 
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)



class Ball:
    def __init__(self, x, y):
        self.R = randint(10, 50) 
        self.x = x 
        self.y = y
        a, b, c = np.random.choice(range(256), size=3)
        collor_ball = '#%02x%02x%02x' % (a, b, c)
        self.collor = collor_ball
        self.dx, self.dy = (30, 30) 
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill=self.collor) 

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0: 
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0: 
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)



def click_creature(event):
    main_ball = Ball(event.x, event.y)
    main_ball.move()
    main_ball.show()
def tick():
    for ball in balls:
        ball.move()
        ball.show()
    for ball in new_balls:
        ball.move()
        ball.show()
    root.after(50, tick)

def click_creature(event):
    main_ball = Ball(event.x, event.y)
    new_balls.append(main_ball)
    print('x=', event.x, 'y=', event.y)





root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(width=1000, height=800, bg='white')
canvas.pack()

canvas.bind('<Button-1>', click_creature)

balls = [Balls() for i in range(5)]
new_balls = []

tick()
root.mainloop()