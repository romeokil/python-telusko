#This is lec-28.4.py
#Constructor in inheritance 
'''
Agr inheritance hai toh toh child class ka object apna constructor ko doondhege ni mila toh super class ka constructor ko call kr dega,agr child class ka constructor hai toh phir super class ka constructor ko ni puchne jaega,but phir bhi agr hm explicitly call krna chahte hai toh super.method/variable ko call kr skta hai

'''
class A:
    def __init__(self):
        print("Constructor of class A called!")

class B(A):
    def __init__(self):
        super().__init__()           #Calling the init method/constructor of B using super must write inside the constructor of class B
        print("Constructor of class B is called!")
b=B()