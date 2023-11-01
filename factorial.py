x=5
def fact(x):
    
    if x==0:
        return 1
    else:
        result=x*fact(x-1)
        return result

print(fact(x))