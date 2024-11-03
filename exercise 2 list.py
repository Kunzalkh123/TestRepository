fruits = ["apple","banana","cherry","date"]
print(fruits)

numbers = [10,20,30,40,50]
print("first element:",numbers[0])
print("last element:",numbers[-1])

animals = ["cats","dog","bird"]
animals[1]="hamster"
print(animals)

colors = []
colors.append("red")
colors.append("green")
colors.append("blue")
colors.remove("green")
print(colors)

names = ["Alice","Bob","Charlie","Diana"]
print("length of the list:",len(names))

numbers = [4,7,1,8,5]
total_sum = sum(numbers)
print("sum of elements:",total_sum)

age = [2,45,18,34,60]
print("maximum age:",max(age))
print("minimum age:",min(age))

scores = [88,56,92,78,61]
scores.sort()
print("sorted list:",scores)

numbers = [1,3,5,7,9]
if 5 in numbers:
    print("found")
else:
    print("not found")

 items = [1,2,2,3,4,4,4,5]
count_of_4 = items.count(4)
print("count of 4:",count_of_4 )

list_1 = [1,2,3,4,5]
list_2 = [6,7,8]
list_1.extend(list_2)
print(list_1)