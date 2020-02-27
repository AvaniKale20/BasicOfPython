class Computer:
    # here the cpu and ram its just a argument, for assigning the value we can use self.cpu, why ?
    # bcz self is a object
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print ("1> its init method it will call automatically, no need to call like onther method we call")

        print

    def config(self):
        print ("config is ="+self.cpu,self.ram)
        print ("it is config method , it not built in method , it is not automatically called , we nned to call that method..")

# here we are creating an object (computer) of this class.
computer=Computer("i78",88)
computerOne=Computer("i",99)
computerTwo=Computer("hh",89)

# here we need to call config method similarly no need to call init method bcz it is built in method...
computer.config()
computerOne.config()
computerTwo.config()
print
Computer.config(computer)
Computer.config(computerOne)
Computer.config(computerTwo)


