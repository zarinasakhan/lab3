def reverses(sentence):
    s=''
    x=sentence.split()
    x=x[::-1]
    for elem in x:
        s+=elem
        s+=" "
    return s

sentence=(input("Enter sentence : "))
print(reverses(sentence))