class zomatostudentclass():
    overallamount=[]

    def countofitem(self, food, count):
        global overallamount
        foodprice = {"dosai": "25", "idly": "5", "meals": "150", "chapathi": "40", "biriyani": "200",
                     "chickenrice": "170",
                     "idiyappam": "15", "poori": "25", "mutton": "170", "fishfry": "75"}

        if (food == "dosai"):
            if (count < 40):
                totalamount = count * int(foodprice["dosai"])
                self.overallamount.append(int(totalamount))
                print('cost of ' + str(count) + ' dosai is:' + str(totalamount))
            else:
                print("dosai is not available")
        if (food == "idly"):
            if (count < 30):
                totalamount = count * int(foodprice["idly"])
                self.overallamount.append(totalamount)
                print('cost of ' + str(count) + ' idly is:' + str(totalamount))
            else:
                print("idly is not available")
        if (food == "meals"):
            if (count < 40):
                totalamount = count * int(foodprice["meals"])
                self.overallamount.append(int(totalamount))
                print('cost of ' + str(count) + ' meals is:' + str(totalamount))
            else:
                print("meals is not available")

    def totalamount(self):
        tamount = 0
        for eachamount in self.overallamount:
            tamount = tamount + eachamount
        print(""+str(tamount))


obj=zomatostudentclass()
obj.countofitem("dosai",4)
obj.countofitem("idly",4)
obj.countofitem("meals",4)
obj.totalamount()