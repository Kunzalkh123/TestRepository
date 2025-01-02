for i in range(1, 11):
    print(i)

total = 0
for i in range(1, 6):
    total += i
print("Sum:", total)

text = input("Enter a string: ")
for char in text:
    print(char)

number = int(input("Enter a number: "))
while number >= 0:
    print(number)
    number -= 1

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

for i in range (1,11):
    print(i)

import random
target = random.randint(1, 50)
guess = None
while guess != target:
    guess = int(input("Guess a number between 1 and 50: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
print("Correct! You guessed the number.")

num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

num = int(input("Enter a positive integer: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")

num = int (input ("Enter a number:") )
for i in range(1,11):
    print(f"{num} x {i}=(num * i)")

for i in range(1,15,2):
    print(i)
