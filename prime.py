def is_prime(number):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    return False

prime_numbers = []

for num in range(1, 100):
    if is_prime(num):
        prime_numbers.append(num)

print(prime_numbers)
