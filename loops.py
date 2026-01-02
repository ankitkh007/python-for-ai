for i in range(5):
    print("hello")

for i in range(1,11): #starts from 1 goes till 11-1=10 ie n-1
    print(i)

for i in range(0,9,2):
    print(i)

name="Ankit"
for i in name:
    print(i)

k=1
list=["Ankit", 21, "Khanna", 0.25]
for content in list:
    print(f"This is content no. {k} : {content}")
    k+=1

x=5
while x>=1:
    print(x)
    x-=1