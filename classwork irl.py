totalamount=int(input("Enter the total bill amount: "))
discount=True

if totalamount> 50:
    if discount:
        print("New total with discount",totalamount+totalamount*10/100)
else:
    print("Total amount:",totalamount)

age=int(input("Enter your age: "))

if age <= 12:
    print("The price is £5")
elif age <=17:
    print("The price is £7")
elif age <=64:
    print("The price is £10")
else:
    print("The price is £6")

amount= float(input())