class stringhandle() :
    def stringconecpt(self):
        name1="sathish kumar R"
        name2 = ' satish kumar '
        name3 ="""sathish kumar R
        B.Tech
        Tester"""
        print(name1)
        print(name2)
        print(name3)
        print(name1[0])
        print(len(name3))
        for x in range(0,len(name3)):
            print(name3[x])

        if("B.Tech" not in name3):
            print("true")
        else:
            print("this is present")

        print(name3[2:10])
        print(name1[-1])
        print(name1.upper())
        print(name1.lower())
        print(name1.isupper())
        print(name2)
        print(name2.strip())
        print(name2.replace(" ",""))
        print(name2.replace("a","A"))
        print(name2.split("a"))
        print(name2.split(" "))
        print(name1+name2)
        name4="sathis's is a trainer in \"Besant\""
        print(name4)
        print(name2.count("z"))
        print(name2.endswith(" "))
        print(name2.rstrip())
        print(name2.lstrip())
obj=stringhandle()
obj.stringconecpt()
