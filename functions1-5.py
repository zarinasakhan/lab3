def permute(s, current=""):
    if len(s) == 0:
        print(current)  
    for i in range(len(s)):
        new_s = s[:i] + s[i+1:]  
        permute(new_s, current + s[i])  
s =input("Enter string: ")
permute(s)
