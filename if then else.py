age=int(input("Enter your age: "))

if age >=18:
    print("you are an adult.")
else:
    print("you are not an adult. ")

marks=int(input("Enter your marks: "))
if marks >= 90:
    print("GRADE: A")
elif marks >= 75:
    print("GRADE: B")
elif marks >= 60:
     print("GRADE: C")
else:
     print("GRADE: F")

number=int(input("Enter a number: "))
if number % 2== 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
