array = [3,4,1,5,112,2,6,7,8,9,10]
min_value = array[0]
for i in array:
    if i < min_value:
        min_value = i
print(f"The lowest value in the array is: {min_value}")