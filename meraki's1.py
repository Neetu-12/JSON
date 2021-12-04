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
for i in dic:
    # print(n,i)
    n=n+1
    for j in range(len(dic["availableCourses"])):
        print(j,dic["availableCourses"][j]["name"],":",dic["availableCourses"][j]["id"])