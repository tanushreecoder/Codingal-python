import turtle    #We are importing the turtle drawing.
t = turtle.Turtle()    #We are naming.
s = turtle.Screen()    #We are giving the screen a name
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']  #The turtle will draw 6 colors in a row.

s.bgcolor('black')
t.speed('fastest')  #We put the speed
t.hideturtle()
while True: #This is put to keep drawing forever
  for x in range(200):         #x Goes from 0 to 199
   t.pencolor(colors[x%len(colors)])   #It will pick colors in the list
   t.width(x/100 + 1)       #The line gets thicker as x gets ticker
   t.forward(x)      #The turtle moves forward by x steps
   t.left(59)    #This makes the spiral twist
  t.right(239)

  for x in range(200, 0, -1):
   t.pencolor('black')
   t.width(x/100 + 7)
   t.forward(x)
   t.right(59)
    
