list=[]
print(type(list))

#accsessing single items form both sides
list=["Ankit","Aman",25,True,0.125]
print(list[3])
print(list[-2])
print(list[2])
print(list[-3])

#slicing
print(list[0:2]) #prints 0th and 1st
print(list[:3]) #prints from start(0)-2
print(list[2:]) #prints from 2-end(4)

fruits=["Apple", "Mango", "Banana"]
#changing any item
fruits[0]="Orange"
print(fruits)
fruits[0]="Apple"
print(fruits)

#Adding any item
fruits.append("grape") #add at end
print(fruits) 
fruits.insert(1,"Abcd") #add at a position
print(fruits)

#Removing elements
fruits.remove("Abcd")
print(fruits)
fruits.pop() #pops out last element from the list
del fruits[0] #del is an inbuilt function
print(fruits)

#List methods
numbers=[1,10,7,5,7,1,4]
print(len(numbers))
print(numbers[3])
print(numbers.index(7))
print(numbers.count(2))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

new_numbers=numbers.copy()
print(new_numbers)

print(fruits)

if "apple" in fruits:
    print("Found")
else:
    print("Not Found")

fruits.pop()
fruits.pop()

print(fruits)
fruits.append("Grapes")
if fruits:
    print("Has items")
else:
    print("Empty!")

print(fruits)
print(fruits[1]) #index out of bound

list1=[1,2,3,4]
list2=list1 ##both variables points to same list
list2.append(5) ##updated in both
print(list1, list2) 

list2=list1.copy() ## now list2 has a copy of list 1
list2.append(6)    ## so any cchanges made in either list
print(list1,list2) ## will not affect both