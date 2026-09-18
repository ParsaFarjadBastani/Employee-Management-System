from employee import Employee
import json


#create class for company
class Company:
    def __init__(self):
        self.employees=[]

    def add_employee(self):
        id=input("Enter your id: ")
        name=input("Enter your name: ")
        age=input("Enter your age: ")
        email=input("Enter email: ")
        position=input("Enter your position: ")
        salary=input("Enter your salary: ")
        employee1=Employee(id,name,age,email,position,salary)
        self.employees.append(employee1)
        print("Employee Added successfully ")

    def Search_employee(self):
        if not self.employees:
            print("No employee added!")
            return

        name1=input("Enter employee name: ")
        for employee in self.employees:
            if name1 == employee.name:
                print(f"""ID={employee.id}
                        NAME={employee.name}
                        AGE={employee.age}
                        EMAIL={employee.email}
                        POSITION={employee.position}
                        SALARY={employee.salary}""")
    def Show_Employees(self):
        if not self.employees:
            print("No employee ")
            return
        for i , employee in enumerate (self.employees,start=1):
            print(f"""{i}-ID={employee.id}
                        NAME={employee.name}
                        AGE={employee.age}
                        EMAIL={employee.email}
                        POSITION={employee.position}
                        SALARY={employee.salary}""")

    def Delete_employee(self):
        if not self.employees:
            print("No employee")
            return
        name1=input("Enter employee`s name: ")

        for employee in self.employees:
            if name1 == employee.name:
                self.employees.remove(employee)
                print("The employee deleted successfully")
                return
        print("The employee not found")
        


    def update_employee(self):
        if not self.employees:
            print("No employee")
            return

        search_id=input("Enter id: ")

        for employee in self.employees:
            if search_id==employee.id:
                
                id=input("Enter your id: ")
                name=input("Enter your name: ")
                age=input("Enter your age: ")
                email=input("Enter email: ")
                position=input("Enter your position: ")
                salary=input("Enter your salary: ")
                employee.id=id
                employee.name=name
                employee.age=age
                employee.email=email
                employee.position=position
                employee.salary=salary
                print("Employee updated")
                return
        print("Employee not found")
    


    def calculate_salary(self):
        print("The salary is 5000$ per day")
        days=int(input("Enter the day you worked"))

        salary=lambda days:days * 5000
        print(f"The salary is {salary(days)}")

    def save_json(self):
        if not self.employees:
            print("No employee to save")
            return
        employees=[]
        for employee in self.employees:

            employee_dic={"ID":employee.id,"NAME":employee.name,
                          "AGE":employee.age,
                          "EMAIL":employee.email,
                          "POSITION":employee.position,
                          "SALARY":employee.salary}

            employees.append(employee_dic)
        with open("employees.json" , "w" ,encoding="utf-8") as file:

            json.dump(employees,file,indent=4)

        print("The file has saved successfully")

    def load_json(self):
        with open("employees.json","r",encoding="utf-8")as file:
            employees=json.load(file)
            self.employees=[]
            for employee in employees:
                employee1=Employee(employee["ID"],employee["NAME"],employee["AGE"],
                        employee["EMAIL"],employee["POSITION"],employee["SALARY"])
                self.employees.append(employees)
            
            print("The employee loaded successfully")







        

            

        


        
