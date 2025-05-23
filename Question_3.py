import turtle

# Recursive function to draw sub-branches with thickness
def draw_branch(length, depth, left_angle, right_angle, reduction_factor):
    if depth == 0:
        return

    turtle.pensize(max(1, depth + 1))
    turtle.forward(length)

    current_pos = turtle.pos()
    current_heading = turtle.heading()

    turtle.left(left_angle)
    draw_branch(length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)

    turtle.penup()
    turtle.setpos(current_pos)
    turtle.setheading(current_heading)
    turtle.pendown()

    turtle.right(right_angle)
    draw_branch(length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)

# ===== User Input =====
left_angle = float(input("Enter left branch angle (degrees): "))
right_angle = float(input("Enter right branch angle (degrees): "))
initial_length = float(input("Enter starting branch length (pixels): "))
depth = int(input("Enter recursion depth (e.g., 5): "))
reduction_percent = float(input("Enter branch length reduction percentage (e.g., 70 for 70%): "))
reduction_factor = reduction_percent / 100

# ===== Turtle Setup =====
turtle.speed("fastest")
turtle.left(90)
turtle.penup()
turtle.goto(0, -250)
turtle.pendown()

# Draw longer trunk (brown and thick)
trunk_length = initial_length * 1.5
turtle.color("brown")
turtle.pensize(depth + 3)
turtle.forward(trunk_length)

# Move to top of trunk and draw branches
top_pos = turtle.pos()
turtle.color("green")

turtle.left(left_angle)
draw_branch(initial_length, depth - 1, left_angle, right_angle, reduction_factor)

turtle.penup()
turtle.setpos(top_pos)
turtle.setheading(90)
turtle.pendown()

turtle.right(right_angle)
draw_branch(initial_length, depth - 1, left_angle, right_angle, reduction_factor)

turtle.hideturtle()
turtle.done()
