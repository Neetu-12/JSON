#Q.3 Python object ko json string mai convert karne ka program likho?
import json
a={
    "name": "David", 
    "class": "I", 
    "age": 6
}
f=json.dumps(a)
print(type(f),f)