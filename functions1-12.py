def histogram(mylist):
    for elem in mylist:
        print("*"*elem)

mylist=[]
length=int(input("enter length:"))
for i in range(length):
    x=int(input("enter elem: "))
    mylist.append(x)
histogram(mylist)