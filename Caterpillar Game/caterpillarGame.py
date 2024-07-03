import turtle as tu
import random as rd

tu.bgcolor('yellow')

caterpillar = tu.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = tu.Turtle()
leafShape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
tu.register_shape('leaf',leafShape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

gameStarted = False
text = tu.Turtle()
text.write('Press SPACE to start',align='center',font=('Arial',16,'bold'))
text.hideturtle()

score = tu.Turtle()
score.hideturtle()
score.speed(0)

def outside_window():
    leftWall = -tu.window_width()/2
    rightWall = tu.window_width()/2
    topWall = tu.window_height()/2
    bottomWall = -tu.window_height()/2
    (x,y) = caterpillar.pos()
    isOut = x < leftWall or  x > rightWall or  y < bottomWall or y > topWall
    return isOut

def gameOver():
    caterpillar.color('yellow')
    leaf.color('yellow')
    tu.penup()
    tu.hideturtle()
    tu.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

def displayScore(currentScore):
    score.clear()
    score.penup()
    x = (tu.window_width() / 2)-50
    y = (tu.window_height() / 2)-50
    score.setpos(x,y)
    score.write(str(currentScore) , align = 'right',font=('Arial',40,'bold'))

def placeLeaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def startGame():
    global gameStarted
    if gameStarted:
        return
    gameStarted = True

    score = 0
    text.clear()

    caterpillarSpeed = 2
    caterpillarLength = 3
    caterpillar.shapesize(1,caterpillarLength,1)
    caterpillar.showturtle()
    displayScore(score)
    placeLeaf()

    while True:
        caterpillar.forward(caterpillarSpeed)
        if caterpillar.distance(leaf)<20:
            placeLeaf()
            caterpillarLength = caterpillarLength + 0.25
            caterpillar.shapesize(1,caterpillarLength,1)
            caterpillarSpeed = caterpillarSpeed + 0.25
            score = score + 10
            displayScore(score)
        if outside_window():
            gameOver()
            break

def moveUp():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def moveDown():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def moveLeft():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def moveRight():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

tu.onkey(startGame,'space')
tu.onkey(moveUp,'Up')
tu.onkey(moveRight,'Right')
tu.onkey(moveDown,'Down')
tu.onkey(moveLeft,'Left')
tu.listen()
tu.mainloop()