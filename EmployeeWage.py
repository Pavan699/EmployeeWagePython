'''
@Author: Pavan Nakate
@Date: 2021-11-08 01:13
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Employee Wage
'''
print("Welcome to Employee Wage Problem Solution")
import random

def check_emp_wage():
    """
    Description:
        This function is to check whether employee is present or absent.
        Random fuction is used to check the attendace.
    Parameter:
        None
    Return:
        None
    """  
    #contant
    WAGE_PER_HOUR = 20
    #using random to check Attendance
    check = random.randint(0,1)
    # if 1-> Present is 0-> Absent
    if check == 1:
        print("Employee is present")
        emp_work_hour = 8
    else:
        print("Employee is absent")
        emp_work_hour = 0
    
    #Calculating Daliy Wage
    daliy_wage = emp_work_hour * WAGE_PER_HOUR
    print("Daliy Wage is : ",daliy_wage)

if __name__ == "__main__":
    check_emp_wage()