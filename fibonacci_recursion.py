prev1= 0
prev2 = 1
count = 2
print("Fibonacci Series:")
print(prev1)
print(prev2)

def fibonacci(prev1, prev2):
    global count 
    if count < 10:
        new_value = prev1 + prev2
        print(new_value)
        prev1 = prev2
        prev2 = new_value
        count += 1
        fibonacci(prev1, prev2)
    else:
        return
    
fibonacci(prev1, prev2)