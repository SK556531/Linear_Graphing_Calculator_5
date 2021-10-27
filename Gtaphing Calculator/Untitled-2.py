equation = input("Please enter an equation in y = mx + b format: ")

slope=""
yint=""

t=0

list_of_equation=list(equation)
for n in list_of_equation:
  if(t==2):
    yint=yint+n
  elif(t==1):
    if(n=="+"):
      t+=1
    elif(n!="x" and n!="+"):
      slope=slope+n
  elif(n=="="):
    t+=1
print(slope)
print(yint)

slope=int(slope)
yint=int(yint)
