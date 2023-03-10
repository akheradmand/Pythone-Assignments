print("Please enter array number's to check if it is symmetrical or not (enter / to end): ")
input_array=[]

while True:
    i=input()
    if i=="/":
        break
    else:
        input_array.append(i)

print("input array= ",input_array)
n=len(input_array)

for i in range(n//2):
    if input_array[i]!=input_array[n-i-1]:
        print("input array is not symmetrical")
        break
else:
    print("input array is symmetrical")