import json
print("Welcome to login signup")
print("Press 1 to login")
print("Press 2 to signup")
user=int(input("press the button"))
if user==1 :
    name=input("enetr your name")
    password=input("enter the password")
    u,l,d,s=0,0,0,0
    if len(password)>=6:
        for i in password:
            if (i.isupper()):
                u=1
            if i.isdigit():
                d=1
            if i.islower():
                l=1
            if i=="@" or i=="!" or i=="#" or i=="$" or i=="%" or i=="^" or i=="&" or i=="*"==s:
                s=1
        t=u+l+d+s
        if t==4:
            print("password submitt succesess")
        else:
            print("please atlease 1 cappital small special number")
    else:
        print("password is too short")
    file=open("Neetu.json","r")
    n=file.read()
    if name in n:
        if password in j:
            print("your login successfull")
            print("-----------------------")
            print(n)
        else:
            print("please enter correct password")
    else:
        print()
        print("first login your account")

else:
    name=input("enetr your name")
    password=input("enter the password")
    u,l,d,s=0,0,0,0
    if len(password)>=6:
        for i in password:
            if (i.isupper()):
                u=1
            if i.isdigit():
                d=1
            if i.islower():
                l=1
            if i=="@" or i=="!" or i=="#" or i=="$" or i=="%" or i=="^" or i=="&" or i=="*"==s:
                s=1
        t=u+l+d+s
        if t!=4:
            print("please atlease 1 cappital small special number")
        else:
            password2=input("confirm password")
            if password!=password2:
                print("please enter correct password")
            else:
                hobby=input("enter your hobby")
                birth=input("enter your DOB")
                gender=input("eneter your gender")
                designation=input("enter your post")
                dic={}
                dic["password"]=password
                dic["hobby"]=hobby
                dic["birth"]=birth
                dic["gender"]=gender
                dic["designation"]=designation
                b=json.dumps(dic,indent=2)
                file1=open("Neetu.json","a")
                file1.writelines(b)
                file1.write("\n")
                file1.write("\n")
                file1.close()
                print()

                print("congratulation",name,"your signup successfully")
    else:
        print("password is too short")