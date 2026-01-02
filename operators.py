# Basic math
print(10 + 3)   
print(10 - 3)   
print(10 * 3)   
print(10 / 3)   

# Special operators
print(10 // 3)  
print(10 % 3)   
print(10 ** 3)  

#Logical Operators
age=18
has_license=False

can_drive=age>=18 and has_license
print(can_drive)

day="Sunday"
is_weekend=day=="Saturday" or day=="Sunday"
print(is_weekend)
print(not is_weekend)

##Truth Tables
# AND: Both must be True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# OR: At least one must be True  
print(True or False)    # True
print(False or False)   # False

# NOT: Flips the value
print(not True)         # False
print(not False)        # True


#age=age+5
age=18
age+=5
print(age)

k=20
k+=5; print(k)
k-=7; print(k)
k*=2; print(k)
k/=2; print(k)
