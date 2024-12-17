import turtle as tu
import random

wn = tu.Screen()
wn.bgcolor("black")  
wn.title("Frozen Snow Flower")
wn.setup(width=800, height=800) 

roo = tu.Turtle()
roo.speed(0)  
roo.pensize(2)

colors = ["#A9D8E6", "#6AC0D4", "#C1A9F7", "#D8E6F7"]  

def draw_tree(length, pensize, color):
    if length < 10:
        return
    else:
        roo.pensize(pensize)
        roo.pencolor(color)
        roo.forward(length)  
        roo.left(30)
      
        draw_tree(length * 0.7, pensize - 1, random.choice(colors))
        roo.right(60)
      
        draw_tree(length * 0.7, pensize - 1, random.choice(colors))
        roo.left(30)
        roo.backward(length) 

def draw_snow_flower(sides, length, pensize):
    for i in range(sides):
      
        color = random.choice(colors) 
        draw_tree(length, pensize, color)  
        roo.right(360 / sides)  

draw_snow_flower(12, 120, 10)  

roo.hideturtle()

wn.exitonclick()