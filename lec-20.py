#This is lecture no 20
#break,continue and Pass in for loop
#break
'''
x=int(input("Enter the no of candy's you want"))
avail=10
i=1
while i<=x:
    if(x>avail):
        print("Not available")
        break
    print("Candy's")
    i+=1

print("Bye")

'''
#continue
'''
for i in range(20):
    if i%3==0 and i%5==0:
        continue
    print(i)
print("Bye")

'''
#Pass-->Basically if me jb hm kuch ni likhte hai toh python me pass likh dete hai.

for i in range(30):
    if i%2!=0:
        pass
    else:
        if i==0:
            pass
        else:
            print(i)
print("Bye")
