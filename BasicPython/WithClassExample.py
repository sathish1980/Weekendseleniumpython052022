class example():
    #print("Sathish")
    global a,b
    a=5
    b=25

    #constructor
    def __init__(self):
        print("sathish")
    def __init__(self,a):
        print("B.tech"+a)
    def funcation1(self,b):
        c=a+b
        print(c)

    def funcation2(self, d, b):
        c = d - b
        print(c)

    def voterid(self,State,age):
        if (State=="TN") or (State=='Tn'):
            if (age>18) and (age<=100):
                print("Your eliglble to apply voter id")
                if (age > 60):
                    print("Your eliglble to senior consession")
            else:
                manymore=18-age
                print("You have to wait for: "+str(manymore)+" more years")
        elif (State=="FR"):
            print("Your eliglble to apply voter id under FR")
        else:
            print("You are not part of Tamil Nadu")

    def whileloop(self,a,nextnumber):
        actualnumber=a+nextnumber
        while(a<=actualnumber):
            print("The value is : "+str(a))
            if (a==7):
                continue
            a+=1
    def continueexample(self):
        i=0
        while(i<6):
            i+=1
            if (i==3):
                continue
            print(i)
    fruits=["Apple","Orange","Mango","Pineapple"]
    for bs in fruits:
        if(bs=="Orange" or bs=="Mango"):
            continue
        print(bs)
    for x in range(0,11):
        print(x)

    def multipleforloop(self):
        fruits = ["Apple", "Orange", "Mango", "Pineapple"]
        vegs = ["carrot", "beetroot", "radish", "onion"]
        for fr in fruits:
            print(fr)
            for vg in vegs:
                print(vg)

    def studentlist(self,*name):
        print(name[1])
        for x in name:
            print(x)
    def Branch(self,brachname="Annanagar"):
        print(brachname)

name=example("kumar")
name.Branch("Tambaram")
