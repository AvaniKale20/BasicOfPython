i=1
while i<=4:
    print("# # # #")
    i=i+1
# -------------------------------------------

print

for i in range(4):
    for j in range(4):
         print ("# "),

    print
# ----------------------------------------

for i in range(4):
    for j in range(i+1):
        print ("X"),

    print
# ----------------------------------------

print
for i in range(4):
    for j in range(4-i):
        print ("X"),

    print
#  ------------------------------------------
# here only one number is present which is divisible by five
print
x=[1,4,5,6,7]

for i in x:
    if i % 5 == 0:
        print i

#  ------------------------------------------
# here only two number is present which is divisible by five
print
x=[1,4,5,6,7,15]

for i in x:
    if i % 5 == 0:
        print i
#  ------------------------------------------
# We want only one number which is first ,here more than one number are present which is divisible by five
print
x=[1,4,5,10,7,15]

for i in x:
    if i % 5 == 0:
        print i
        break

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
x=[1,4,11,7,19]

for i in x:
    if i % 5 == 0:
        print i
        break
    else:
        print ("not found")