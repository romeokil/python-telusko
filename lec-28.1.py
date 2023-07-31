#Inheritance in oops in pyhton 
#This is single level inheritance
class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B(A): #Here we are passing the class A i.e doing inheritance
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")


print("Accessing the features from object a")
a=A()
a.feature1()
a.feature2()

print("Accessing the features from object b")
b=B()
b.feature3()
b.feature4()
b.feature1()   #That y we are able to access the feature2 and feature1
b.feature2()   #Otherwise we are not able to access.