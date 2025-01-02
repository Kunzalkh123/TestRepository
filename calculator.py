def calculator(a,b,operation):
   if operation == "add":
     return a+b
   elif operation == "subtract":
      return a-b
   elif operation == "multiply":
      return a*b
   elif operation == "divide":
      return a/b if b !=0 else "division by zero"
   else:
      return "invalid operation"
   
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))

operator = input("Enter an operator(add,subtract,multiply,divide):").lower()

result = calculator(a,b,operator)
print("Results:",result)
