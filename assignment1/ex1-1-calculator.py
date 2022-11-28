import math

print("welcome to my calculator")

print("+ : sum")
print("- : sub")
print("* : mul")
print("/ : div")

print("factorial:!")
print("sqrt")
print("log")

print("sin")
print("cos")
print("tan")
print("cot")

print("please enter your choice:")
op=input()

if op == "+" or op=="-" or op=="*" or op=="/":
    a=float(input("enter first number:"))
    b=float(input("enter second number:"))
    
elif op=="!":
    a=int(input("enter a number:"))

else:
    a=float(input("enter a number:"))


if op=="+":
    result=a+b

elif op=="-":
    result=a-b

elif op=="*":
    result= a*b

elif op=="/":
    if b==0:
        result="Cannot devide by zero"
    else:
        result=a/b

elif op=="sin":
    result=math.sin(a/180*math.pi)

elif op=="cos":
    result=math.cos(a/180*math.pi)

elif op=="tan":
    if a==90 or a==270:
        result="invalid input"
    else:
        result=math.tan(a/180*math.pi)

elif op=="cot":
    if a==0 or a==180:
        result="invalid input"
    else:
        result=math.cos(a/180*math.pi)/math.sin(a/180*math.pi)

elif op=="log":
    result=math.log(a)

elif op=="!":
    if a>0 and a % 1==0:
        result=math.factorial(a)
    else:
        result="invalid input"

elif op=="sqrt":
    if a>=0:
        result=math.sqrt(a)
    else:
        result="invalid input"

print(result)