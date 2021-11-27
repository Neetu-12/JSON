import json
a={"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }
b=json.dumps(a)
c=json.loads(b)
print(type(c),c)

# import json
# a={"neetu":"suraj","baby":"bhn"}
# a1=json.dumps(a)
# print(a,type(a1))

# import json
# f=open("m.json")
# a=json.load(f)
# print(a)

# import json
# f=open("n.json")
# a=json.load(f)
# # print(type(f))
# print(a)

####   we have used the open() function to read the JSON file. Then, the file is parsed using json.load() method which gives us a dictionary named data.
# import json
# f=open("m.json")
# a=json.load(f)
# print(a)