def has_33(nums):
    x=[]
    for elem in nums:
        if elem == 7  or elem == 0:
            x.append(elem)
        if x==[0,0,7]:
            return True
    return False
       
nums=[]
length=int(input("enter length:"))
for i in range(length):
    x=int(input("enter elem: "))
    nums.append(x)
print(has_33(nums))