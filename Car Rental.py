

import csv
from operator import mod
from secrets import choice #?
import time # Delay of 1, yet to do
import getpass #for password/login
filename=open('Car data.csv','r') #File type for car dataset
file=csv.DictReader(filename)
type(file)

#5 lists for each data
brand=[],
model=[],
transmission=[],
fuel=[],
price_per_day=[]
path= ('r','C:\\Users\\Aaditya\\Desktop\\Kjsce\\Python Programming\\Car Rental Project Folder\\Car data.csv')#path will have to be changed for device
#Device specific path

brand=list(brand) #converted tuple to list
model=list(model)
transmission=list(transmission)
fuel=list(fuel)
price_per_day=list(price_per_day)
choice

with open('Car data.csv', 'rb') as csvfile: #To access CSV dataset
    for col in file:
        brand.append(col["Brand"]) 
        model.append(col["Model"])  
        transmission.append(col["Transmission"])
        fuel.append(col["Fuel"])
        price_per_day.append(col["Cost"])
    
    brand,model,transmission,fuel,price_per_day=(list(t) for t in zip(*sorted(zip(brand,model,transmission,fuel,price_per_day))))

class menu:
    def __init__(self,user_type):
        self.user_type=user_type
    def dis(self): #display function
        global user_type
        print("\tWELCOME to Online Car Rental Service!\n")
        print("\tEnter which type of user are you?:\n  1. Agency Operator/Employee\t2. Customer")
        n=int(input())
        if n==1:
            user_type="Operator"
        elif n==2:
            user_type="Customer"
        else:
            print("Sorry, Wrong input!")
            SystemExit #it will stop running.
        
        return user_type

class customer(menu): #derived from menu class
    def __init__(self,user_type):
        super().__init__(user_type) # to access user_type variable from parent menu class
        global choice
        print("\nDisplaying Car Inventory:\n")
        print("Car Brand\tModel Name\tTransmission\tFuel\tRate per day")
        l=len(brand)
        for i in range(1,l+1): # for loop starts from 1 till l+1 to exlude the titles of columns
            print(i,"\t",brand[i],"\t",model[i],"\t",transmission[i],"\t",fuel[i],"\t",price_per_day[i])  
        choice=int(input("Enter your choice number"))
    
class bill(menu): #derived from menu class
    days=int(input("Enter the number of days you want to rent the car for:  (Valid range is between 1 to 60)\n"))
    if days>=1 and days<=5:
        rate=price_per_day[choice]
        cost=rate*days
    elif days>=6 and days<=10:
        rate=0.85*price_per_day[choice]
        cost=rate*days
    elif days>=11 and days <=15:
        rate=0.7*price_per_day[choice]
        cost=rate*days
    elif days>=16 and days<=60:
        rate=0.5*price_per_day[choice]
        cost=rate*days
    else:
        print("Invalid Input")
        SystemExit
    print("Confirm Selection:")
    print("You have chosen ",brand[choice],model[choice],", with ",transmission[choice]," transmission choice and ",fuel[choice]," fuel, at the rate of Rs. ",price_per_day[choice]," per day") #change the rate
    print("Thus Resulting in Total Bill of Rs. %0.2f" %cost)
    #Thank you screen

class employee(menu): #derived from menu class
    def __init__(self,user_type):
        super().__init__(user_type)
        print("Agency Operator/Employee Page Display:")
        pwd=getpass.getpass(prompt="Enter password to login: ") #password and login
        if pwd=="BossGuy":
            print("Successful Login:")
            print(" 1. Add Vehicle\t2. Delete Vehicle\t3. Update Rates")
            n=int(input())
            if n==1:
                brand1=input("Enter the brand")
                model1=input("Enter the model")
                transmission1=input("Enter the kind of transmission")
                fuel1=input("Enter the type of fuel")
                price_per_day1=input("Enter the price per day")
                brand.append(brand1)
                model.append(model1) 
                transmission.append(transmission1)
                fuel.append(fuel1)
                price_per_day.append(price_per_day1)
                brand,model,transmission,fuel,price_per_day=(list(t) for t in zip(*sorted(zip(brand,model,transmission,fuel,price_per_day))))
                print("Displaying the updated inventory:")
                print("Car Brand\tModel Name\tTransmission\tFuel\tRate per day")
                l=len(brand)
                for i in range(1,l+1): # for loop starts from 1 till l+1 to exlude the titles of columns
                    print(i,"\t",brand[i],"\t",model[i],"\t",transmission[i],"\t",fuel[i],"\t",price_per_day[i])  
                
            elif n==2:
                #Show entire inventory just like Line 114
                #Ask user which car number he wants to delete
                #Remove that Vehicle (remove brand, model, transmisison, fuel, price_per_day)
                #Display the new inventory just like line 114
                l=len(brand)
                for i in range(1,l+1): # for loop starts from 1 till l+1 to exlude the titles of columns
                    print(i,"\t",brand[i],"\t",model[i],"\t",transmission[i],"\t",fuel[i],"\t",price_per_day[i])                 
                n=int(input("Enter the number of the car you wish to remove: "))
                del brand[n]
                del model[n]
                del transmission[n]
                del fuel[n]
                del price_per_day[n]
                print("Displaying the updated inventory:")
                print("Car Brand\tModel Name\tTransmission\tFuel\tRate per day") 
                for i in range(1,l+1): # for loop starts from 1 till l+1 to exlude the titles of columns
                    print(i,"\t",brand[i],"\t",model[i],"\t",transmission[i],"\t",fuel[i],"\t",price_per_day[i])                 
            elif n==3:
                #Show entire inventory just like Line 114
                #Ask user (accept number) which number car he wants to modify
                #Display that specific car details like: Brand,, Model, Current Rate
                #Ask user what is new rate
                #price_per_day[index]=new rate just taken input from user
                #Display the entire inventory
                l=len(brand)
                for i in range(1,l+1): # for loop starts from 1 till l+1 to exlude the titles of columns
                    print(i,"\t",brand[i],"\t",model[i],"\t",transmission[i],"\t",fuel[i],"\t",price_per_day[i]) 
                ir=int(input("Enter the number of the car who's rate you want to modify: "))
                fr=int(input("Enter the new rate for the selected car: "))
                price_per_day[ir]=fr
                
            
        else:
            print("Wrong Credentials!")
            SystemExit
         
