arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 1  # No. of rotations
i, j = 0, 0
 
print("Given array is")
for i in range(n):
    print(arr[i], end=" ")
 
# Reverse the first n-1 terms
for i, j in zip(range(0, (n-k)//2),
 range(n-k-1, (n-k)//2-1, -1)):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
 
# Reverse the entire array
for i, j in zip(range(0, n//2), range(n-1, n//2-1, -1)):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
 
print("\nRotated array is")
for i in range(n):
     print(arr[i], end=" ")