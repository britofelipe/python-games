# Simple Pong
# By Felipe Brito, based on @TokyoEdTech version
# felipeabrito.com

import turtle

wn = turtle.Screen()
wn.title("Pong by Felipe Brito")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # You don't have to update the page

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() # O T maísculo é para o nome da classe
paddle_a.speed(0) # the speed of animation
paddle_a.shape("square") # by default, its 20px by 20x
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # turtles, by definition, draw lines. With this command, they don't
paddle_a.goto(-350, 0 )

# Paddle B
paddle_b = turtle.Turtle() 
paddle_b.speed(0) 
paddle_b.shape("square") 
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() 
paddle_b.goto(350, 0 )

# Ball
ball = turtle.Turtle() 
ball.speed(0) 
ball.shape("square") 
ball.color("white")
ball.penup() 
ball.goto(0, 0 )
ball.dx = 0.25 # everytime it moves, it moves by 2px
ball.dy = 0.25
ball.dx_default = ball.dx
ball.dy_default = ball.dy

# Pengray
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor() # it returns the Y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() # it returns the Y coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # it returns the Y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # it returns the Y coordinate
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w") # When the user press "w", call the function
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = -ball.dx_default
        ball.dy = ball.dy_default
        score_a += 1
        pen.clear()
        pen.write("Player 1: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = ball.dx_default
        ball.dy = ball.dy_default
        score_b += 1
        pen.clear()
        pen.write("Player 1: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.03
        ball.dy *= 1.03
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.03
        ball.dy *= 1.03
        