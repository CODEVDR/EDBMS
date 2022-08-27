from datetime import datetime as dt
from sqlmodule import *

# For Date And Time
x = str(dt.now())
x = x.split()
# For Connection Purpose
pw = input("Enter Server Password : ")
cs = connect_server(pw)
if cs[2] != 0:
    q1 = f"""create database if not exists Employees_DB;"""
    execute_query(cs[0], q1)
    cd = connect_database(cs[1])
    print("\t\t\t\tPrayag's Employee Management System")
    while True:
        print("1.Employee registeration")
        print("2.Employee details")
        print("3.Update salary")
        print("4.Employees list")
        print("5.Work experience")
        print("6.Know your salary")
        print("7.Exit")
        ch = input("Enter Your Choice : ")
        if ch == "1":
            print()
            print("=============================================")
            emp_id = input("Enter Employee's Id : ").capitalize()
            name = input("Enter Employee's Name : ").capitalize()
            age = input("Enter Employee's Age : ").capitalize()
            addr = input("Enter Employee's Address : ").capitalize()
            ph_no = input("Enter Employee's Phone Number : ")
            sal_pm = input("Enter Employee's Salary Per Month : ")
            # Sql Code Starts From Here
            q0 = "use Employees_DB;"
            q1 = "create table if not exists employee_data(emp_id varchar(50) primary key,name varchar(50),age varchar(50),addr varchar(90),ph_no varchar(50),sal_pm varchar(50),doj varchar(70));"
            execute_query(cd, q0)
            execute_query(cd, q1)
            try:
                q2 = f"""insert into employee_data values("{emp_id}","{name}","{age}","{addr}","{ph_no}","{sal_pm}","{x[0]}");"""
                execute_query(cd, q2)
                print("-------------------")
                print("Stored Sucessfully")
                print("-------------------")
            except:  # If Employee id Is entered once again it Throws an Error
                print(
                    f"Employee Id '{emp_id}' already Present Try Entering a Different one.")
            print("=============================================")
            print()
        elif ch == "2":
            # Employee details
            print()
            print("====================================")
            emp_id = input("Enter Employee's Id : ").capitalize()
            name = input("Enter Employee's Name : ").capitalize()
            q1 = f"""select * from employee_data where emp_id="{emp_id}" && name="{name}";"""
            res = read_query(cd, q1)
            if res == []:
                print("-----------------")
                print("No Data Present")
                print("-----------------")
            else:
                print("-------------------------------------------")
                print("Emp_id,Name,age,addr,ph_no,Sal_pm,DOJ")
                print("-------------------------------------------")
                for i in res:
                    print(i)
            print("====================================")
            print()
        elif ch == "3":
            # Update salary
            print()
            print("=====================================")
            emp_id = input("Enter Employee's Id : ").capitalize()
            name = input("Enter Employee's Name : ").capitalize()
            up_sal_pm = input("Enter Updated Salary : ")
            try:
                q1 = f"""update employee_data set sal_pm="{up_sal_pm}" where emp_id="{emp_id}" && name="{name}";"""
                execute_query(cd, q1)
                print("---------------------------")
                print("Sucessfully Updated Salary")
                print("---------------------------")
            except:
                print("----------------------------------------------------")
                print("No Such Employee Id And Name is Present In Database.")
                print("----------------------------------------------------")
            print("=====================================")
            print()
        elif ch == "4":
            # Employees list
            print()
            print("====================================================")
            print("Employees list")
            q1 = "select * from employee_data;"
            res = read_query(cd, q1)
            if res == []:
                print("------------")
                print("No Data")
                print("------------")
            else:
                print("-------------------------------------------")
                print("Emp_id,Name,age,addr,ph_no,Sal_pm,DOJ")
                print("-------------------------------------------")
                for i in res:
                    print(i)
            print("====================================================")
            print()
        elif ch == "5":
            print()
            print("=======================================")
            emp_id = input("Enter Your Employee ID : ").capitalize()
            name = input("Enter Your Name : ").capitalize()
            q1 = f"""select doj from employee_data where emp_id="{emp_id}" && name="{name}";"""
            res = read_query(cd, q1)
            if res == []:
                print("Not Data Present..")
            else:
                # dat_now
                x = x[0]
                x = x.split("-")
                x = int(x[0])
                # date of joining
                doj = res[0][0]
                doj = doj.split("-")
                doj = int(doj[0])
                # check
                print("--------------------")
                if x-doj == 0:
                    print("Newely Joined.")
                elif x-doj == 5:
                    print("Beigneer")
                elif x-doj == 10:
                    print("Experienced")
                elif x-doj == 20:
                    print("Professional")
                print("--------------------")
            print("=======================================")
            print()
        elif ch == "6":
            # Know your salary
            print()
            print("====================================================")
            emp_id = input("Enter Your Employee ID : ").capitalize()
            name = input("Enter Your Name : ").capitalize()
            q1 = f"""select sal_pm from employee_data where emp_id="{emp_id}" && name="{name}";"""
            res = read_query(cd, q1)
            if res == []:
                print("------------")
                print("No Data")
                print("------------")
            else:
                print("---------------------------------------------------")
                print(f"Your Salary is {res[0][0]}")
                print("---------------------------------------------------")
            print("====================================================")
            print()
        elif ch == "7":
            break
        else:
            print("Invalid Syntax!!")
else:
    print("Try Again")
