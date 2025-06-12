prev1= 0
prev2= 1

print("Fibonacci Series:")
print(prev1)
print(prev2)
for i in range(10):
    new_value = prev1 + prev2
    print(new_value)
    prev1 = prev2
    prev2 = new_value