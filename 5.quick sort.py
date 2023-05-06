def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[]
    right=[]
    for i in range(1,len(arr)):
        if arr[i]<pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left)+[pivot]+quick_sort(right)
mylist=[9,4,7,2,5,3,1,8,6]
sl=quick_sort(mylist)
print(sl)