#members: Hasan Ahmad, Souichioru Kotaki, Andrew Chung, Joseph Moyles
import turtle as t
t.speed(0)

#functions
def move(xx,yy):
    t.penup(),t.goto(xx,yy),t.pendown()

def hash_marks_x():
    t.penup()
    t.goto(-200, 0)
    for i in range(40):
        t.lt(90)
        t.pendown()
        t.fd(5)
        t.color("light grey")
        t.fd(195)
        t.bk(195)
        t.color("black")

        t.bk(10)
        t.color("light grey")
        t.bk(195)
        t.fd(195)
        t.color("black")
        t.fd(5)
        
        t.penup()
        t.rt(90)
        t.fd(10)

def hash_marks_y():
    t.penup()
    t.goto(0, 200)
    for i in range(40):
        t.pendown()
        t.fd(5)
        t.color("light grey")
        t.fd(195)
        t.bk(195)
        t.color("black")

        t.bk(10)
        t.color("light grey")
        t.bk(195)
        t.fd(195)
        t.color("black")
        t.fd(5)
        
        t.penup()
        t.rt(90)
        t.fd(10)
        t.lt(90)

#hash marks
hash_marks_x()
hash_marks_y()

#x+y axis
move(-200,0)
t.forward(400)
move(0,0)
t.left(90)
t.forward(200)
t.backward(400)
move(-200,-200)

# box coordinate plane
for i in range(4):
    t.forward(400)
    t.right(90)
    
#equation line and stamping (arrows)
equation = input("Please enter an equation in y = mx + b format: ")
slope=""
yint=""

j=0

list_of_equation=list(equation)
for n in list_of_equation:
  if(j==2):
    yint=yint+n
  elif(j==1):
    if(n=="+"):
      j+=1
    elif(n!="x" and n!="+"):
      slope=slope+n
  elif(n=="="):
    j+=1

m=int(slope)
b=int(yint)

t.penup()
t.setposition(0,b)
t.pendown()
angle = 90 - 45/m
t.setheading(angle)
t.color("red")
t.forward(200-b)
t.stamp()
t.backward(400)
t.right(180)
t.stamp()


# finish
wn = t.Screen()
wn.mainloop()