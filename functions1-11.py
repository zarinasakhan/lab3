def palindrome(word):
    if word==word[::-1]:
        return True
    return False
x=input("enter a word: ")
print(palindrome(x))