# import json
# a= {'4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}
# b=a.items()
# s=sorted(b)
# r={}
# r.update(s)
# c=r
# n=json.dumps(c)
# print(type(n),n)


import json
a={
 "a":  1,
 "a":  2,
 "a":  3, 
 "a": 4,   
 "b": 1, 
 "b": 2}
f=json.dumps(a)
p=json.loads(f)
print(type(p),p)




# import random
# def hangman():
#     list_of_words=["Neetu","Baby","Suraj","Daksh"]
#     word=random.choice(list_of_words)
#     turns=10
#     guessmade=""
#     valid_entry=set("abcdefghijklmnopqrstuvwxyz")
#     while len(word)>0:
#         main_word=""
#         missed=0
#         for letter in word:
#             if letter in guessmade:
#                 main_word=main_word+letter
#             else:
#                 main_word=main_word+"_"
#         if main_word==word:
#             print(main_word)
#             print("you won!!!!")
#             break

#         print("guess the words",main_word)
#         guess=input()

#         if guess in valid_entry:
#             guessmade=guessmade+guess
#         else:
#             print("enter valid character")
#             guess=input()
#         if guess not in word:
#             turns=turns-1
#             if turns==9:
#                 print("9 turns are left")
#                 break
# name=input("enter the name")
# print("Welcome ",name)
# hangman()
