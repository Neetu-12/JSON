import random
print("!!!Welcome to the Game Cow Bull!!!")
while True:
    def cow_bull(l):
        b=random.sample(l,5)
        print(b)
        i=1
        r=[]
        cow=[]
        turns=8
        while i<=8:
            j=0
            user=int(input("Enter the no."))
            postn=int(input("Enter postion no."))
            while j<len(b):
                if user in b:
                    if user==b[j]:
                        if postn==j:
                            if user not in r:
                                r.insert(j,b[j])
                                print("Bull",r,"\U0001F917")
                            else:
                                print("can't take same element")
                                break
                        else:
                            cow.insert(j,b[j])
                            print("cow ","you r right but postion is wrong you can reuse it again",cow,"\U0001F919")
                else:
                    print('You are not exist in secret number!')
                    break   
                j=j+1
            turns-=1
            if len(r)==len(b):
                return ('you are winner')
            if turns==0:
                pass
            print(turns,"chance left")
            i=i+1
    li=[0,1,2,3,4,5,6,7,8,9]
    cow_bull(li)
    s= input("Do you want to play again enter yes/no:")
    if s=="yes":
        print(cow_bull(li))
    else:
        print("Game over")
    break