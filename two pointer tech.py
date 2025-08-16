def rev(arr):
    n=len(arr)
    l=0
    r=n-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr
print(rev([1,2,3,4]))
