user_sentence=input("please enter a sentences to count word's number: ")
no_of_words=0

sentence_len=len(user_sentence)

for i in range(sentence_len-1):

    if (user_sentence[i].isspace()==False) and (user_sentence[i+1].isspace()==True):
        no_of_words +=1

if user_sentence[sentence_len-1].isspace()==False:     #baraye akharin character
    no_of_words +=1

print("number of words in this sentences= ",no_of_words)