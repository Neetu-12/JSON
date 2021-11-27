import json
a= {'4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
b=a.items()
s=sorted(b)
r={}
r.update(s)
c=r
n=json.dumps(c)
print(type(n),n)