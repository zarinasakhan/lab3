def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]==3:
            return True
    return False
       
nums=[]
length=int(input("enter length:"))
for i in range(length):
    x=int(input("enter elem: "))
    nums.append(x)
print(has_33(nums))