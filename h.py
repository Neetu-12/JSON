import json
a={"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }
b=json.dumps(a)
c=json.loads(b)
print(type(c),c)