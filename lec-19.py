#For loop in Python
x={'62',5.4,'Rahul'}
for i in x:
    print(i)

for i in {56,6.4,"Abhishek"}:
    print(i)

for i in range(10): #It will not include 10 in this and 0 start krta hai
    print(i)

for i in range(3,10,2):#Normal Syntax (Type-1)
    print(i)

for i in range(4,10): #increment condition mandatory ni hai and wo apne aap 1 increment kr de rha hai agr tu ni likha hai toh (Type-2)
    print(i)

for i in range(10):
    if(i%2==0):
        print("Even")
    else:
        print("Odd")