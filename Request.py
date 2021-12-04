###1)))))By:---Meee...
book={}
book['tom']={'name':'tom','address':
'1 red street,NY','phone':989898
}
book['bob']={'name':'bob','address':
'1 red street,NY','phone':23452332
}
import json
s=json.dumps(book)
# print(s)
with open("/home/admin123/Desktop/REQUEST/neet.json","w") as f:
    f.write(s)
    f.close()
    
##2)))).................
# f=open("neet.json","r")
# s=f.read()
# f.close()
# print(s)
print(book['bob']["phone"],book["tom"]["phone"])