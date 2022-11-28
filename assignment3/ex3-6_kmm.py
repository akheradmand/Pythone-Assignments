print("This program calculates the least common multiple of two numbers")

number1=int(input("please enter number1: "))
number2=int(input("please enter number2: "))

for i in range(min(number1,number2),0,-1):

    if (number1 % i ==0) and (number2 % i == 0):
        bmm=i
        kmm=number1*number2/bmm
        print("K.M.M = ", kmm)
        break