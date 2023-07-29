#Datatype in Python
#None Numeric List Tuple Set String Range Dictionary
#jo layk other languages me null rehta hai usko ye log none bolte hai.
#Numeric-->int float complex bool
a=9
print(type(a))
b=5.7
print(type(b))
c=7+6j #complex lekin isme i,k ni likh skte hai j likh skte hai.
print(type(c))
d=6>5
print(type(d))
e=int(d)#datatype conversion 
print(e)
print(type(e))
u=complex(a)#datatype converison
print(type(u))
print(u)
#Sequence ->List Tuple Set String Range 
l=[45,55,67,53,23,89]#list
print(l)
print(type(l))
s={34,67,89,23,25,67}#set
print(s)
print(type(s))
t=(3,5,6,2,5,9)      #tuple
print(t)
print(type(t))
st='a'               #string
print(st)
print(type(st))
#range
print(list(range(10)))#Ye 
print(list(range(2,10,2)))#Ye bhi teen parameters leta hai.
d={'shashank':'iphone','rahul':'samsung','abhishek':'micromax'} #range
print(d.get('shashank')) #Isko normal braces use kr rhe hai.
print(d['abhishek']) #Isko hmko array ka format rkhna pda.

