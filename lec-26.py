#This is lecture 26 Types of methods in python
#Instance method,Static method,Class method
#Getter and Setter are called accessors(it will not modify the value) and mutators(modify the value)

class Student:

    School="Rahulmania"     #Class Variable

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod          #class method eska argument me bhi class hi bhejte hai
    def getSchool(cls):
        return cls.School
    
    @staticmethod         #static method ka argument khaaali hota hai or yhi iska pehchaan hai
    def print():
        print("This is print method of static method")


s1=Student(22,33,44)
s2=Student(33,77,55)

print("Average of student 1 is",s1.avg())
print("Average of student 2 is",s2.avg())

print("School Name is ",Student.getSchool())  #Class method ke liye tmko class ke naam se call krna pdega

s1.print()                #Calling of an static function
s2.print()

