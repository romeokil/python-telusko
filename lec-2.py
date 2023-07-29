#This lecture is of variables in python
#Isme hmlogo ko datatype define ni krna pdta hai.
x=10 
y=2
#Isme string me number add krne ke liye comma ka use kr skte hai.
print("The sum of",x," and ",y, "is",(x+y))
print(10,"Rahul")

#accessing the particular element in the string.
name='Abhishek'
print(name[3])#isme indexing 0 se start hota hai.
print(name[-3])#esme piche se -1 se count krne lgta hai.
print(name[0:2])#ye 0 ko include krega and 2 ko exclude kr dega.(Type:1)
print(name[1:4])#same as above
print(name[1:])#esme end point ni tha toh pura count kr liya.(Type:2)
print(name[:4])#starting se 4 ko exclude krke saara le liya.(Type:3)
print(name[3:10])#starting se pura le liye qki upper limit toh 10 utna letters bhi ni hai.
#string in python is immutable i.e ek value assign kr diye string me toh change ni kr skte hai not even a character
#Jaise upr hmlog name ka value abhishek diye hai toh ab rahul ni kr skte hai.

##Length of the string is defined as len function
z=len(name)
print("Length of abhishek is",z)

