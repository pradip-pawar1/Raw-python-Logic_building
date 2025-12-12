import math

# Ask the user to enter a number:

num = int(input("Enter the number : "))

# Analyzer 1: Even/odd finder
def isEven(n:int):
    if n%2 ==0:
        print(f'Number {n} is Even.')
        return True
    else:
        print(f'Number {n} is odd.')
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
                is_prime = False
                break
        print(f"Number {n} is {is_prime} prime number.")
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
        print(f"Calculated root: {root}")
        if root == int(root):
            return True
        else:
            return False
        


analyzer_1 = isEven(num)
analyzer_2 = isPrime(num)
analyzer_3 = perfect_square(num)


final_report = {
"Number is" : num,
"The number is even": analyzer_1,
"The number is Prime": analyzer_2,
"The number have perfect square": analyzer_3,

}

print("Final Report")
for i in final_report:
    print(f"{i} :=: {final_report[i]}")