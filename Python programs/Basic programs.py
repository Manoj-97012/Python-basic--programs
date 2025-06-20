# basic programs
#Palindrome string
def is_palidrome(s):
    return s == s[::-1]

s = "MOM"
ans = is_palidrome(s)
if ans:
    print("it's is a palidrome")
else:
    print("it's not a palidrome")

# factorial program
num = 5
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(fact)

# Reverse string
def reverse_string(s):
    return s[::-1]

s = "Manoj"
reversed_s = reverse_string(s)
print("Reversed string:", reversed_s)

# swap number
a = 10
b = 20

a,b = b, a
print(a,b)

# check if odd or even
num = 4
if num % 2 == 0:
    print("even")
else:
    print("odd")

# prime or not

def is_prime(number):
    if number>1:
        for num in range(2, number):
            if number % num ==0:
                return "Not Prime"
            return "Prime"
        else:
            return "Not prime"
print(is_prime(3))
