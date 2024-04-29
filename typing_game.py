from random import choice, randrange
from string import ascii_lowercase
from turtle import *
from sys import exit

from freegames import vector

targets = []
letters = []
score = 0

def inside(point):
    return -200 < point.x < 200 and -200 < point.y < 200

def draw_score(score):
    score_turtle.clear()
    score_turtle.color('grey')
    score_turtle.write(f"Score: {score}", align='center' ,font=('Consolas', 20, 'normal'))

def draw():
    clear()
    for target, letter in zip(targets, letters):
        goto(target.x, target.y)
        color('#39FF14')
        write(letter, align='center', font=('Consolas', 20, 'normal'))
    update()

def move():
    if randrange(20) == 0:
        x = randrange(-150, 150)
        target = vector(x, 200)
        targets.append(target)
        letter = choice(ascii_lowercase)
        letters.append(letter)

    for target in targets:
        target.y -= 1

    draw()
    
    for target in targets:
        if not inside(target):
            exit()

    ontimer(move, 15)

def press(key):
    global score
    if key in letters:
        score += 1
        pos = letters.index(key)
        del targets[pos]
        del letters[pos]
    else:
        score -= 1
    draw_score(score)
    print("Current Score:", score)


setup(420, 420, 370, 0)
bgcolor('black')
hideturtle()
up()
tracer(False)
listen()
score_turtle = Turtle(visible=False)
score_turtle.penup()
score_turtle.goto(0, 180)
score_turtle.pendown()
score_turtle.color('black')
score_turtle.hideturtle()

draw_score(score)
move()

for letter in ascii_lowercase:
    onkey(lambda letter=letter: press(letter), letter)

done()
