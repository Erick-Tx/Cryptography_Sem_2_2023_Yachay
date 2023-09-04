
def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

# Find and print prime numbers up to 1000
for number in range(2, 1001):
    if is_prime(number):
        print(number, end=" ")

