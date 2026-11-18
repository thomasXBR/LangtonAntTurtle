import turtle
from random import randint

CURSOR_SIZE = 20
GRID_STEP = 5
STEPS_PER_FRAME = 200  # Increase for faster simulation, decrease for smoother animation

# Set up the screen and disable automatic per-step redraws
screen = turtle.Screen()
screen.tracer(0)

# Set up the black trail turtle (t) on the 10x10 grid
t = turtle.Turtle('square')
t.shapesize(GRID_STEP / CURSOR_SIZE)
t.color("black", "#000000")
t.penup()
t.speed(0)

# Set up the red square turtle (pat) snapped to the same 10x10 grid
pat = turtle.Turtle('square', visible=False)
pat.shapesize(GRID_STEP / CURSOR_SIZE)
pat.color("black", "red")
pat.penup()
pat.speed(0)
pat.setposition(randint(-25, 25) * GRID_STEP, randint(-25, 25) * GRID_STEP)
pat.showturtle()

# Maps (x, y) grid coordinates -> stamp ID
filled_spots = {}

def drawPixel():
    current_pos = (round(t.xcor()), round(t.ycor()))
    
    # Toggle the current cell and turn 90 degrees based on its state
    if current_pos in filled_spots:
        t.left(90)
        t.clearstamp(filled_spots.pop(current_pos))
    else:
        t.right(90)
        filled_spots[current_pos] = t.stamp()
        
    t.forward(GRID_STEP)
    
    # Keep pat aligned directly on top of t's current cell
    pat.setposition(t.pos())

step = 0
while True:
    # "Accelerates" the simulation so you don't have to wait a lot (You're welcome)
    drawPixel()
    step += 1
    if step % STEPS_PER_FRAME == 0:
        screen.update()