user_list=[]
non_repetitive_list=[]

while True:
    user_input= input("please enter a number/word or 'f' to finish: ")
    if user_input=="f":
        break
    else:
        user_list.append(user_input)

for x in user_list:
    if x not in non_repetitive_list:
        non_repetitive_list.append(x)

print("your list= " , user_list)
print("non repetitive list= " , non_repetitive_list)
