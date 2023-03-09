n=str(input("enter the name of the student"))
h=int(input("Total number of classes held"))
a=int(input("Total nymber of classes attended"))
attendance=a/h*100
print("The attendance percentage of ",n,"is ",attendance)
if(attendance>=75):
   print(n," is eligible for exam")
else:
    print(n," is not eligible")
