def decitobinary(n):
    if n>1:
        decitobinary(n//2)
    print(n % 2,end =' ') 
userin=34
decitobinary(userin)  
print()     
