import json
a={
    "name": "David", 
    "class": "I", 
    "age": 6
}
f=json.dumps(a,indent=2)
print(f)

##output:-
{
    "name": "David", 
    "class": "I", 
    "age": 6
}
