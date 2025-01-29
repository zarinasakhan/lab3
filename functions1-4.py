def filter_prime(mylist):
    x=[elem for elem in mylist if elem>1 and all(elem%i!=0 for i in range(2,elem))]
    return x
mylist=[]
length=int(input("enter length:"))
for i in range(length):
    x=int(input("enter elem: "))
    mylist.append(x)
print(filter_prime(mylist))
