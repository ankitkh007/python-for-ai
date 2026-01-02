def calculate():
    a=2
    b=3
    sum=a+b
    return sum

calculate()
    

def check_weather():
    temperature=31
    if temperature>=30:
        print("It's hot!")
    elif temperature<30 and temperature>=15:
        print("It's normal")
    else:
        print("It's cold")
    pass

check_weather()

##parameterized functions
def greet(name):
    print(f"Hello! {name}")
    pass

greet("Ankit")
greet("Aman")

def greeting(firstname, lastname):
    print(f"Hello! {firstname} {lastname}")
    pass

greeting("Ankit","Khanna")
greeting(lastname="Khanna", firstname="Ankit")

def simple_interest(principal,rate,time):
    si=(principal*rate*time)/100
    print(f"The Principal amount is: {principal}")
    print(f"The rate of interest is: {rate}")
    print(f"The duration(in years) is: {time}")
    print(f"The Simple Interest is: {si}")
    print(f"Amount after {time} years is: ", si+principal)
    pass

simple_interest(1550,7,2)
simple_interest(2500.25,6.5,3)

def database(name, age, city):
    print(f"{name}, {age} from {city}")
    pass

database("Ankit Khanna",25,"Kolkata")
database(city="Australia", age=37, name="Travis Head")

def area(length, breadth):
    return length*breadth

print(f"Area is: {area(5,7)}")
print("Area is: ", area(5,7))


def result(name):
    print (f"Hello! {name}")

get=result("Ankit")
print(get)


def min_max_numbers(numbers):
    return min(numbers), max(numbers)

print(min_max_numbers([1,2,3,4,10,99,-1]))

list=[100,125,0,5,999,-200]
print("Minimum and Maximum is: ",min_max_numbers(list))