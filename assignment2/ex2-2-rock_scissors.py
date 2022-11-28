import random

computer_score=0
user_score=0

while computer_score<5 and user_score<5:
    x=random.randint(1,3)

    if x==1:
        computer_choice="rock"
    elif x==2:
        computer_choice="paper"
    elif x==3:
        computer_choice= "scissors"

    user_input= input("please enter 'r' for rock, 'p' for paper & 's' for scissors:")

    if user_input=="r":
        user_choice="rock"
    elif user_input=="p":
        user_choice="paper"
    elif user_input=="s":
        user_choice= "scissors"

    print("computer_choice: ", computer_choice)
    print("user_choice: ", user_choice)

    if computer_choice=="rock" and user_choice=="paper":
        user_score=user_score+1
    elif computer_choice=="rock" and user_choice=="scissors":
        computer_score=computer_score+1
    elif computer_choice=="paper" and user_choice=="rock":
        computer_score=computer_score+1
    elif computer_choice=="paper" and user_choice=="scissors":
        user_score=user_score+1
    elif computer_choice=="scissors" and user_choice=="rock":
        user_score=user_score+1
    elif computer_choice=="scissors" and user_choice=="paper":
        computer_score=computer_score+1

print("computer_score: ",computer_score)
print("user_score: ",user_score)

if computer_score==5:
    print("🙁")
    print("you lose")
else:
    print("🎉👏")
    print("you win")