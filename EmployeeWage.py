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
    # #using random to check Attendance
    # check = random.randint(0,1)
    # if 1-> Present is 0-> Absent
    if check == full_time:
        print("Employee is Full-Time")
        emp_work_hour = 8
    elif check == part_time:
        print("Employee is Part-Time")
        emp_work_hour = 4
    else:
        print("Employee is Absent")
        emp_work_hour = 0
    
    #Calculating Daliy Wage
    daliy_wage = emp_work_hour * WAGE_PER_HOUR
    print("Daliy Wage is : ",daliy_wage)

#variables in switchers
full_time = 0
part_time = 1
absent = 2
#switche for calculating wages
switcher = {
    0: full_time,
    1: part_time,
    2: absent,
}

check = int(input("Enter 0:full-time-Wage 1:part-time-wage 2:Absent ==> "))
emp_Check = switcher.get(check,"Invalid Input")

if __name__ == "__main__":
    check_emp_wage()