class Computers:
      pass


c = Computers()
c2 = Computers()

print (id(c))
print (id(c2))

# every time whenever object is created then it will take some space
#  QUE : size of an object ?
#  ANS : its depend upon no of variable , how many data is present in it..
# QUE : who will decide ? who will calculate the memory ?
# Ans : that is constructor , it will call init() method internally no need to call explicitliy.
#  QUE : who will allocate size to object?