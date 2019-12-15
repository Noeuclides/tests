# initializing string
test_str = "abcde"

# printing original string
print("The original string is : " + str(test_str))

# Get all substrings of string
# Using itertools.combinations()
res = [test_str[i: j] for i in range(len(test_str))
                 for j in range(i + 1, len(test_str) + 1)] 
print(set(res))
print(len(set(res)))

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+n 
