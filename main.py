#create menu for employee managment
from company import Company
def Menu():
    print(f"""Wellcome to employee managment
    1-Add employee
    2-Search employees
    3-Show all employee
    4-Delete employee
    5-Update employee
    6-Calculate Salary
    7-Save to JSON
    8-Load from JSON
    9-Exit
    
        """)
company1=Company()
while True:
    Menu()
    choose=input("Enter a number: ")

    if choose == "1":
        company1.add_employee()
        
    elif choose == "2":
        company1.Search_employee()

    elif choose == "3":
        company1.Show_Employees()

    elif choose == "4":
        company1.Delete_employee()
        
    elif choose == "5":
        company1.update_employee()

    elif choose == "6":
        company1.calculate_salary()
    
    elif choose == "7":
        company1.save_json()
        

    elif choose == "8":
        company1.load_json()

    elif choose == "9":
        break

    
