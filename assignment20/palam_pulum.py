import random

computer1_score=computer2_score=your_score=0

for i in range(5):
    computer1_choice=random.choice(["✋","🤚"])
    computer2_choice=random.choice(["✋","🤚"])
    your_choice=input("please enter your choice: b / f: ")
    
    if your_choice=="f":
        your_choice="✋"
    elif your_choice=="b":
        your_choice="🤚"
    
    print(computer1_choice,computer2_choice,your_choice)

    if computer1_choice==computer2_choice!=your_choice:
        your_score += 1
    elif computer1_choice==your_choice!=computer2_choice:
        computer2_score += 1
    elif computer2_choice==your_choice!=computer1_choice:
        computer1_score += 1

max_score=max(computer1_score,computer2_score,your_score)
if max_score==computer1_score:
    print("computer1 win")
elif max_score==computer2_score:
    print("computer2 win")
elif max_score==your_score:
    print("you win👏")
    