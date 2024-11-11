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