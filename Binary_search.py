def bineary_search(array, value):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) //2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1
def verify(index):
    if index == -1:
        print("Element not found in the array.")
    else:
        print(f"Element found at index: {index}")

arr = [1, 2, 3, 4, 5]
tar = 3
result = bineary_search(arr, tar)
verify(result)