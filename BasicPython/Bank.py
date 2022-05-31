class bank(): #parent class

    def customerinfo(self,customeridentification):
        if(customeridentification=="S"):
            print("You are savings account customer")
        elif (customeridentification == "C"):
            print("You are current account customer")
        else:
            print("You are not a valid account customer. Please provide valid account identificatin ifo")

