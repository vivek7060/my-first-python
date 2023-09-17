def sort_list(number,order):
    if order=="asc":
        return sorted(number)
    elif order=="desc":
        return sorted(number,reverse=True)
    
        
    
    elif order=="none":
        return number
    else:
        print("invalid value")
my_list=[3,7,6,8,9,0,2,1,4]
my_list2=["ram","hare","kashnaya","gfwd","gedhgwd"]

ascending_result=sort_list(my_list,"asc")
print("ascending order",ascending_result)

descending_result=sort_list(my_list,"desc")
#my_list2.reverse()
print("decending order",descending_result)

alternative_result=sort_list(my_list,"none")
print("alternative_result",alternative_result)

