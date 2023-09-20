user_list=[]
reverse_user_list=[]

while True:
    user_input= input("please enter a number/word or 'f' to finish: ")
    if user_input=="f":
        break
    else:
        user_list.append(user_input)

for i in range(len(user_list),0,-1):
    reverse_user_list.append(user_list[i-1])

print("your list= ", user_list)
print("reverse of your list= " ,reverse_user_list)
