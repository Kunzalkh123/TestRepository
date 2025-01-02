student = {
    "name": "Alice",
    "age":20,
    "courses":["Maths","Physics"]
}
print(student)

student_info = {
    "name": "Bob",
    "age":21,
    "major":["computer science"]
}
print(student_info)

student_infor2 = dict(name="Emma",age=22,major="Biology")
print(student_infor2)

student = {
    "name": "Charlie",
    "age": 19,
    "major": "Physics"
}
print(student["name"])
print(student.get("GPA", "Not Available"))

student = {
    "name": "Dave",
    "age": 20,
    "major": "Chemistry"
}

student["GPA"] = 3.8

student["age"] = 21

student.pop("major")

print(student)

student = {
    "name": "Eve",
    "age": 22,
    "major": "Biology"
}
print(student.keys())    
print(student.values())  
print(student.items()) 

for key, value in student.items():
    print(f"{key}:{value}")

if "GPA" in student:
    print("GPA is:", student["GPA"])
else:
    print("GPA key not found")

