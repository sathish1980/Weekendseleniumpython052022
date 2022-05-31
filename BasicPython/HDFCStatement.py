from BasicPython.HDFC import HDFC
from BasicPython.SBI import SBI


class HDFCStatement(HDFC,SBI):

    def ministatement(self):
        print("Statement for last 10 transaction")
        print("10-22022  1000.00")
        print("10-22022  1002.00")

    def Annualstatment(self):
        print("Statement for last one year")
        print("10-22022  10.00")
        print("10-22022  100.00")

mini=HDFCStatement()
mini.customerdetails("Besant")
mini.customerinfo("C")
mini.ministatement()
mini.Annualstatment()
mini.Sbicustomerinfo("sathish")