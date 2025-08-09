import turtle
turtle.Screen().bgcolor("purple")
scr = turtle.Screen()
scr.setup(400, 300)
turtle.title("Welcome to the turtle in python. You will be seeing a square")
board = turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.left(90)
    i = i + 1