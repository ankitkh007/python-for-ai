full_name="Ankit Khanna"
age=21
print(f"My name is {full_name} and my age is {age}")

print(full_name.upper())
print(full_name.lower())
print(full_name.title())

str="  hello       "
print(str.strip())

price="$19.99"
print(price.strip("$"))

message = "I love Python programming with Python"

print("Python" in message)
print(message.startswith("P"), message.endswith("Python"))

print(message.find("Python"))
print(message.count("Python"))

new_message=message.replace("Python", "Annaconda")
print(new_message)

name=full_name.replace("Ankit", "Abcdef")
print(name)