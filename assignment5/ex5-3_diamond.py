n= int(input("enter number of rows: "))

def diamond(n):

    diamond=[]

    for i in range(0,2*n-1):
        row=[]
        for j in range(0,2*n-1):
            row.append(" ")

        diamond.append(row)

    for i in range(0,n):
        for j in range(n-i-1,n+i):
            diamond[i][j]="*"
            diamond[2*n-2-i][j]="*"

    for r in diamond:
        for c in r:
            print(c,end='')
        print("")

diamond(n)