import getpass
import csv

from pip import main
def main_menu():
    index='1'
    while index=='1':
        print("**CAR RENTAL SERVICE**")
        print("\nSelect an option:")
        print("1 = Employee Login")
        print("2 = Customer Login")
        print("0 = Exit")
        user_input=input("Enter the option number: ")
        if user_input=='1':
            password=getpass.getpass(prompt="Enter the password: ")
            if password=="TrustMe":
                employee_menu()
            else:
                print("Wrong Password")
                opt=input("Press any key to go back to main menu\n")
                #index-=1
                main_menu() #check once
        
        elif user_input=='2':
            pass
            #customer_menu()
        
        elif user_input=='0':
            index=0
        
        else:
            print("\nInvalid Input...\n")


def employee_menu():
    print("**Employee Menu**")
    print("\nSelect an option:")
    print("1 = Add Car")
    print("2 = Modify Car")
    print("3 = Delete Car")
    print("4 = Return to Main Menu")

    emp_input=input("Enter an option: ")
    while (emp_input!='1' and emp_input!='2' and emp_input!='3' and emp_input!='4'):
        print("Invalid Input, select again...")
        employee_menu()
    
    if emp_input=='1':
        add_car()
    
    elif emp_input=='2':
        modify_car()

    elif emp_input=='3':
        pass#del_car()

    elif emp_input=='4':
        main_menu()
    

def add_car():
    #r=csv.reader(open("C:\\Users\\Aaditya\\Desktop\\Kjsce\\Python Programming\\Car Rental Project Folder\\cars_list.txt"))

    car_numberPlate_exists=False

    index=0
    print("\nAdd Car Entry\n")
    car_brand=input("Car Brand: ")
    car_model=input("Car Model: ")
    car_fuel=input("Car Fuel: ")
    car_transmission=input("Transmission: ")
    car_numberPlate=input("No. Plate: ")
    car_price_per_day=input("Rate per day: ")

    carslist=load_carlist()

    if car_numberPlate!="":
        car_numberPlate=car_numberPlate.upper()
        check_carPlates=check_carPlates_fn(carslist,car_numberPlate)
        car_numberPlate_exists=check_carPlates[0]
        last_seqno=check_carPlates[1]

        if car_numberPlate_exists:
            print("Not Valid as number is already taken.")
            employee_menu()
    
    if  not car_numberPlate_exists:
        print()
        if len(car_numberPlate)!=10:
            print("Number should be 8 characters long!")
            index+=1
        if not car_price_per_day.isnumeric():
            print("Price must be in numbers!")
            index+=1
        
        if index!=0:
            print("The detail(s) are invalid, please try again!")
            employee_menu()
        else:
            print("\n\nDetails of the Car.\n")
            print("Brand: {0}".format(car_brand.upper()))
            print("Model: {0}".format(car_model.upper()))
            print("Fuel: {0}".format(car_fuel.upper()))
            print("Transmission: {0}".format(car_transmission.upper()))
            print("Price Per Day: Rs. {0}".format(car_price_per_day))
            print("Number Plate: {0}".format(car_numberPlate.upper()))

            save_YN=input("Confirm if you want to save this record with 'Y' or discard with 'N':  ")
            if save_YN.upper()=='Y':
                last_seqno=int(last_seqno)+1
                carslist=open("C:\\Users\\Aaditya\\Desktop\\Kjsce\\Python Programming\\Car Rental Project Folder\\cars_list.txt","a")
                carslist.write("\n"+str(last_seqno)+","+ car_brand.upper() + ","+car_model.upper()+","+ car_fuel.upper()+ ","+ car_transmission.upper() +car_numberPlate.upper()+","+ car_price_per_day)
                
                carslist.close()
                print("Car Added Successfully\n")
            else:
                print("Record Not Saved as User cancelled the command")
    employee_menu()

def modify_car():
    pass

def load_carlist():
    r=csv.reader(open("C:\\Users\\Aaditya\\Desktop\\Kjsce\\Python Programming\\Car Rental Project Folder\\cars_list.txt"))
    lines=list(r)
    return lines

def check_carPlates_fn(mycarlist,mycarplate):
    plate_existYN=False

    for i in range(len(mycarlist)):
        car_id=mycarlist[i][0]
        
        if mycarlist[1][6]==plate_existYN:
            plate_existYN=True
    
    return plate_existYN,car_id

main_menu()
