print("Welcome User")

name= input("Please enter your name:")
family= input("Please enter your family:")

print("Please enter your scores(0-20)")

l1= float(input()) 
l2= float(input()) 
l3= float(input()) 

if l1<0 or l2<0 or l3<0 or l1>20 or l2>20 or l3>20:

    print("Invalid input")
    
else:
    average=(l1+l2+l3)/3
    if average>=17:
        print("Great")
    elif average<17 and average>=12:
        print("Normal")
    elif average<12:
        print("Fail")
    print(name, family,", your average is:",average)