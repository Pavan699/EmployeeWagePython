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
    MAX_WORK_DAYS = 20
    MAX_WORK_HOURS = 100
    #variables
    total_wage = 0
    total_working_hours = 0
    total_working_days = 0
    
    while not(total_working_days == MAX_WORK_DAYS or total_working_hours == MAX_WORK_HOURS):
        # if 0-> Fulltime is 1-> Parttime 2->Absent
        check = random.randint(0,2)
        if check == full_time:
            print("Employee is Full-Time")
            emp_work_hour = switcher.get(check,"Invalid Input")
        elif check == part_time:
            print("Employee is Part-Time")
            emp_work_hour = switcher.get(check,"Invalid Input")
        else:
            print("Employee is Absent")
            emp_work_hour = switcher.get(check,"Invalid Input")
    
        #Calculating Daliy Wage
        daliy_wage = emp_work_hour * WAGE_PER_HOUR
        print("Daliy Wage is : ",daliy_wage)

        #incrementing hours and days
        total_working_days += 1
        total_working_hours += emp_work_hour

        total_wage += daliy_wage
    print("Total Month Wage is : ",total_wage)

#variables in switchers
full_time = 0
part_time = 1
absent = 2
#switche for calculating wages
switcher = {
    0: 8,
    1: 4,
    2: 0,
}

if __name__ == "__main__":
    check_emp_wage()