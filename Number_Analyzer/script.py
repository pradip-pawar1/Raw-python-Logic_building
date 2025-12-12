import math

# Ask the user to enter a number:
num = int(input("Enter the number : "))

# Analyzer 1: Even/odd finder
def isEven(n:int):
    if n%2 ==0:
        return True
    else:
        return False

# Analyzer 2: Is prime or not finder
def isPrime(n:int):
    if n <= 1:
        print("No")
        return False
    else:
        is_prime = True # Flag variable (can be true)
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        return is_prime

# Analyzer 3: Perfect square finder
def perfect_square(n:int):
    if n < 0: # Negative numbers don't have perfect square
        return False
    
    # 0 and 1 are perfect square...
    if n <= 1:
        return True
    else:
        root = math.sqrt(n)
        if root == int(root):
            return True
        else:
            return False
        
# Analyzer 4: Check number is Armstrong or not
def armstrong(n:int):
    str_n = str(n)

    sum = 0
    power = len(str_n)
    
    for i in str_n:
        i = int(i)
        sum += i**power

    if sum == n:
        return True
    else:
        return False

# Analyzer 5: Reverse the number
def reverse(n:int):
    n = str(n)
    rev = n[::-1]
    return rev

# Analyzer 6: Reverse the number
def sum_digit(n:int):
    n = str(n)
    sum = 0

    for i in n:
        i = int(i)
        sum += i
    return sum

# Analyzer 8: Factorial calculation
def factorial(n:int) ->int:
    
        if not isinstance(n, int) or n<0 or n> 20:
            return f"Number not matches the conditions of factorial"
        
        # Handling base case: 0! = 1 & 1! = 1
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
             


f1 = isEven(num)
f2 = isPrime(num)
f3 = perfect_square(num)
f4 = armstrong(num)
f5 = reverse(num)
f6 = sum_digit(num)
f7 = lambda x: len(str(x)) # 
f8 = factorial(num)

final_report = {
    "Number is" : num,
    "The number is even": f1,
    "The number is Prime": f2,
    "The number have perfect square": f3,
    "The number is Armstrong": f4,
    "Reversed number": f5,
    "Sum of all didgits": f6,
    "Length of digits": f7(num),
    "Factorial of the number is": f8
}

print("\nFinal Report")
for i in final_report:
    print(f"{i} <=> {final_report[i]}")