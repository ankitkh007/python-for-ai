## Tuple are immutable
## Tuples are like lists, but they can’t be changed once created. 
## They’re immutable (unchangeable) sequences.

tup=(3,5) ## ()--> this brackets means it is a tuple
print(type(tup)) #<class 'tuple'>

print(tup[0])

empty=()
single=(7,) ## needs comma for single item so that python thinks it's a tuple

point=(3,5)
colors=("red", "green", "blue")

print(colors[1])
print(colors[-1])

## Python's coolest tuple feature

point=(6,7)
x,y=point
print(x,y) ## 6 7

#Multiple assignment
a, b, c= 1, 2, 3

j,k=4,5
j,k=k,j ## Swap value! ##cool feature!!