
#Function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate 
result = gcd(num1, num2)
print("The GCD of",num1,"and", num2,"is", result)
