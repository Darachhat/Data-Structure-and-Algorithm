def linear_seacrh(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return "Element not found"

def verify(index):
    if index == "Element not found":
        print("Element not found in the array.")
    else:
        print(f"Element found at index: {index}")

array = [1, 2, 3, 4, 5]
target = 3
result = linear_seacrh(array, target)
verify(result)