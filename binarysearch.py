arr = [7, 5, 4, 6, 10, 13, 15, 18, 20]
num = int(input())
arr.sort()
print(arr)
low = 0
high = len(arr)-1
found = False
while low <= high:
    mid = (low+high)//2
    if arr[mid] == num:
        print("found: ", mid)
        found = True
        break
    elif num < arr[mid]:
        high = mid-1
    elif num > arr[mid]:
        low = mid+1
if not found:
    print("element not found")



