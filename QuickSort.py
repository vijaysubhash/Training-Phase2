def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left_arr = [i for i in arr[1:] if i <= pivot]
    right_arr = [i for i in arr[1:] if i > pivot]
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


arr = [30, 20, 50, 40, 10, 20]
print(arr)
res = quick_sort(arr)
print(res)
