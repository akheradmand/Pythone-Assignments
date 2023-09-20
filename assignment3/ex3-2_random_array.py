import random

lower_bound=int(input("please enter the lower_bound: "))
upper_bound=int(input("please enter the upper_bound: "))
n=int(input("please enter the length: "))

if n>upper_bound-lower_bound+1:
    print("This is impossible")

else:

    non_frequent_array=[]

    while len(non_frequent_array)<n:

        random_number=random.randint(lower_bound,upper_bound)

        non_frequent_array.append(random_number)

        if len(set(non_frequent_array))!=len(non_frequent_array):

            non_frequent_array.remove(random_number)

    print(non_frequent_array)
    