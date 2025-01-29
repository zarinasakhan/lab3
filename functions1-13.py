import random
print("Hello! What is your name?")
name=input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
x=random.randrange(1,20)
guessing=int(input())
count=1
while guessing!=x:
    print("Your guess is too low.")
    print("Take a guess.")
    count+=1
    guessing=int(input())
print(f"Good job, {name}! You guessed my number in {count} guesses!")