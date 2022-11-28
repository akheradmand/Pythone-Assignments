
n=int(input("please enter number of Fibonacci series:"))

f=[1]

if n==1:
    print(f)
    
elif n==2:
    f.append(1)
    print(f)
    
elif n>2:
    f.append(1)
    for i in range(2,n):
        fi=f[i-1]+f[i-2]
        f.append(fi)
    
    print(f)

elif n<=0:
    print("Invalid input")