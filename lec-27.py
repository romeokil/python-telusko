#This is lecture no 27 in which we talk about inner class in python

class Student:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()

    def show(self):
        print("Name and Roll No is",self.name,self.roll)

    class Laptop:

        def __init__(self):
            self.brand='DELL'
            self.CPU="i5"
            self.RAM=16

        def show(self):
            print("The configuration of the laptop is",self.brand,self.CPU,self.RAM)


s1=Student('David',10)
s2=Student('Rahul',11)
s1.show()
s2.show()

#Accessing the values in the inner class
#Syntax->Object.variable name in the outer class.value

print(s1.lap.brand)
print(s1.lap.CPU)
print(s1.lap.RAM)


