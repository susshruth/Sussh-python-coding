import os
import random

import turtle
turtle.title("Space Wars")
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)

class Sprite(turtle.Turtle):
*tab*def __init__(self, spriteshape, color, startx, starty):
*tab**tab*turtle.Turtle.__init__(self, shape = spriteshape)
*tab**tab*self.speed(0)
*tab**tab*self.penup()
*tab**tab*self.color(color)
*tab**tab*self.fd(0)
*tab**tab*self.goto(startx, starty)
*tab**tab*self.speed = 1

*tab*def move(self):
*tab**tab*self.fd(self.speed)
*tab**tab*if self. xcor() > 290:
*tab**tab**tab*self.setx(290)
*tab**tab**tab*self.rt(60)

*tab**tab*if self. xcor() < -290:
*tab**tab**tab*self.setx(-290)
*tab**tab**tab*self.rt(60)
            
*tab**tab*if self. ycor() > 290:
*tab**tab**tab*self.sety(290)
*tab**tab**tab*self.rt(60)

*tab**tab*if self. ycor() < -290:
*tab**tab**tab*self.sety(-290)
*tab**tab**tab*self.rt(60)

class Player(Sprite):
*tab*def __init__(self, spriteshape, color, startx, starty):
*tab**tab*Sprite.__init__(self, spriteshape, color, startx, starty)
*tab**tab*self.speed = 4
*tab**tab*self.lives = 3

*tab*def turn_left(self):
*tab**tab*self.lt(45)
    
*tab*def turn_right(self):
*tab**tab*self.rt(45)

*tab*def accelerate(self):
*tab**tab*self.speed += 1

*tab*def decelerate(self):
*tab**tab*self.speed -= 1

class Game():
*tab*def __init__(self):
*tab**tab*self.level = 1
*tab**tab*self.score = 0
*tab**tab*self.state = "playing"
*tab**tab*self.pen = turtle.Turtle()
*tab**tab*self.lives = 3
    
*tab*def draw_border(self):
*tab**tab*self.pen.speed(0)
*tab**tab*self.pen.color("white")
*tab**tab*self.pen.width(3)
*tab**tab*self.pen.penup()
*tab**tab*self.pen.goto(-300, 300)
*tab**tab*self.pen.pendown()
*tab**tab*for side in range(4):
*tab**tab**tab*self.pen.fd(600)
*tab**tab**tab*self.pen.rt(90)
*tab**tab*self.pen.penup()
*tab**tab*self.pen.ht()

game = Game()
game.draw_border()    

player = Player("triangle", "white", 0, 0)
# blue = Sprite("square", "blue", 0, 0)
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()

while True:
*tab*player.move()

delay = input("Press enter to finish. > ")