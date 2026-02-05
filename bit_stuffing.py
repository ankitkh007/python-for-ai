def bitstuffing(data):
    i=0
    count=0
    
    while i<len(data):
        if data[i]=='1':
            count+=1
        else:
            count=0
        
        if count==5:
            data.insert(i+1, '0')
            count=0
        i+=1
    
data=list(input("Enter the bits: "))
print(len(data))
bitstuffing(data=data)
print(len(data))
print("The data after bit stuffing is: ", "".join(data))