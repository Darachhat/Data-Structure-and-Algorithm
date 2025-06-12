array = [21,23,55,23,121,432,12,3,123,123]
n= len(array)-1

for i in range(n):
    for j in range(n-i):
        if array[j] >  array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
print("Sorted array is:", array)