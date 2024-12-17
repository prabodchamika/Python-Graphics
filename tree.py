import turtle as tu

roo = tu.Turtle()
Wn = tu.Screen()
Wn.bgcolor("black")
Wn.title("Advanced Fractal Tree Pattern")
roo.left(90)
roo.speed(0)

def draw_tree(length,pensize,color):
    if length <5:
        return
    roo.pensize(pensize)
    roo.pencolor(color)
    roo.forward(length)
    roo.left(30)
    draw_tree(length * 0.75, max(pensize -1, 1), "yellow")
    roo.right(60)
    draw_tree(length * 0.75, max(pensize -1, 1), "red")
    roo.left(30)
    roo.backward(length)

draw_tree(100,8, "green")

Wn.exitonclick