def binary_search_recursion(array, value):
    if len(array) == 0:
        return -1
    else:
        mid = len(array) // 2
        if array[mid] == value:
            return mid
        else:
            if array[mid] < value:
                return binary_search_recursion(array[mid+1], value)
            else:
                return binary_search_recursion(array[mid-1], value)
            
def verify(index):
    if index == -1:
        print("Element not found in the array.")
    else:
        print(f"Element found at index: {index}")

arr = [1, 2, 3, 4, 5]
tar = 3
result = binary_search_recursion(arr, tar)
verify(result)