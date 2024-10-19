import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Space Avoidance Game - Avoid the Asteroids!")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Spaceship
spaceship = turtle.Turtle()
spaceship.shape("triangle")
spaceship.color("white")
spaceship.penup()
spaceship.goto(0, -250)
spaceship.setheading(90)

# Create asteroids
def create_asteroid():
    asteroid = turtle.Turtle()
    asteroid.penup()
    asteroid.color("gray")
    asteroid.goto(random.randint(-390, 390), random.randint(100, 300))
    asteroid.speed(0)
    asteroid.shape("square")
    asteroid.shapesize(stretch_wid=2, stretch_len=1)  # Rectangular shape
    return asteroid

asteroids = [create_asteroid() for _ in range(5)]

# Game Over message
game_over_turtle = turtle.Turtle()
game_over_turtle.hideturtle()
game_over_turtle.color("red")
game_over_turtle.penup()
game_over_turtle.goto(0, 0)

# Flame drawing function
def draw_flame(x, y):
    flame = turtle.Turtle()
    flame.hideturtle()
    flame.speed(0)
    flame.penup()
    flame.goto(x, y)
    
    # Draw the longer orange flame
    flame.color("orange")
    flame.setheading(270)  # Point downwards
    flame.begin_fill()
    for _ in range(2):
        flame.forward(15)  # Longer flame
        flame.right(90)
        flame.forward(5)
        flame.right(90)
    flame.end_fill()

    # Draw the shorter red flame
    flame.color("red")
    flame.goto(x, y - 15)
    flame.begin_fill()
    for _ in range(2):
        flame.forward(10)  # Shorter flame
        flame.right(90)
        flame.forward(3)
        flame.right(90)
    flame.end_fill()

# Move the spaceship
def move_left():
    x = spaceship.xcor()
    x -= 20
    if x < -390:
        x = -390
    spaceship.setx(x)

def move_right():
    x = spaceship.xcor()
    x += 20
    if x > 390:
        x = 390
    spaceship.setx(x)

# Main game loop
def game_loop():
    for asteroid in asteroids:
        y = asteroid.ycor()
        y -= random.randint(5, 10)
        asteroid.sety(y)

        # Check for collision
        if spaceship.distance(asteroid) < 20:
            game_over_turtle.write("Game Over!", align="center", font=("Arial", 24, "normal"))
            return

        # Reset asteroid if it goes off-screen
        if y < -300:
            asteroid.goto(random.randint(-390, 390), random.randint(100, 300))

    # Draw the flame under the spaceship and erase it on the next frame
    x, y = spaceship.xcor(), spaceship.ycor() - 20
    draw_flame(x, y)

    wn.ontimer(game_loop, 50)  # Increased frequency of the game loop

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Start the game
game_loop()
wn.mainloop()
