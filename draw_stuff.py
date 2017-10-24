from random import randint
from turtle import *
import math
i = True
pensize(5)
rt = Turtle()
again = True
screensize(1000,600)
colormode(255)
radians()


def triangle():
    for r in range(3):
        left(2 * math.pi / 3)
        col = 1
        for i in range(13):
            if col == 1:
                color(0, 0, 0)
                forward(20)
                col = -1
            else:
                penup()
                forward(20)
                pendown()
                col = 1

def square():
    for r in range(4):
        left(math.pi / 2)
        col = 1
        for i in range(13):
            if col == 1:
                color(0, 0, 0)
                forward(20)
                col = -1
            else:
                penup()
                forward(20)
                pendown()
                col = 1
                
def squigly():
    leftr = 0
    rightr = 0
    leftrrt = 0
    rightrrt = 0
    for r in range(1):
        rt.pensize(5)
        
        speed(10)
        for r in range(2):
            for i in range(10):
                lr = randint(0,1)
                
                if lr == 0:
                    for r in range(6):
                        if r >= 3:
                            leftr = leftr + .1
                            leftrrt = leftrrt + .1
                            color(randint(1,255), randint(1,255), randint(1,255))
                            left(leftr)
                            forward(5)
                            rt.left(leftrrt)
                            rt.forward(5)
                        else:
                            leftr = leftr + .1
                            leftrrt = leftrrt + .1
                            left(leftr)
                            penup()
                            forward(5)
                            pendown()
                            rt.left(leftrrt)
                            rt.penup()
                            rt.forward(5)
                            rt.pendown()

                if lr > 0:
                    for r in range(6):
                        if r >= 3:
                            rightr = rightr + .1
                            rightrrt = rightrrt + .1
                            color(randint(1,255), randint(1,255), randint(1,255))
                            right(rightr)
                            forward(5)
                            rt.right(rightrrt)
                            rt.forward(5)
                        else:
                            rightr = rightr + .1
                            rightrrt = rightrrt + .1
                            right(rightr)
                            penup()
                            forward(5)
                            pendown()
                            rt.right(rightrrt)
                            rt.penup()
                            rt.forward(5)
                            rt.pendown()
            penup()
            home()
            pendown()
            rt.penup()
            rt.home()
            rt.pendown()
        rt.clear()
        clear()

def l():
    color(0 ,0 ,0)
    left(.3)

def r():
    color(0 ,0 ,0)
    right(.3)
    
def game():
    for i in range(500):
        backward(3)
        onkeyrelease(l, "a")
        onkeyrelease(r, "d")
        listen()

def drawf():
    circ = Turtle()
    er = True
    while er == True:
        co = 0
        screen.onclick(circ.goto)
        circ.color(co, co, co)
        circ.forward(10)
        circ.left(50)
        screnn.onclick(None)
    
def timer():
    time = 0
    while time != 300:
        time = time + 1
        print(time)
    clear()
    
while again == True:
    '''
    triangle()
    timer()
    square()
    timer()
    squigly()
    timer()
    game()
    timer()
    '''
    drawf()


