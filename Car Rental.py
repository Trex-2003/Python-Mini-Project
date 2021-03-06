import getpass
import csv
import time

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
            customer_menu()
        
        elif user_input=='0':
            index=0
            SystemExit
        
        else:
            print("\nInvalid Input...\n")
            main_menu()


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
        del_car()

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
            print("Number should be 10 characters long!")
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
            print("Transmission: {0}".format(car_transmission.upper()))
            print("Fuel: {0}".format(car_fuel.upper()))
            print("Price Per Day: Rs. {0}".format(car_price_per_day))
            print("Number Plate: {0}".format(car_numberPlate.upper()))

            save_YN=input("Confirm if you want to save this record with 'Y' or discard with 'N':  ")
            if save_YN.upper()=='Y':
                last_seqno=int(last_seqno)+1
                carslist=open("C:\\Users\\Aaditya\\Desktop\\Kjsce\\Python Programming\\Car Rental Project Folder\\cars_list.txt","a")
                carslist.write("\n"+str(last_seqno)+","+ car_brand.upper() + ","+car_model.upper()+","+ car_transmission.upper()+","+car_fuel.upper()+"," +car_numberPlate.upper()+","+ car_price_per_day)
                
                carslist.close()
                print("Car Added Successfully\n")
            else:
                print("Record Not Saved as User cancelled the command")
    employee_menu()
def del_car():
    
    carslist=load_carlist()
    #del_index
    for i in range(len(carslist)):
        #seq=i
        car_id=carslist[i][0]
        brand=carslist[i][1]
        model=carslist[i][2]
        fuel=carslist[i][4]
        trm=carslist[i][3]
        price=carslist[i][5]
        plate=carslist[i][6]

        if i!=0:    #Since we do not want to print the 1st row:
            print(car_id,"\t",brand,"\t",model,"\t",trm,"\t",fuel,"\t",price,"\t",plate,"\n")
    
    del_index=int(input("\nEnter the Car ID which you want to delete: "))
    while(del_index<0 or del_index>len(carslist)):
        print("Invalid input, loading employee menu...\n")
        employee_menu()
        break
    
    print("Car Selected: {0} - {1}".format(carslist[del_index][1],carslist[del_index][2]))
    user_IN=input("Enter 'Y' if you want to delete this car entry from record: ")
    while(user_IN.upper()!='Y'):
        print("Taking back to Employee menu...")
        employee_menu()
    if user_IN.upper()=='Y':
        f=open("C:\\Users\\Aaditya\\Desktop\\Kjsce\\Python Programming\\Car Rental Project Folder\\cars_list.txt","a+")
        # for i in range(len(carslist)):
        #     seq=i
        #     carslist_str=str(carslist[i])
        #     carslist_str=carslist_str.replace('[','')
        #     carslist_str=carslist_str.replace(']','')
        #     carslist_str=carslist_str.replace("'",'')
        #     carslist_str=carslist_str.replace(' ','')
        # del carslist[del_index]
        carslist.pop(del_index)
        print("Entry successfully Deleted...")
        time.sleep(0.5)
        print("Updated Inventory:\n")
        print("Car ID Brand\tModel\tFuel\tTransmission\tPrice Per Day (Rs)  Number Plate:")
        for i in range(len(carslist)):
            #if  i<del_index:
            car_id=carslist[i][0]
            brand=carslist[i][1]
            model=carslist[i][2]
            fuel=carslist[i][4]
            trm=carslist[i][3]
            price=carslist[i][5]
            plate=carslist[i][6]
            # elif i==del_index:
            #     continue
            # elif i>del_index:
            #     carslist[i][0]=int(carslist[i][0])-1
                
            if i!=0:    #Since we do not want to print the 1st row:
                print(car_id,"\t",brand,"\t",model,"\t",trm,"\t",fuel,"\t",price,"\t",plate,"\n")
            
            f.close()




def modify_car():
    brand2=" "
    model2=" "
    fuel2=" "
    trm2=" "
    price2=" "
    plate2=" "
    save_YN="N"

    carslist=load_carlist()
    print("Car ID Brand\tModel\tFuel\tTransmission\tPrice Per Day (Rs)  Number Plate:")
    for i in range(len(carslist)):
        car_id=carslist[i][0]
        brand=carslist[i][1]
        model=carslist[i][2]
        fuel=carslist[i][4]
        trm=carslist[i][3]
        price=carslist[i][5]
        plate=carslist[i][6]

        if i!=0:    #Since we do not want to print the 1st row:
            print(car_id,"\t",brand,"\t",model,"\t",trm,"\t",fuel,"\t",price,"\t",plate,"\n")
    
    car_id=input("Enter the Car ID number which you wish to modify: ")

    for i in range(len(carslist)):
        if carslist[i][0]==car_id:
            list_row_no=i
            brand=carslist[i][1]
            model=carslist[i][2]
            fuel=carslist[i][4]
            trm=carslist[i][3]
            price=carslist[i][5]
            plate=carslist[i][6]

            print("Car ID: {0}".format(car_id))
            print("Brand: {0}".format(brand.upper()))
            brand2=input("Enter brand: ")
            print("Model: {0}".format(model.upper()))
            model2=input("Enter Model: ")
            print("Transmission: {0}".format(trm.upper()))
            trm2=input("Enter transmission: ")
            print("Fuel: {0}".format(fuel.upper()))
            fuel2=input("Enter fuel: ")
            print("Price Per Day: Rs. {0}".format(price))
            price2=input("Enter cost per day in Rs.: ")
            print("Number Plate: {0}".format(plate.upper()))
            plate2=input("Enter number plate: ")

            if brand2!="": #this means if <user entered enter key>
                brand=brand2.upper()
            if model2!="":
                model=model2.upper()
            if fuel2!="":
                fuel=fuel2.upper()
            if trm2!="":
                trm=trm2.upper()
            if price2!="":
                price=price2
            if plate2!="":
                plate=plate2
            print("\nShowing UPDATED details of the car:\n")
            print("Car ID: {0}".format(car_id))
            print("Brand: {0}".format(brand.upper()))
            print("Model: {0}".format(model.upper()))
            print("Transmission: {0}".format(trm.upper()))
            print("Fuel: {0}".format(fuel.upper()))
            print("Price Per Day: Rs. {0}".format(price))
            print("Number Plate: {0}".format(plate.upper()))

            save_YN=input("\nConfirm if you want to save this record with 'Y' or discard with 'N':  ")
    if save_YN.upper()=='Y':
        carslist[list_row_no][1]=brand
        carslist[list_row_no][2]=model
        carslist[list_row_no][4]=fuel
        carslist[list_row_no][3]=trm
        carslist[list_row_no][5]=price
        carslist[list_row_no][6]=plate

        f=open("C:\\Users\\Aaditya\\Desktop\\Kjsce\\Python Programming\\Car Rental Project Folder\\cars_list.txt","w")
        for i in range(len(carslist)):
            carslist_str=str(carslist[i])
            carslist_str=carslist_str.replace('[','')
            carslist_str=carslist_str.replace(']','')
            carslist_str=carslist_str.replace("'",'')
            carslist_str=carslist_str.replace(' ','')

            if i==0:    #NOT adding new line for first line
                f.write(carslist_str)
                print()
            else:
                f.write("\n"+carslist_str)
                print()
        
        f.close()

        print("Record saved Successfully.")
    else:
        print("Record Not Saved as User cancelled the command")
        employee_menu()

    pressreturn=input("Press Enter to return to previous menu...")
    employee_menu()

def load_carlist():
    r=csv.reader(open("C:\\Users\\Aaditya\\Desktop\\Kjsce\\Python Programming\\Car Rental Project Folder\\cars_list.txt"))
    lines=list(r) #list of lists
    return lines

def check_carPlates_fn(mycarlist,mycarplate):
    plate_existYN=False

    for i in range(len(mycarlist)):
        car_id=mycarlist[i][0]
        
        if mycarlist[1][6]==plate_existYN:
            plate_existYN=True
    
    return plate_existYN,car_id


def customer_menu():
    save_YN="N"
    days=1
    print("**Customer Menu**")
    print("\nSelect a vehicle:")
    print("Displaying Car Inventory\n")
    carslist=load_carlist()
    time.sleep(1)
    print("Car ID Brand\tModel\tFuel\tTransmission\tPrice Per Day (Rs)  Number Plate:")
    i=0
    for i in range(len(carslist)):
        car_id=carslist[i][0]
        brand=carslist[i][1]
        model=carslist[i][2]
        fuel=carslist[i][4]
        trm=carslist[i][3]
        price=carslist[i][5]
        plate=carslist[i][6]
        
        if i!=0:    #Since we do not want to print the 1st row:
            print(car_id,"\t",brand,"\t",model,"\t",trm,"\t",fuel,"\t",price,"\t",plate,"\n")
        # print("Car ID: {0}".format(car_id))
        # print("Brand: {0}".format(brand.upper()))
        # print("Model: {0}".format(model.upper()))
        # print("Transmission: {0}".format(trm.upper()))
        # print("Fuel: {0}".format(fuel.upper()))
        # print("Price Per Day: Rs. {0}".format(price))
        # print("Number Plate: {0}".format(plate.upper()))
    
    car_choice=int(input("Enter the Car ID number which you wish to Rent/Hire: "))

    print("Car Selected: {0} - {1}".format(carslist[car_choice][1],carslist[car_choice][2]))
    user_IN=input("Enter 'Y' if interested in renting this car: ")
    while(user_IN.upper()!='Y'):
        print("Taking back to main menu...")
        main_menu()
    if user_IN.upper()=='Y':
        days=int(input("\nEnter Number of days for which you want to rent car: "))
        while(days<1 or days>45):
            print("\nInvalid Range, taking you back to Customer Menu...\n")
            time.sleep(0.75)
            customer_menu()
        bill(days,car_choice)
    SystemExit
            
def bill(days,car_choice_in):
    final_bill=0
    slab=0
    carslist=load_carlist()
    for i in range(len(carslist)):
        car_id=carslist[i][0]
        brand=carslist[i][1]
        model=carslist[i][2]
        fuel=carslist[i][4]
        trm=carslist[i][3]
        price=carslist[i][5]
        plate=carslist[i][6]
    # print(carslist)
    # print(car_choice_in)
    # print(carslist[car_choice_in])

    if days<=10:
        a=int(carslist[car_choice_in][5])
        final_bill=days*(a)
        slab=0
    elif days>10 and days<=20:
        a=int(carslist[car_choice_in][5])
        final_bill=days*0.85*a
        slab=15
    elif days>20 and days<=45:
        a=int(carslist[car_choice_in][5])
        final_bill=days*0.75*a
        slab=25
    
    cust_Name=input("Enter your Name:  ")
    
    brandOut=carslist[car_choice_in][1].upper()
    modelOut=carslist[car_choice_in][2].upper()
    trmOut=carslist[car_choice_in][3].upper()
    fuelOut=carslist[car_choice_in][4].upper()
    #format((carslist[car_choice_in][1]).upper(),(carslist[car_choice_in][2]).upper())
    #carslist[car_choice_in][3].upper())

    print("\n\n**BILL**\n")
    print("Customer Name: ",cust_Name)
    print("Car Brand and Model: {0} - {1}".format(brandOut,modelOut))
    print("Transmission: {0}".format(trmOut))
    print("Fuel Type: {0}".format(fuelOut))
    print("Number of days: {0}".format(days))
    print("Amount to be paid after %.2f" %slab ," percent discount: Rs. %.2f" %final_bill)
    time.sleep(0.5)
    print("Taking back to main menu...")
    time.sleep(2)
    #print("Time: ",time.gmtime)
    
    print("\n**THANK YOU**")
main_menu()
