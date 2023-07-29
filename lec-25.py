#This is lecture no 25 learn about constructor,self and comparing objects in python
#When we are not writing anything in the class we should write pass
#Objects is created in heap memory all are having the different location identified by id.
'''
class Computer:
    pass

c1=Computer()
print(id(c1))
'''

class Computer:

    def __init__(self):
        self.name='Rahul'
        self.age=34
    
    def compare(self,other):
        if(self.age==other.age):
            return True
        else:
            return False
        
c1=Computer()
c2=Computer()

c2.age=33

if(c1.compare(c2)):
    print("Ages are Same!!")

else:
    print("Ages are Different!!")

