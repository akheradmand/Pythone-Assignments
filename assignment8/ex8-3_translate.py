import gtts
import os

def read_from_file():
    global words_bank

    f= open("Pythone-Assignments/assignment8/translate.txt","r")
   
    words_list=f.read().split("\n")

    words_bank=[]
    for i in range(0,len(words_list),2):
        my_dict={"en":words_list[i],"fa":words_list[i+1]}
        words_bank.append(my_dict)
    f.close()
    # print(words_bank)

def translate_english_to_persian():

    user_text=input("enter your english text: ")
    user_words=user_text.split(" ")
    # print(user_words)

    output=""

    for user_word in user_words:
        for word in words_bank:
            if user_word==word["en"]:
                output=output + word["fa"] + " "
                break
        else:
            output=output + user_word + " "
    
    print("\033[38;5;4m"+output+"\033[0m")

def translate_persian_to_english():
    user_text=input("enter your persian text: ")
    user_sentences=user_text.split(".")

    output=""
    for user_sentence in user_sentences:

        user_words=user_sentence.split(" ")

        for user_word in user_words:
            for word in words_bank:
                if user_word==word["fa"]:
                    output=output+word["en"]+" "
                    break
            else:
                output=output+user_word+" "
        
        output=output+"."

    print("\033[38;5;4m"+output+"\033[0m")
    translated_voice=gtts.gTTS(output,lang="en",slow=False)
    translated_voice.save("Pythone-Assignments/assignment8/translated_voice.mp3")

def add_new_word():
    en_word=input("please enter english word: ")
    fa_word=input("please enter the meaning of word: ")

    path='Pythone-Assignments/assignment8/translate.txt'
    isExisting = os.path.exists(path)
    if isExisting==True:
        f=open(path,"a")
        f.write("\n")
        f.write(en_word)
        f.write("\n")
        f.write(fa_word)
        f.close()
        print("\033[38;5;4m"+"Thanks,these words added to our word bank"+"\033[0m")
    else:
        print("\033[38;5;4m","This path is not correct","\033[0m")

def show_menu():
    print("welcome to my translator")
    print("1- translate english to persian")
    print("2- translate persian to english")
    print("3- add a new word to database")
    print("4- exit")

read_from_file()

while True:
    show_menu()
    choice = int(input("enter your choice: "))

    if choice==1:
        translate_english_to_persian()
    elif choice==2:
        translate_persian_to_english()
    elif choice==3:
        add_new_word()
    elif choice==4:
        exit(0)
        