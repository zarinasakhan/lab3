numbers = []
length=int(input("length: "))
while length>0:
    elem=int(input("elem: "))
    numbers.append(elem)
    length-=1
    
prime_numbers = list(filter(lambda x: x > 1 and all( x % i != 0 for i in range(2, x)), numbers))
print(prime_numbers) 