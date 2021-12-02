import random
print ("!!!Welcome to the game, Hangman!!!")
def hangman():
    list_of_words=["neetu","baby","suraj","daksh"]
    word=random.choice(list_of_words)
    # print(word)
    turns=10
    guessmade=""
    valid_entry=set("abcdefghijklmnopqrstuvwxyz")
    while len(word)!=0:
        main_word=""
        missed=0
        for i in word:
            if i in guessmade:
                main_word=main_word+i
            else:
                main_word=main_word+"_"
        if main_word==word:
            print(main_word)
            print("you won!!!!")
            break

        print("guess the words",main_word)
        guess=input()

        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter valid character")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns are left")
                print("----------------")
            if turns==8:
                print("8 turns are left")
                print("----------------")
                print("        O       ")
            if turns==7:
                print("7 turns are left")
                print("----------------")
                print("   |____ O      ")
                print("   |     |      ")
            if turns==6:
                print("6 turns are left")
                print("----------------")
                print("  |____ O       ")
                print("  |     |       ")
                print("  |    /        ")
            if turns==5:
                print("5 turns are left")
                print("----------------")
                print("   |____ O      ")
                print("   |     |      ")
                print("   |   /   \    ")
            if turns==4:
                print("4 turns are left")
                print("----------------")
                print("  |____\ O      ")
                print("  |      |      ")
                print("  |    /   \    ")
            if turns==3:
                print("3 turns are left")
                print("----------------")
                print("   |___\ O /    ")
                print("   |     |      ")
                print("   |   /   \    ")
            if turns==2:
                print("2 turns are left")
                print("----------------")
                print("    |__\ O / |  ")
                print("    |    |      ")
                print("    |  /   \    ")
            if turns==1:
                print("1 turns are left")
                print("----------------")
                print("   |___\ O /_|  ")
                print("   |     |      ")
                print("   |   /   \    ")
            if turns==0:
                print("Uloose the Game")
                print("U  die a man")
                break

name=input("enter the name")
print("Welcome ",name)
hangman()