from turtle import *
shape("arrow")
#we want to paint house 

#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square 

#drawing a door

forward(70)
color("pink")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#first window 
color("light blue")
penup()
goto(65, 140)
pendown()
begin_fill()
right(60)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

#second window
penup()
goto(140, 140)
right(180)
pendown()
begin_fill()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
penup()
goto(0, 0)
end_fill()

forward(200)
left(90)
right(180)
forward(200)
left(50)
left(50)
right(10)

#we want to paint another house 

#step 1: draw a square 
width(7)
color(puprle)
left(90)
left(90)


exitonclick()










exitonclick()