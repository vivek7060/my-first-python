#arr[2 3 4 5 6 7]
def getminmex(arr):
    arr.sort()
    minmax={"min": arr[0],"max": arr[-1]}   
    return(minmax)

arr=[23,43,56,45,78,98,78]
minmax=getminmex(arr)

print("enter the min value",minmax["min"])
print("enter the value of mex",minmax["max"])
