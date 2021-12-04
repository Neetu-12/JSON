import requests
import json
url="http://saral.navgurukul.org/api/courses"
n=requests.get(url)

with open("course.json","w") as file:
    h=json.loads(n.text)
    # print(n)
    json.dump(h,file,indent=4)
    # print(n.text)
f=open("course.json","r")
dic=json.load(f)
f.close()
n=1
id=[]
for i in dic:
    # print(n,i)
    n=n+1
    for j in range(len(dic["availableCourses"])):
        print(j,dic["availableCourses"][j]["name"],":",dic["availableCourses"][j]["id"])
        id.append(dic["availableCourses"][j]["id"])
user=int(input("enter serial no.:-"))
n=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises")
m=n.json()
j=0
i=0
slug=[]
while j<len(m["data"]):
    print(i,m["data"][j]["name"])
    slug.append(m["data"][j]["slug"])
    i=i+1
    j=j+1

    slugname=int(input("**Enter your slug number:"))
    sluglist=requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname])
    b=sluglist.json()
    print("CONTENT",b["content"])
    print()
    print("**Up:-If you wanted to go back Menu")
    print("Next;-If you wanted to go to the content of next exercise")
    print("Previous:-If you wanted to go to the content of next exercise")
    print("Exit:-If you wanted to start again!**")
    
    i=0
    while i<len(slug):
            next_step = input("choose your next step:")
            if next_step == "up" or next_step == "Up":
                sluglist = requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname-1])
                b=sluglist.json()
                print(slugname-1,"content",b["content"])
            
            elif next_step == "previous" or next_step == "Previous":
                sluglist = requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname])
                j=sluglist.json()
                print(b["content"])
        
            elif next_step == "next" or next_step == "Next":
                sluglist = requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname+1])
                k=sluglist.json()
                print(slugname+1,"content:",k["content"]) 
            elif next_step == "exit" or next_step == "Exit":
                requests()
    requests()