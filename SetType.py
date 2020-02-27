setType = set({1,2,3,3})
print setType

# setType[1]=1
# print setType

setType.add(4)
print setType

setType.remove(3)
print setType
print
setType.update([3,5,6,7])
print setType
print

setType.pop()
print setType
print

setType.pop()
print setType

print (1 in setType)

setEx ={98,45,100,78,35}
print setEx

setEx.pop()
print setEx


setExTwo = {3,2,4,1,5,6}
setExTwo.clear()
print setExTwo

# setExTwo = {3,2,4,1,5,6}
# del setExTwo
# print setExTwo

set1 = {"avani" , "jayant" , "kale"}
set2 = {1,4,3,2,6,5}

set1.update(set2)
print (set1)

setNew = set1.union(set2)
print (setNew)

setName = {"a","b","c","a","d"}
setNo = {2,2,1,3}

setAns = setName.union(setNo)
print setAns
print
setName.update(setNo)
print setName
print

# constructor

setConstructor = set((5,4,6,3,9,0,2))
print setConstructor