def myFunction():
    print "new function"
myFunction()
# -----------------------
print
def funsum(x,y):
    print (x+y)

funsum(1,2)
# ------------------------
print
def function(name):
    print ("name is = "+name)

function("avani")

# ARBITARY * ARGUMENT
# -------------------------
print
def functionWithArbitaryArgument(*name):
    print (name[2] + " is smart...")

functionWithArbitaryArgument("avani","stella","ellena")



