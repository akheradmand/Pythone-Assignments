n=int(input("please enter a number(1-...): "))

snake=[]

for i in range(0,n):
    snake.append("*")

for j in range(1,n,2):
    snake[j]="#"

for i in range(n):
    print(snake[i],end='')