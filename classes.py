# class dog:
#     def __init__(self, name, breed):
#         self.name=name
#         self.breed=breed

# class cat:
#     def __init__(self, name, breed="None"):
#         self.name=name
#         self.breed=breed

# Tommy=dog(name="Tommy",breed="Laborador")
# Catty=cat(name="Catty")
# print(Tommy.name, Tommy.breed, Catty.name, Catty.breed)


# class APIConfig:
#     def __init__(self, api_key, model="gpt-3.5", max_tokens=100):
#         self.api_key=api_key
#         self.model=model
#         self.max_tokens=max_tokens
#         self.base_url="https://api.openai.com/v1"

# config1=APIConfig("key-1234",max_tokens=500)
# config2=APIConfig(api_key="key-7777", model="gpt-4.0", max_tokens=1000)

# print(config1.api_key, config1.model, config1.max_tokens, config1.base_url)
# print(config2.api_key, config2.model, config2.max_tokens, config2.base_url)


# -----------------------------------------------------------------------------------------------------------------------
##Adding behaviours or member methods in a class
# class DataValidator:
#     def __init__(self):
#         self.errors = []

#     def validate_email(self, email):
#         if "@" not in email:
#             self.errors.append(f"Invalid email: {email}")
#             return False
#         return True

#     def validate_age(self, age):
#         if age < 0 or age > 150:
#             self.errors.append(f"Invalid age: {age}")
#             return False
#         return True

#     def get_errors(self):
#         return self.errors

# # Use the validator
# validator = DataValidator()

# # Notice: we don't pass self, just the email
# validator.validate_email(email="bad-email")
# validator.validate_age(age=200)

# # Or using positional arguments
# validator.validate_email("another-bad-email")
# validator.validate_age(150)

# validator.validate_email("another-bad-@email")
# validator.validate_age(150)

# print(validator.get_errors())
# # ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']

# ----------------------------------------------------------------------------------------------------------------

## Inheritence
# Parent class - general animal
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         return f"{self.name} is eating"

#     def sleep(self):
#         return f"{self.name} is sleeping"

# # Child class - specific animal
# class Dog(Animal):
#     def bark(self):
#         return f"{self.name} says woof!"

# # Create a dog - using positional argument
# my_dog = Dog("Buddy")
# # Or with named argument
# my_dog2 = Dog(name="Max")

# # Dog can do animal things (inherited)
# print(my_dog.eat())    # Buddy is eating
# print(my_dog.sleep())  # Buddy is sleeping

# # Dog can also do dog things
# print(my_dog.bark())   # Buddy says woof!
# print(my_dog2.eat())
# print(Dog(name="Aman").eat(),Dog(name="Aman").bark())

# ---------------------------------------------------------------------------------


# class TextProcessor:
#     def __init__(self, text):
#         self.text = text

#     def clean_text(self):
#         self.text = self.text.strip().lower()
#         return self.text

#     def remove_punctuations(self):
#         self.text = self.text.replace(".", "").replace(",", "")
#         return self.text


# text = TextProcessor(text="  Hello!.Ankit.  ")
# print(text.clean_text())
# print(text.remove_punctuations())


class calculate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y


calculator = calculate(2, 5)
print(calculate.add())
print(calculate.sub())
print(calculate.mul())
