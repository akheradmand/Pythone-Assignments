import random

boys = ['mohammad', 'sobhan', 'abdollah', 'kiya', 'mahdi', 'sajjad', 'homan', 'arman']
girls = ['mahtab', 'hane', 'harir', 'fateme', 'kiana', 'faezeh', 'minoo', 'mina', 'soghra']
result=[]

for i in range(min(len(boys),len(girls))):
    
    groom=random.choice(boys)
    bride=random.choice(girls)

    boys.remove(groom)
    girls.remove(bride)

    result.append((groom,bride))
 
print(result)
