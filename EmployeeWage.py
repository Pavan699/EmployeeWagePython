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
    #using random to check Attendance
    check = random.randint(0,1)
    # if 1-> Present is 0-> Absent
    if check == 1:
        print("Employee is present")
    else:
        print("Employee is absent")

if __name__ == "__main__":
    check_emp_wage()