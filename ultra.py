import turtle as tu
import math

wn = tu.Screen()
wn.bgcolor("black")
wn.title("Ultra")
wn.setup(width=800, height=800)

spiral = tu.Turtle()
spiral.speed(0)
spiral.width(2)
spiral.hideturtle()

def draw_advanced_spiral():
    angle = 121       
    max_turns = 300   
    max_width = 5     
    hue_shift = 0    
    for i in range(max_turns):
        
        red = (math.sin(i / 50 + hue_shift) + 1) / 2
        green = (math.sin(i / 60 + hue_shift) + 1) / 2
        blue = (math.cos(i / 70 + hue_shift) + 1) / 2
        spiral.pencolor(red, green, blue)  
        distance = i * 2 + math.sin(i / 20) * 10  
        spiral.forward(distance)
        spiral.right(angle + math.sin(i / 100) * 5)  
        spiral.left(2)  
        spiral.width((i / 100) % max_width + 1)
        spiral.speed(0.1 + (i / 3000))  
        hue_shift += 0.01

draw_advanced_spiral()

wn.exitonclick()
