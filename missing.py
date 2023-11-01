def findmissing(arr,N):
    temp=[0] * [N+1]
    for i in range(0,N):
        temp[arr[i] - 1] = 1
    for i in range(0,N+1):
        if (temp[i]==0):
            ans=i+1
if __name__ == '__main__':

    arr=[1,2,4,5]
    N=len(arr)
    findmissing(arr,N)
