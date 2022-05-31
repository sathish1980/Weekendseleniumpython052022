from BasicPython.Bank import bank
from BasicPython.HDFC import HDFC


class SBI(bank):

    def Sbicustomerinfo(self,custname):
        print("Welcome to SBI")
        print("Good Day Mr/Mrs . "+custname)

sbiobj=SBI()
sbiobj.Sbicustomerinfo("Besant")
sbiobj.customerinfo("S")

