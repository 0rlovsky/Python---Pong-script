import turtle

# Window setup
window = turtle.Screen()
window.title("Pong By Aorlov")
window.bgcolor("black")
window.setup(width=1380, height=1080)
window.tracer(0)

# Paddle A (Player)
paddle_a = turtle.Turtle()
paddle_a.speed(1)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-650, 0)

# Paddle B (Bot)
paddle_b = turtle.Turtle()
paddle_b.speed(1)
paddle_b.shape("square")
paddle_b.color("silver")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(650, 0)

# Ball
hit_ball = turtle.Turtle()
hit_ball.speed(0.2)
hit_ball.shape("circle")
hit_ball.color("Silver")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 0.2
hit_ball.dy = -0.2

# Display the score
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 460)
pen.write("Player: {}    Bot: {}".format(score_a, score_b), align="center", font=("Courier", 36, "normal"))

# Move paddle b (bot)
def move_paddle_b():
    if hit_ball.ycor() > paddle_b.ycor():
        paddle_b.sety(paddle_b.ycor() + 10)
    elif hit_ball.ycor() < paddle_b.ycor():
        paddle_b.sety(paddle_b.ycor() - 10)

# Keyboard bindings (only for player)
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

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")

# Function to restart the game
def restart_game():
    global score_a, score_b
    score_a = 0
    score_b = 0
    pen.clear()
    pen.write("Player: {}    Bot: {}".format(score_a, score_b), align="center", font=("Courier", 36, "normal"))

# Game loop
game_over = False
while not game_over:
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
        hit_ball.goto(0, 0)
        hit_ball.dy *= 1
        score_a += 1  # Increment Player's score
        pen.clear()
        pen.write("Player: {}    Bot: {}".format(score_a, score_b), align="center", font=("Courier", 36, "normal"))
        if score_a == 5:
            pen.goto(0, 0)
            pen.write("Player Wins! Press Enter to play again", align="center", font=("Courier", 36, "normal"))
            window.listen()
            window.onkeypress(restart_game, "Return")
            while True:
                if window.listen():
                    break
            break  # Exit the game loop if player wins

    if hit_ball.xcor() < -910:
        hit_ball.goto(0, 0)
        hit_ball.dy *= 1
        score_b += 1  # Increment Bot's score
        pen.clear()
        pen.write("Player: {}    Bot: {}".format(score_a, score_b), align="center", font=("Courier", 36, "normal"))

    # Paddle ball collision for player
    if (hit_ball.xcor() < -640 and hit_ball.xcor() > -650) and (
            hit_ball.ycor() < paddle_a.ycor() + 60 and hit_ball.ycor() > paddle_a.ycor() - 60):
        hit_ball.setx(-640)
        hit_ball.dx *= -1

    # Paddle ball collision for bot
    if (hit_ball.xcor() > 640 and hit_ball.xcor() < 650) and (
            hit_ball.ycor() < paddle_b.ycor() + 60 and hit_ball.ycor() > paddle_b.ycor() - 60):
        hit_ball.setx(640)
        hit_ball.dx *= -1

    # Move paddle b (bot)
    move_paddle_b()