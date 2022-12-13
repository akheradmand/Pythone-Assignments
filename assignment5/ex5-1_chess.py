n= int(input("enter nnumber of rows: "))
m= int(input("enter nnumber of columns: "))

def chess(n,m):

    chess_list=[]

    for i in range(n):
        row=[]
        
        for j in range(m):
            if (i+j) % 2 ==0:
                row.append("*")
            else:
                row.append("#")
        
        chess_list.append(row)
        

    for r in chess_list:
        for c in r:
            print(c,end=' ')
        print("")

chess(n,m)