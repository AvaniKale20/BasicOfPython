dictionarytype = {1:'a',2:'b',3:'c',5:'e'}
print dictionarytype
print
print ("there is 2nd way to Fetching the value through key---------------------")
print dictionarytype.get(5)
print dictionarytype.get(4)
print



print ("there is one way to Fetching the value through key---------------------")
print dictionarytype[1]
print dictionarytype[5]
# print dictionarytype[4]
print

dictionarytype[1]="abc"
print dictionarytype

print dictionarytype.pop(1)
print dictionarytype

print dictionarytype.popitem()
print dictionarytype
# if "b" in dictionarytype:
#     print ("yes")

newDictionary = {
    "fff":9000,
    "hhh":456,
    "avani":1234,
    "aman":2345,
    "sneha":3456
}
print newDictionary
print newDictionary.popitem()
print newDictionary

print
newCopyDictionary = newDictionary
print newCopyDictionary

newMy=newDictionary.copy()
print newMy
# --------------------------------------
print
key = ["navin","harsh", "kiran"]
values = ["python","java","js"]
print (key,values)
# If we want to convert into dictionary, we want to mearge that thing
data = zip(key,values)
print data
conertIntoDictionary= dict(data)
print conertIntoDictionary