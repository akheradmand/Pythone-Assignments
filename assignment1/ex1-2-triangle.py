a1=float(input("enter first number:"))
a2=float(input("enter second number:"))
a3=float(input("enter third number:"))

if a1<=0 or a2<=0 or a3<=0:
    print("invalid input")
else:
    
    if a1+a2>a3 and a1+a3>a2 and a2+a3>a1:
        print("Congratulations; it's possible to draw a triangle with this dimensions")
    else:
        print("It's not possible to draw a triangle with this dimensions")