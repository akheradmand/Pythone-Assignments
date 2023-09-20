user_number= int(input("please enter your number: "))

q=user_number
i=1

while True:

    if user_number<=0:
        print("Invalid number")
        break

    elif (q % i !=0):
        print("This number is not the answer of factorial❌")
        break

    elif (q % i == 0):

        q= q / i
        if q==1:
            print("yes," , user_number , "=" , i , "!")
            break
        
        else: 
            i=i+1
            