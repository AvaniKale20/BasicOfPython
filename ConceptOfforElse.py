#  ------------------------------------------
# if there is no number which is divisible by 5, then print not found but , here is one problem it s printing
# five time bcs else part is after that if part and in loop its present.
print
x=[1,4,11,7,19]

for i in x:
    if i % 5 == 0:
        print i
        break
    else:
        print ("not found")

# ---------------------------------
#  here problem is solve he we have to write else part in for loop line .. its Concept of  "for else"
print
print("concept of for else ---------------------")
x=[1,4,11,7,19]

for i in x:
    if i % 5 == 0:
        print i
        break
else:

 print ("not found")

# ---------------------------------
#  here break statement is why important ? bcs it will print 10 and after that not found
print
print("Break statement is imp ---------------------")
x=[1,4,11,10,19]

for i in x:
    if i % 5 == 0:
        print i
        break
else:

 print ("not found")