#This is lecture 28.5.py
'''
Basically isse pehle single level inheritance tha toh hmlog super method bolke init method ko call kr le rhe the but  kyuki ek hi parent/super class tha ab agr multilevel inheritance ho gy tb kiska init call krega toh yaad rkhna  
ki hmesha left to right jaata hai mtlb jo left me likha hua hai usko call krege code me dikhaate hai

'''
class A:
    def __init__(self):
        print("This is init method of class A")

    def feature1(self):
        print("This is feature1 of class A")

class B:
    def __init__(self):
        print("This is init method of class B")

    def feature1(self):
        print("This is feature1 of class B")
    
class C(A,B):
    def __init__(self):
        super().__init__()   #Dekh hm call kiye init method ko but wo class A ka hua.
        super().feature1()  #Dekh normal method me bhi yhi chiz applicable hai feature1 bhi classA ka call hoga
        print("This is init method of Class C")

c=C()
