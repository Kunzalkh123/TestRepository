lists_of_sproducts= {
"A1":("Oil,48"),
"A2":("apples,18"), 
"A3":("detergent,89"), 
"A4":("bananas,10"),
"A5":("mango,15"),
"A6":("chocolate,39"),
"A7":("juice,12"), 
"A8":("water,1"), 
"A9":("pinnaple,16"),
"A10":("biscuits,17"),
"A11":("pear,30"), 
"A12":("watermelon,13"),
"A13":("chips,6"),
"A14":("custurd,9"), 
"A15":("candy,37"),
                    }
def display():
      print("lists_of_sproducts:")
for code, (name,price) in lists_of_sproducts():
      print(f"{code}: {name} - ${price:.2f}")

display()
