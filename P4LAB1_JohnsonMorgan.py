import turtle

# Create screen
wn = turtle.Screen()
wn.bgcolor("lightblue")  # background color

# Create turtle
house = turtle.Turtle()
house.color("purple")  # turtle color
house.pensize(3)
# Draw square
for i in range(4):
    house.forward(100)
    house.left(90)
house.left(90)
house.forward(100)
house.right(90)
# Draw triangle
count = 0
while count < 3:
    house.forward(100)
    house.left(120)
    count += 1
    house.penup()
house.goto(30, 0)
house.pendown()

for i in range(2):
    house.forward(40)
    house.left(90)
    house.forward(60)
    house.left(90)
    wn.mainloop()
