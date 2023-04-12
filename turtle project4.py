import turtle
t=turtle.Turtle()
list1=['red','purple','green','blue','yellow']

for i in range(200):
    t.color(list1[i%5])
    t.pensize(i/10+1)
    t.fd(i)
    t.lt(59)
    
