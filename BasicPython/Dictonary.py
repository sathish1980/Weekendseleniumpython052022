class dictonaryconcept():

    def dictonary(self):
        employees = { "name":"sathish", "age" :"45", "qualification": "B.tech", "emplyeesstatus":"Yes","name1":"sathish",}
        salary = {"emp1":1000,"emp2": 2000,"emp3": 5000, "emp4" :6000}
        print(employees)
        print(salary)
        print(employees["age"])
        print(employees.get("age"))
        print(employees["name"])
        print(employees["qualification"])
        print(employees["emplyeesstatus"])
        print(len(employees))
        print(type(employees))
        print(employees.keys())
        emplyesskey=employees.keys()
        print(type(emplyesskey))
        print(employees.values())
        employees["name"]="Sara"
        print(employees)
        print(employees.items())
        if "name" in employees:
            print("keyt exist")
        employees.update({"qualification":"B.E"})
        print(employees)
        employees["Hobby"]="playing football"
        print(employees)
        employees["Hobby"] = "cricket"
        print(employees)
        employees.pop("emplyeesstatus")
        print(employees)
        employees.popitem()
        print(employees)
        del employees["name1"]
        print(employees)
        #del employees
        #employees.clear()
        print(employees)
        employees["designation"]="Manager"
        print(employees)
        for x in employees:
            print(employees[x])
        for x in employees.values():
            print(x)
        for x in employees.keys():
            print(x)
            print(employees[x])
        for x,y in employees.items():
            print(x,y)
        #employees+salary
        print(employees)

obj = dictonaryconcept()
obj.dictonary()