import turtle
import os
import math
import random

#set the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invators")
wn.screensize(200)

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

#Create the players
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#choose the number of enemies
number_of_enemies = 5
#create a empty list
enemies = []

#Add enemies to the list
# for i in range(number_of_enemies):
#     #Create enemy
#     enemies.append(turtle.Turtle())

# for enemy in enemies:    
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
x = random.randint(-200, 200)
y = random.randint(100, 250)
enemy.setposition(x, y)

enemyspeed = 2

#Create player's bullet
bullet = turtle.Turtle()
bullet.color("grey")
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 60

#Define bullet state
bulletstate = "ready"

#Move player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare the bulletstate as global if it needs to be changed
    global bulletstate

    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 30:
        return True
    else:
        return False

#Create keboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:

    # for enemy in enemies:
    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #Move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    #Checking if the bullet is collied with the enemy
    if isCollision(bullet, enemy):
        #Reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)

    #Reset the enemy
    enemy.setposition(-200, 250)
    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check if the bullet has reached the boundry
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"



delay = input("Press enter to finish.")