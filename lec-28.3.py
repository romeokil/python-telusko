#Inheritance in oops in pyhton 
#This is multiple inheritance
class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B(): 
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")

class C(A,B):#Inherting from 2 super class A,B
    def feature5(self):
        print("This is feature 5")

print("Accessing the features from object a")
a=A()
a.feature1()
a.feature2()

print("Accessing the features from object b")
b=B()
b.feature3()
b.feature4()

print("Accessing the features from object c")
c=C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()