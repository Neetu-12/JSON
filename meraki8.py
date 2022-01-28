a=["neelam","programer","24","2400",]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
r={}
d={}
for i in range(len(a)):
    if i==0:
        d["name"]=a[i]
    elif i==1:
        d["Designation"]=a[i]
    elif i==2:
        d["age"]=a[i]
    elif i==3:
        d["salary"]=a[i]
r["emp1"]=d
d1={}
for i in range(len(b)):
    if i==0:
        d1["name"]=b[i]
    elif i==1:
        d1["Designation"]=b[i]
    elif i==2:
        d1["age"]=b[i]
    elif i==3:
        d1["salary"]=a[i]
r["emp2"]=d1
d2={}
for i in range(len(c)):
    if i==0:
        d2["name"]=c[i]
    elif i==1:
        d2["Designation"]=c[i]
    elif i==2:
        d2["age"]=c[i]
    elif i==3:
        d2["salary"]=c[i]
r["emp3"]=d2

print(r)