student = {
    "Name": "Alice",
    "Age": 24,
    "Major": "Computer Science"
}

print("Name:", student["Name"])
print("Major:", student["Major"])

student["GPA"] = 3.8

student["Age"] = 25

print(student)

for key, value in student.items():
    print(f"{key}: {value}")

def check_key(dictionary, key):
    if key in dictionary:
        return "Key exists"
    else:
        return "Key does not exist"

print(check_key(student, "Name"))  
print(check_key(student, "Hobbies")) 

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)

student.pop("Age", None)  

print(student)

classroom = {
    "Student1": {"Name": "John", "Age": 20},
    "Student2": {"Name": "Emma", "Age": 22}
}

print("Student2 Name:", classroom["Student2"]["Name"])
print("Student1 Age:", classroom["Student1"]["Age"])

squares = {x: x**2 for x in range(1, 6)}
print(squares)
