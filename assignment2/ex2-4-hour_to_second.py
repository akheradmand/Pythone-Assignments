print('Welcome User')
print("This program help you to convert time's input to Second")

hr=int(input("please enter hour:"))
m=int(input("please enter minutes:"))
s=int(input("please enter seconds:"))

if hr<0 or m<0 or s<0:
    print("Invalid input")
else:
    sec=hr*3600 + m*60 + s
    print(hr,":",m,":",s," = ",sec, "seconds")