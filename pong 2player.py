import turtle
import tkinter as tk
import time 


# Window setup
window = turtle.Screen()
window.title("Pong By Aorlov")
window.bgcolor("Blue")
window.setup(width=1380, height=1080)
window.tracer(0)



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(1)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-650, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(650, 0)


# Ball
hit_ball = turtle.Turtle()
hit_ball.speed(5)
hit_ball.shape("circle")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = 5

# Display the score
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 460)
pen.write("Player One: 0    Player Two: 0", align="Center", font=("Courier", 36, "normal"))

# Create a turtle object for displaying the start message
start_message = turtle.Turtle()
start_message.speed(0)
start_message.color("red")
start_message.penup()
start_message.hideturtle()
start_message.goto(0, 0)
start_message.write("Press Enter to start the game", align="center", font=("Courier", 24, "normal"))

def start_game():
    start_message.clear()  # Clear the start message
    pen.clear()  # Clear any previous win message
    pen.write("Player One: 0    Player Two: 0", align="center", font=("Courier", 36, "normal"))
    game_loop()  # Start the game loop


# Bind the start_game function to the Enter key press event
window.onkeypress(start_game, "Return")


def paddle_a_up():
    y = paddle_a.ycor()
    if y < 470:
         y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -470:
        y -= 20
    paddle_a.sety(y)

# def paddle_a_right():
#     x = paddle_a.xcor()
#     if x < -200:
#          x += 10
#     paddle_a.sety(x)

# def paddle_a_left():
#     x = paddle_a.xcor()
#     if x > 200:
#          x -= 10
#     paddle_a.sety(x)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 470:
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -470:
        y -= 20
    paddle_b.sety(y)

#def paddle_b_left():
#   x = paddle_b.xcor()
#  if x < 650:
#      x += -20
#  paddle_b.set(x)

#def paddle_b_right():
#x = paddle_b.xcor()
#if x > 650:
#       x += -20
#    paddle_b.set(x)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
# window.onkeypress(paddle_a_right, "e")
# window.onkeypress(paddle_a_right, "q")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")
#window.onkeypress(paddle_b_right, "Right")
#window.onkeypress(paddle_b_left, "Left")
# Game loop

# Define the frame rate
FRAME_RATE = 60  # Adjust this value as needed

def game_loop():
    scoreA=0
    scoreB=0
    last_update_time = time.time()

    # Clear the start message
    start_message.clear()

    while True:
        # Calculate time since the last update
        current_time = time.time()
        elapsed_time = current_time - last_update_time

        # If less than 1/FRAME_RATE seconds have passed, wait until the next frame
        if elapsed_time < 1 / FRAME_RATE:
            time.sleep((1 / FRAME_RATE) - elapsed_time)

        last_update_time = time.time()

        window.update()

        # Move the ball
        hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
        hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

        # Checking borders top & bottom
        if hit_ball.ycor() > 470:
            hit_ball.sety(470)
            hit_ball.dy *= -1

        if hit_ball.ycor() < -470:
            hit_ball.sety(-470)
            hit_ball.dy *= -1

        # checking boarders Left and Right
        if hit_ball.xcor() > 910:
            hit_ball.goto(0,0)
            hit_ball.dy *= 1
            scoreA += 1  # Increment Player A's score
            pen.clear()
            pen.write("Player One: {}    Player Two: {}".format(scoreA, scoreB), align="center", font=("Courier", 36, "normal"))
            if scoreA == 5:
                pen.goto(0, 0)
                pen.write("Player One Wins!", align="center", font=("Courier", 36, "normal"))
                pen.penup()
                pen.hideturtle()
                pen.goto(0, 460)
                return  # Exit the game loop



        if hit_ball.xcor() < -880:
            hit_ball.goto(0,0)
            hit_ball.dy *= 1
            scoreB += 1  # Increment Player B's score
            pen.clear()
            pen.write("Player One: {}    Player Two: {}".format(scoreA, scoreB), align="center", font=("Courier", 36, "normal"))
            if scoreB == 5:
                pen.goto(0, 0)
                pen.write("Player Two Wins!", align="center", font=("Courier", 36, "normal"))
                pen.penup()
                pen.hideturtle()
                pen.goto(0, 460)
                return  # Exit the game loop

        # Paddle ball collision
        if (hit_ball.xcor() > 640 and hit_ball.xcor() < 650) and (
            hit_ball.ycor() < paddle_b.ycor() + 60 and hit_ball.ycor() > paddle_b.ycor() - 60):
            hit_ball.setx(640)
            hit_ball.dx *= -1

        if (hit_ball.xcor() < -640 and hit_ball.xcor() > -650) and (
            hit_ball.ycor() < paddle_a.ycor() + 60 and hit_ball.ycor() > paddle_a.ycor() - 60):
            hit_ball.setx(-640)
            hit_ball.dx *= -1

window.mainloop()


