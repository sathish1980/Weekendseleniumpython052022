class constructor():

    global a
    def __init__(self):
        print("With out parameter")
    def __init__(self,firstparam):
        print("With parameter : " +firstparam)
    def add(self,a,b):
        self.a=a
        self.b=a
        print(a+b)
        #print(self.a)
        #print(a)


    def div(self,a,b):
        try:
            c=a/b
            print(c)
        except NameError:
            print("This is an exception")
        except ZeroDivisionError:
            print("You have entered the 0 value in the division number")
        except :
            print("error occured")
        finally:
            print("This is finally block")
    def sub(target):
        print(target.a)

    def raiseexception(self,name):
        try:
            if name=="sathish":
                raise Exception("He is most wanted")
                print("OK")
        except:
            print("Name matched with the list")
    def mul(target):
        print("this is mul: "+str(target.a))

con=constructor("besant") # instantiation
con.add(3,4)
con.div(10,0)
con.sub()
con.raiseexception("sathish")
con.mul()