tup = (1,3,7,2,4,3)
print tup

# Count the one repetative number
countOfTwo=tup.count(3)
print countOfTwo

# Fetch the value
fetchingValue=tup[1]
print fetchingValue
print tup

# We can not change the value of tuple but we can convert tuple into list
print
print("tuple converted into list-------------")

print("tuple converted into list")
tupleConvertIntoList = list(tup)
print tupleConvertIntoList

print
print(" adding at 1 index new value ")
tupleConvertIntoList.insert(1,3)
print tupleConvertIntoList

print
print("replace the value insted of 1")
tupleConvertIntoList[0]=3
print tupleConvertIntoList
print

print("List converted into tuple-------------")
listConvertIntoTupple=tuple(tupleConvertIntoList)
print listConvertIntoTupple
print

print (3 in listConvertIntoTupple)

print("Delet tuple completly : it will show error like TUPLE IS NOT DEFINE")
del listConvertIntoTupple
print listConvertIntoTupple


