def bitDestuffing(data):
    i=0
    count=0
  
    while i<len(data):
        if data[i]=='1':
            count+=1
        else:
            count=0
        
        if count==5 and i+1<len(data):
            if data[i+1]=='0':
                del data[i+1]
            count=0
        i+=1
    
data=list(input("Enter the bits: "))
print(len(data))
bitDestuffing(data=data)
print(len(data))
print("The data after bit de stuffing is: ", " ".join(data))