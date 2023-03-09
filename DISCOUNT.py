n=int(input("Enter the total number of items purchased "))
total=n*100
print("The total cost of the purchase ",total)
if(total>=1000):
    ntotal=total-(total*10/100)
    print("The new price after the discount is ",ntotal)
else:
    print("No discount")
