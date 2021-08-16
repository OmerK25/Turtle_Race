import math
import random
import turtle
import time

win_length = 500
win_height = 500

turtles = 8

turtle.screensize(win_length, win_height)

class racer(object):
    def __init__(self, color, pos,shape='turtle'):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape(shape)
        self.turt.color("black",color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self):
        r = random.randrange(1, 20)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.turt.pendown()
        self.turt.forward(r)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)


def setupFile(name, colors):
    file = open(name, 'w')
    for color in colors:
        file.write(color + ' 0 \n')
    file.close()


def startGame():

    tList = []
    turtle.clearscreen()
    turtle.Screen().bgpic("grass.gif")
    turtle.hideturtle()
    colors = ["red", "green", "blue", 'yellow', 'pink', 'orange', 'purple', 'white', 'grey']
    start = -(win_length/2) + 20
    for t in range(turtles):
        newPosX = start + 1.05*t*(win_length)//turtles
        tList.append(racer(colors[t],(newPosX, -230)))
        tList[t].turt.showturtle()

    Explaination = racer("black", (0,320),"arrow")
    Explaination.turt.hideturtle()
    Explaination.turt.write("Pick a turtle to win the race :)", align='center',font=("Comic Sans MS", 25, "normal"))
    time.sleep(3)
    Explaination.turt.clear()
    Explaination.turt.write("Good Choice", align='center', font=("Comic Sans MS", 25, "normal"))
    time.sleep(0.7)
    Explaination.turt.clear()
    Explaination.turt.write("3", align='center', font=("Comic Sans MS", 25, "normal"))
    time.sleep(0.7)
    Explaination.turt.clear()
    Explaination.turt.write("2", align='center',font=("Comic Sans MS", 25, "normal"))
    time.sleep(0.7)
    Explaination.turt.clear()
    Explaination.turt.write("1", align='center', font=("Comic Sans MS", 25, "normal"))
    time.sleep(0.7)
    Explaination.turt.clear()
    Explaination.turt.write("GO!", align='center', font=("Comic Sans MS", 25, "normal"))
    time.sleep(0.5)
    Explaination.turt.clear()

    run = True
    while run:
        for t in tList:
            t.move()


        maxColor = []
        maxDis = 0
        for t in tList:
            if t.pos[1] > 230 and t.pos[1] > maxDis:
                maxDis = t.pos[1]
                maxColor = []
                maxColor.append(t.color)
            elif t.pos[1] > 230 and t.pos[1] == maxDis:
                maxDis = t.pos[1]
                maxColor.append(t.color)

        if len(maxColor) > 0:
            run = False
            Explaination.turt.write("The winner is: "+str(maxColor[0]), align='center', font=("Comic Sans MS", 25, "normal"))
            time.sleep(1.5)
            Explaination.turt.clear()
            Explaination.turt.write("Don't worry, next time you will win :) ", align='center', font=("Comic Sans MS", 25, "normal"))
            time.sleep(1.5)
            Explaination.turt.clear()
            
    oldScore = []
    file = open('scores.txt', 'r')
    for line in file:
        l = line.split()
        color = l[0]
        score = l[1]
        oldScore.append([color, score])

    file.close()

    file = open('scores.txt', 'w')

    for entry in oldScore:
        for winner in maxColor:
            if entry[0] == winner:
                entry[1] = int(entry[1]) + 1

        file.write(str(entry[0]) + ' ' + str(entry[1]) + '\n')


    file.close()


startGame()

while True:
    time.sleep(2)
    startGame()
