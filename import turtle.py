import turtle 

lucky=turtle.Turtle()

rainbow = ["red", "orange", "yellow", "green", "blue", "purple", "pimk"]

# Write whatever code you want here!
lucky.width(10)

lucky.penup()
lucky.back(30)
lucky.pendown()

for rainbow in ["red", "orange", "yellow", "green", "blue", "purple", "pink"]:
        lucky.color(rainbow)
        lucky.forward(80)
        lucky.right (50)
        lucky.penup()
        lucky.forward(80)
        lucky.right(50)
        lucky.pendown()
lucky.hideturtle()              