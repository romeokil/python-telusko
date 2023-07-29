#Lists in Python.
#List is mutable.
nums=[10,20,30,40,50]
names=['Rahul','Navin','Abhishek']
mil=[nums,names]#Array bol skte hai or esme list of numbers and list of strings ko combine kr skte hai.*
print(mil)
#Inserting values-append and insert
nums.append(44)#append hmesha last me hi hota hai.
print(nums)
nums.insert(3,55)
print(nums)#insert me desired value daal skte hai jaha bhi jae.
#Deleting values-pop and remove
nums.remove(55)#remove me sirf value dena hai jisko hatana hai.
print(nums)
nums.pop(2)#pop me index no daal ke element ko delete kr skte hai.
print(nums)
#Deleting multiple values at a time.
del nums[3:]
print(nums)
#Adding multiple values at a time.->extend
nums.extend([44,67,78,34])
print(nums)
#We can find sum,min,max,sort,len
print(max(nums))
print(min(nums))
print(sum(nums))
print(len(nums))
nums.sort()
print(nums)



