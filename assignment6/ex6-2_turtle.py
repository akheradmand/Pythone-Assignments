import turtle

turtle.bgcolor("black")

p=turtle.Pen()
p.shape("turtle")
n=3
while n<11:
    p.up()
    p.setpos(20*(n-3),0)
    p.down()
    p.pencolor("red")
    zavieh_charkhesh= 180-((n-2)*180)/n
    p.setheading(zavieh_charkhesh+(n-2)*180/n/2)
    for j in range(n):
        p.forward(50+8*(n-3)) #15
        p.left(zavieh_charkhesh)

    n+=1

turtle.done()
