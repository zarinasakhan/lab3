def solve(numheads, numlegs):
    chickens=((numheads*4)-numlegs)//2
    rabbits=numheads-chickens
    print("chickens are:", chickens, "rabbits are:", rabbits)

x=int(input("enter numheads: "))
y=int(input("enter numlegs: "))
solve(x,y)