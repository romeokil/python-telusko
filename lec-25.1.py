#This lecture 25.1 consist of variables in python 
#Class variables(static variables) and instance variables

class Car:
    
    wheels=3  #class variables/static variables or ye shared ho rha hai dono me 

    def __init__(self):
        self.com="BMW"   #instance variables 
        self.mil=10

c1=Car()
c2=Car()
print("Company and mileage of Car1",c1.com,c1.mil,c1.wheels)
print("Company and mileage of Car1",c2.com,c2.mil,c2.wheels)

