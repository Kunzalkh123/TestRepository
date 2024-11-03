fruits = ["apple","mango","stawberry","pineapple","watermelon"] 
print(fruits) 

colors = ['red','blue','green','yellow','purple']
print(colors[0], colors[2], colors[4]) 

numbers=[10,20,30,40,50] 
print(numbers)
numbers.insert(1,25)
numbers.append(60)
print(numbers) 


names=['Alice','Bob','Charlie','David','Emma'] 
subset= names[0:3] 
print(subset) 

numbers=[1,2,3,4,5,6,7,8,9,10] 
for i in numbers: 
    print("The square of",i,"is",i*i) 

shopping_cart=[] 
shopping_cart.append('milk') 
shopping_cart.append('bread') 
shopping_cart.append('eggs')
shopping_cart1=['butter','cheese'] 
shopping_cart.extend(shopping_cart1) 
print(shopping_cart) 

numbers = [45,22,88,56,92,33] 
print("Maximum value:",max(numbers)) 
print("Minimum Value:",min(numbers)) 

letters=['a','b','a','c','b','a','d'] 
count_of_a=letters.count('a') 
print("Count of a:",count_of_a) 

even_squares=[i**2 for i in range(0,11,2)] 
print("The squares of even numbers from 1 to 10 are",even_squares) 

nums=[1,2,2,3,4,4,5,6,6,7] 
nums= list(dict.fromkeys(nums)) 
print(nums) 