from turtle import Turtle, Screen
import time
import random
import turtle

turtle.colormode(255)
screen = Screen()
screen.bgcolor("green")
screen.title("Hra Had")
screen.setup(width=600,height=600)
screen.tracer(False)

# Proměnné
score = 0
highest_score = 0

#Hadí hlava

head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Myš

mouse = Turtle("circle")
mouse.color("grey")
mouse.penup()
mouse.goto(100,100)


score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("red")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write("Skóre:0 Nejvyšší Skóre: 0", align= "center", font=("Arial", 18))

# tělo 

body_parts = []

#Funkce

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    barva = (r, g, b)
    return barva 

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+ 20) 

    if head.direction == "left":
        x = head.xcor()
        head.setx( x -20)

def move_up():
    if head.direction  != "down":
        head.direction =  "up"

def move_down():
    if head.direction  != "up":
        head.direction = "down"

def move_right():
    if head.direction  != "left":
        head.direction = "right"

def move_left():
    if head.direction  != "right":
         head.direction = "left"

#Kliknutí na klávesy

screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")

#hlavní cyklus

while True:
    screen.update()
        
    #Kontrola kolize s hranou obrazovky
    if head.xcor() >290 or head.xcor() < -290 or head.ycor() >290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"

        #Skryjeme části těla
        for one_body_part in body_parts:
            one_body_part.goto(1500,1500)

        # Vyprázdíme list s částmi těla 
        body_parts.clear()

        #resetování score
        score= 0

        score_sign.clear()
        score_sign.write(f"Skóre:{score} Nejvyšší Skóre: {highest_score}", align= "center", font=("Arial", 18))

    # Kolize hlavy s myší 
    if head.distance(mouse) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        mouse.goto(x, y)
    
    #přidání části těla
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("white")
        new_body_part.penup()
        body_parts.append(new_body_part)

        score += 1

        if score % 2== 0:
            screen.bgcolor(random_color())
            mouse.color(random_color())

        if score > highest_score:
            highest_score = score
        score_sign.clear()
        score_sign.write(f"Skóre:{score} Nejvyšší Skóre: {highest_score}", align= "center", font=("Arial", 18))

    for index in range(len(body_parts)-1,0,-1):
        x = body_parts[index-1].xcor()
        y = body_parts[index-1].ycor()
        body_parts[index].goto(x,y)


    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)
    
    move()

    # Hlava narazila do těla
    for one_body_part in body_parts:
        if one_body_part.distance(head)<20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"

             #Skryjeme části těla
            for one_body_part in body_parts:
                one_body_part.goto(1500,1500)
                # Vyprázdíme list s částmi těla 
                body_parts.clear()
            
            #Resetování score

            score= 0

            score_sign.clear()
            score_sign.write(f"Skóre:{score} Nejvyšší Skóre: {highest_score}", align= "center", font=("Arial", 18))

        # Rychlost hry
    if score <= 15:
        time.sleep(0.2)
    elif score >= 16 and score <= 30:
        time.sleep(0.18)
    elif score >= 31 and score <= 45:
        time.sleep(0.15)
    elif score >= 46 and score <= 65:
        time.sleep(0.13)
    elif score >= 66 and score <= 80:
        time.sleep(0.1)
    elif score>= 81 and score <= 100:
        time.sleep(0.09)
    elif score >= 101 and score <= 130:
        time.sleep(0.06)
    elif score >= 131 and score <= 160:
        time.sleep(0.05)
    elif score >=161:
        time.sleep(0.04)


screen.exitonclick()