# CREATION OF AN ARRAY

# importing array for array creation.
# import array // we can do it also
from array import *
# creating an array with integer type.
arr=array.array('i',[1,2,3,4])

# Printing array
print ("integer array is ="),
for i in range(4):
    print arr[i],
print

# ---------------------
# creating array with double type
print
arr=array.array('d',[2.2,1.2,4.3,3.2])

# printing array
print ("double array is = "),
for i in range(4):
    print arr[i],
print

# ---------------------
#  creating array with string type
print
arr=array.array('f',[7.7,8.8,9.9,0.9])

# printing array
print ("float array is = "),
for i in range(4):
    print arr[i],
print
# inserting into array using insert() function

arr.insert(1,7.1)
# print "after inserting one element at 1st position  "
print "array after inserting 7.1  = ",
for i in (arr):
    print i,

# --------------------------------
# creating array with int type
print
print "array with integer type  "
arr=array.array('i',[1,2,3,4,5,6])
print "before inserting using append"
for i in range(6):
    print arr[i],

print "after inserting using append"
arr.append(10)
for i in (arr):
    print i,

# --------------------------------
# creating array with String type
print
print "string array"






