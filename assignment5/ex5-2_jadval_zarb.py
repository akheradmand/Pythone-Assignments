def javdal_zarb(n,m):

    jadval_zarb=[]
    row=[]

    for i in range(0,m+1):
        row.append(i)
    jadval_zarb.append(row)

    for i in range(1,n+1):
        row=[i] #a'dadae 1 ta n kenar jadval
        for j in range(1,m+1):
            field=i*j
            row.append(field)
        
        jadval_zarb.append(row)

    jadval_zarb[0][0]="x"

    for r in jadval_zarb:
        for c in r:
            print(c,end=' ')
        print("")

n= int(input("n= "))
m= int(input("m= "))

javdal_zarb(n,m)
