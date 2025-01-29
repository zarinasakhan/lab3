def volume(radius):
    return (4/3)*radius**3
radius=int(input("Enter radius: "))
print(f"{volume(radius):.3f}π cm^3" )