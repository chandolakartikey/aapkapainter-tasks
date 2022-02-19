def dublicate(arr):
    arr1=sorted(arr)
    dublicateNo=None
    for i in range(len(arr1)-1):
        if arr1[i]==arr1[i+1]:
            dublicateNo=arr1[i]
            break
    if dublicateNo:
        print(dublicateNo)
    else:
        print("No dublicate number")

arr=[1,2,3,4,5,8,8]
dublicate(arr)