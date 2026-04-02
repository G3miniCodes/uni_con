def binary_search(arr, n, target):
    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Driver code
arr = [1, 3, 5, 7, 9, 11]
n = len(arr)
target = 7

result = binary_search(arr, n, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
