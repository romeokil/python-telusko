#This is lecture no 23 oops in python
#making of classes and object

class Computer:
    def config(self):
        print("1TB Hard Disk")


class Area:
    def findarea(self,l,b):
        area=l*b
        return area

comp1=Computer()   #Making of an object
comp1.config()     #Callng function with the help of object

area1=Area()       
x=area1.findarea(2,3)
print(x)