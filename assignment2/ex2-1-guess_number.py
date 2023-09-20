import random

computer_number=random.randint(10,40)
i=0

while True:

    user_number= int(input())
    i=i+1

    if computer_number==user_number:
        print("you win")
        print("you guess number in ", i, "times")
        print("👏")
        break

    elif computer_number>user_number:
        print("boro bala")
        print("")

    elif computer_number<user_number:
        print("bia paeen")
        print("")