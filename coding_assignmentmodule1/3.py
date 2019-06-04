def binarysearch(arr,l,h,n):
	mid=(l+h)/2
	if arr[mid]==n:
		return mid
	elif arr[mid]>n:
		return binarysearch(arr,l,mid-1,n)
	else:
		return binarysearch(arr, mid+1, h, n) 

a=input("enter the comma separated elements")
li=a.split(",")
n=int(input("enter the element to be search"))
result=binarysearch(li,0,len(li)-1,n)
if result != -1: 
    print("Element is present at index ",result) 
else: 
    print("Element is not present in array")
