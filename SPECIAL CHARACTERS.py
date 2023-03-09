s=str(input("Enter a string"))
def string_test(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0,"SPECIAL_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        elif c.match():
            d["SPECIAL_CASE"]+=1
        else:
            pass
    print("Original string : ",s)
    print("Number of upper case characters : ",d["UPPER_CASE"])
    print("Number of lower case characters : ",d["LOWER_CASE"])
string_test("college culturals @ March 7 #$!~ n $athabama@")
