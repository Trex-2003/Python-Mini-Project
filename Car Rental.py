import csv
import time
import getpass
filename=open('Car data.csv','r')
file=csv.DictReader(filename)
type(file)

brand=[],
model=[],
transmission=[],
fuel=[],
price_per_day=[]
path= ('r','C:\\Users\\Aaditya\\Desktop\\Kjsce\\Python Programming\\Car Rental Project Folder\\Car data.csv')
print(path)

brand=list(brand)
model=list(model)
transmission=list(transmission)
fuel=list(fuel)
price_per_day=list(price_per_day)

with open('Car data.csv', 'rb') as csvfile:
    for col in file:
        brand.append(col["Brand"])
        model.append(col["Model"])  
        transmission.append(col["Transmission"])
        fuel.append(col["Fuel"])
        price_per_day.append(col["Cost"])


class menu:
    def __init__(self,user_type):
        self.user_type=user_type
    def dis(self):
        global user_type
        print("\tWELCOME to Online Car Renta Service!\n")
        print("\tEnter which type of user are you?:\n  1. Agency Operator\t2. Customer")
        n=int(input())
        if n==1:
            user_type="Operator"
        elif n==2:
            user_type="Customer"
        else:
            print("Sorry, Wrong input!")
            SystemExit
        
        return user_type

class customer(menu):
    def __init__(self,user_type,choice):
        super().__init__(user_type)
        self.choice=choice
        print("\nDisplaying Car Inventory:\n")
        print("Car Brand\tModel Name\tTransmission\tFuel\Rate per day or 300km")
        l=len(model)
        for i in range(1,l+1):
            print(i,"\t",model[i],"\t",brand[i],"\t",transmission[i],"\t",fuel[i],"\t",price_per_day[i])  
        choice=int(input("Enter your choice number"))

class operator(menu):
    def __init__(self,user_type):
        super().__init__(user_type)
        print("Agency Operator Page Display:")
        pwd=getpass.getpass(prompt="Enter password to login: ")
        if pwd=="BossGuy":
            print("Successful Login:")
            print(" 1. Add Vehicle\t2. Delete Vehicle\t3. Update Rates")
        else:
            print("Wrong Credentials!")
            SystemExit


