class listconcept():

    def __init__(self):
        print("Constructor")

    def employeedetails(self,employeeexist):
        employees=["sathish","kumar","R","B.tech","sathish"]
        salary=[1000,2000,5000,6000]
        print(employees)
        print(salary)
        employees[1]="Sarath"
        #employees[5] = "Vinoth"
        employees.insert(3,"Vinoth")
        employees.insert(100,"sara")
        employees.append("sathish")
        print(employees)
        if (employeeexist in employees):
            print("Yes " + employeeexist + " exist in the company")
        for eachemployee in employees:
            print(eachemployee)
            """if(employeeexist==eachemployee):
                print("Yes "+eachemployee+ " exist in the company")
                break"""


        print(employees[1])
        print(employees[-2])
        print(salary[2])
        print(len(salary))
        print(employees[1:4])
        print(employees[6])
        employees.extend(salary)
        print(employees)
        #salary.extend(employees)
        print(salary)
        employees.remove("sathish")
        print(employees)
        employees.pop(2)
        print(employees)
        employees.pop(-3)
        print(employees)
        del employees[2]
        print(employees)
        #employees.clear()
        #print(employees)
       # del employees
       #print(employees)
        for X in range(0,len(employees)):
            print(employees[X])
        salary.sort()
        print(salary)
        salary.sort(reverse = True)
        print(salary)



obj=listconcept()
obj.employeedetails("kumar")
