## Sets are collections that only store unique values.
## They automatically remove duplicates.

empty_set=set()
print(type(empty_set)) #<class 'set'>

numbers={1,2,1,4,2,6}
print(set(numbers)) ## prints only unique numbers

names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
#unique_names=list(set(names))
print(list(set(names))) # ['Alice', 'Bob', 'Charlie']