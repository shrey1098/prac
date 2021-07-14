def interpolationSearch(arr, lo, hi, x):
    if lo <= hi and arr[lo] <= x <= arr[hi]:
        pos = lo + (x - arr[lo]) *(hi - lo)//(arr[hi] - arr[lo])

        if arr[pos] == x:
            return pos
        if arr[pos] > x:
            return interpolationSearch(arr, lo, pos-1, x)
        if arr[pos] < x:
            return interpolationSearch(arr, pos+1, hi, x)

    return -1


arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)

# Element to be searched
x = 35
index = interpolationSearch(arr, 0, n - 1, x)

if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
