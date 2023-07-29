#More on Variables.
#Agr tm isme dekho toh variables mutable hai values aaram se change kr skte hai. 
a=10
b=a
k=10
#id address which is pointing to and you can see all are pointing to the same memory location
print(id(a))
print(id(b))
print(id(k))
a=9#When we change the value of a the address it is pointing to is also changed.
print(a)
b=9.4
print(id(a))
print(type(a))
print(type(b))
