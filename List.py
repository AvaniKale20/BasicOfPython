name = ["avani","sneha","john","ellina"]
print name

numbers = [10,9,8,07]
print numbers

stringAndInteger = ["abc",100,"yz"]
print stringAndInteger

multipleList  = [numbers,name]
print multipleList

name.append("stafon")
print name

numbers.insert(0,100)
print numbers
numbers.remove(100)
print numbers
numbers.pop(0)
# 9,8,7
numbers.pop(1)
# 9,7
numbers.pop(0)
# 7
print numbers

name.pop()
print name

no_=[1,2,3,4,5]
print no_
del no_[2:]
print no_

no_.extend([100,35,67])
print no_
no_.sort()
print no_
print min(no_)
print max(no_)
print sum(no_)


productList = ["suger","sweet","honey","lemon"]
print productList
productList[1] = "abc"
print productList
productList.insert(1,"sweet")
print productList

# Print arrays value one by one , print all the item in list one by one
print
for x in productList:
    print x
