x=4
y=6
print("print value of x variable:-----------------")
print(x)

print
print("sum of x and y :-----------------")
print(x+y)

print
x=7
print("sum of x and y after changing value of x :-----------------")
print"x+y =",x+y

# print("If we want to use output of the previous outpur then go through '-' underscore ")
# x=1
# y=2
# x+y
# temp= +y
# print x+y
print
print("USING STRING :-------------  ")
name="Avani"
print name
print name + " rock"

print
print("Fetching the character from string :-------------  ")
name="Avani"
print name[0]
print name[2]
print name[4]
# print name[5] it will show string index out of range  length of the string is 5 (start from 0 to 4);

print
print("Fetching the character from end of the string  :-------------  ")
name="Avani"
print name[-1]#i
print name[-2]#n
print name[-4]#v
print name[-5]#a

print
print("Fetching the 1st more than one character from  the string  :-------------  ")
name="Avani"
print name[0:2] #Av
print name[0:4] #Avan
print name[2:]#ani
print name[:2]#av
print name[:6]

print
print("WE CANT CHANGE VALUE OF VARIABLE ONCE WE ASSIGNED : :-------------  ")
name="YOUTUBE"
print "1st value of the name variable = ",name
print "2st value using fetching value from character = ", "MY" + name[3:]

print
print("WE CANT CHAKE LENGHT  : :-------------  ")
name="YOUTUBE "
print "length", len(name)


print
print("show error when printing value of undefined variable :----------------------")
print (" it will show 'z' is not defined ")
print(z)