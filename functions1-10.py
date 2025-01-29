def unique(mylist):
    new_list=[]
    for elem in mylist:
        if elem not in new_list:
            new_list.append(elem)
    return new_list

mylist=[]
length=int(input("enter length:"))
for i in range(length):
    x=(input("enter elem: "))
    mylist.append(x)
print(unique(mylist))