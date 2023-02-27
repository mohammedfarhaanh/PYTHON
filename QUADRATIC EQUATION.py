import math
a=int(input("Enter coefficient of x^2:"))
b=int(input("Enter coefficient of x:"))
c=int(input("Enter constant of x:"))
d=b*b-4*a*c
if d>0:
    r1=(-b+sqrt(d))/(2*a)
    r2=(-b-sqrt(d))/(2*a)
    print("Roots are ",r1,r2)
elif (d==0):
    r1=r2=-b/(2*a)
    print("Roots are ",r1,r2)
else:
    r1=-b/(2*a)
    r2=sqrt(-d)/(2*a)
    print("Roots are ",r1,r2)
    
