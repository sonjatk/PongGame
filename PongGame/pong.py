import turtle

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) # doesn't update the window all the time, makes game faster

# Score
score_a = 0
score_b = 0

# Brick A
brick_a = turtle.Turtle()
brick_a.speed(0) # max animation speed
brick_a.shape("square")
brick_a.shapesize(stretch_wid=5, stretch_len=1)
brick_a.color("white")
brick_a.penup()
brick_a.goto(-350, 0)



# Brick B
brick_b = turtle.Turtle()
brick_b.speed(0) # max animation speed
brick_b.shape("square")
brick_b.shapesize(stretch_wid=5, stretch_len=1)
brick_b.color("white")
brick_b.penup()
brick_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = -0.15

# Turtle Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def brick_a_up():
    y = brick_a.ycor()
    y += 20
    brick_a.sety(y)

def brick_a_down():
    y = brick_a.ycor()
    y -= 20
    brick_a.sety(y)

def brick_b_up():
    y = brick_b.ycor()
    y += 20
    brick_b.sety(y)

def brick_b_down():
    y = brick_b.ycor()
    y -= 20
    brick_b.sety(y)

# Keyboard binding
window.listen() # listen for keyboard input
window.onkeypress(brick_a_up, "w")
window.onkeypress(brick_a_down, "s")
window.onkeypress(brick_b_up, "Up")
window.onkeypress(brick_b_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boarder check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Brick and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < brick_b.ycor() + 40 and ball.ycor() > brick_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < brick_a.ycor() + 40 and ball.ycor() > brick_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
