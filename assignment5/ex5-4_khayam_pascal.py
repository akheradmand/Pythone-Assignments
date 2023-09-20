n=int(input("please enter number of rows: "))

def khayam_pascal(n):

    khayam_pascal=[]

    for i in range(n):
        row=[]
        for j in range(0,i+1):
            row.append(1)
        khayam_pascal.append(row)

    for i in range(2,n):
        for j in range(1,i):
            khayam_pascal[i][j]=khayam_pascal[i-1][j]+khayam_pascal[i-1][j-1]

    for r in khayam_pascal:
        for c in r:
            print(c,end='  ')
        print("")

khayam_pascal(n)
