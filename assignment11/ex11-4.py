n=int(input("enter number: "))

if n<=0:
    print("Invalid input")

elif n % 2 == 1:
    rug=[[0]*n for i in range(n)]
    m=n//2 #middle
    
    for i in range(m-1,-1,-1):
        for j in range(n):
            rug[i][j]=m-i
            rug[n-1-i][j]=m-i
            rug[j][i]=m-i
            rug[j][n-1-i]=m-i

    for row in rug:
        for c in row:
            print(c,end=' ')
        print()
                
elif n % 2 == 0:
    print("please insert odd number")
    