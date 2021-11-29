#Q.3 Python object ko json string mai convert karne ka program likho?
import json
a={
    "name": "David", 
    "class": "I", 
    "age": 6
}
f=json.dumps(a)
print(type(f),f)

#2)))
#Json to Python...
import json
a='{"one":1,"two":2,"three":3}'
b=json.loads(a)
print(type(b))
