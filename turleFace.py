import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Background color

# Create a turtle for drawing
pen = turtle.Turtle()
pen.shape("classic")
pen.color("black")
pen.speed(1)  # You can adjust the drawing speed

# Draw the face
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.begin_fill()
pen.color("yellow")  # Face color
pen.circle(100)
pen.end_fill()

# Draw the eyes
pen.penup()
pen.goto(-40, 30)
pen.pendown()
pen.begin_fill()
pen.color("purple")  # Eye color
pen.circle(20)
pen.end_fill()

pen.penup()
pen.goto(40, 30)
pen.pendown()
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# Draw the pupils
pen.penup()
pen.goto(-35, 45)
pen.pendown()
pen.begin_fill()
pen.color("black")  # Pupil color
pen.circle(10)
pen.end_fill()

pen.penup()
pen.goto(45, 45)
pen.pendown()
pen.begin_fill()
pen.color("green")  # Pupil color
pen.circle(10)
pen.end_fill()

# Draw the mouth
pen.penup()
pen.goto(20, -10)
pen.pendown()
pen.setheading(-60)
pen.pensize(2)  # Thicker line for the mouth
pen.circle(30, 120)
pen.pensize(10)  # Reset line thickness

# Add a message
pen.penup()
pen.goto(0, -150)
pen.pendown()
pen.color("black")
pen.write("Custom Smiley Face", align="center", font=("Arial", 16, "normal"))

# Close the window on click
screen.exitonclick()
