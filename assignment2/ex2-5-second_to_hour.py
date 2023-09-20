print('Welcome User')
print("This program help you to convert seconds to hr:m:s")

sec=int(input("please enter seconds:"))

if sec<0:
    print("Invalid input")
else:
    hr=sec//3600
    m=(sec%3600)//60
    s=(sec%60)

    print(sec, "seconds"," = ",hr,":",m,":",s)
    