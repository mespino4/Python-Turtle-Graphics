import turtle

colors = ["red", "orange", "yellow",
          "green", "blue", "purple"]
pen = turtle.Turtle()
pen.speed(10)
turtle.bgcolor("black")  
pen.pensize(2)

initial_size = 30  

for i in range(400):
    pen.color(colors[i % 6])
    pen.forward(initial_size + i)
    pen.left(59)

pen.hideturtle()



turtle.done()
