user_array=[]

while True:
    user_input=input("please enter a number or 'f to finish entering data: ")

    if user_input=="f":
        break
    else:
        user_array.append(float(user_input))

print(user_array)

breaker=False
for i in range(len(user_array)):

    for j in range(i+1,len(user_array)):

        if user_array[i]>user_array[j]:
            print("❌This array is not sorted from smallest to largest")
            breaker=True
            break

    if breaker==True:
        break
if breaker==False:
    print("✅This array is sorted from smallest to largest")
