dict={}
print(type(dict))

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person.keys())
print(person.values())

print(person.get("name"))
print(person.get("work","Not available"))

person["name"]="Ankit" ## updated existing
print(person.get("name"))

person["email"]="abcd@gmail.com" ## added new key and value
print(person)

del person["email"]              # Remove by key
age = person.pop("age")          # Remove and return
person.clear()   


print(person.items())

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})
person.update({"name":"Ankit"})

## Nested dictionaries
student={
    "ankit":{"age":20, "grade":"A"},
    "aman":{"age":21, "grade":"A+"},
    "ankit2":{"age":19, "grade":"B"}
}

print(student)
print(student["ankit"])
print(student["aman"]["age"])