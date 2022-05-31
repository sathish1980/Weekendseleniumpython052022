from BasicPython.Bank import bank


class HDFC(bank): #child /derived class

    def customerdetails(self,custname):
        print("Welcome to HDFC")
        print("Good Day Mr/Mrs . "+custname)

obj=HDFC()
obj.customerdetails("sahtish")
obj.customerinfo("C")



