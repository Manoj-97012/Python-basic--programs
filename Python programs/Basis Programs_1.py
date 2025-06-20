#Write a Python program to calculate the area of a  rectangle given its length and width

l = int(input("Enter a length :"))
b = int(input("Enter a breath :"))

area = l * b
print(area)


 # Create a program that takes a user's name and age as  input and prints a greeting message

username = input("Enter a name: ")
age = int(input("Enter an age: "))

print(f"Hello, my name is {username}, and I am {age} years old. Welcome!")

# Write a program to check if a number is even or odd

num = int(input("Enter a number :"))
if num % 2 == 0:
    print("Even")
else:
    print("odd")

#Given a list of numbers, find the maximum and minimum values

def find_max_min(numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    return max_value,min_value

numbers = [3,4,1,2,6]
max_value,min_value = find_max_min(numbers)
print(f"The maximum value is {max_value} !")
print(f"The minimum value is {min_value} !")


# Create a Python function to check if a given string is a palindrome
def is_palidrome():
    return s == s[::-1]
s = input('Enter a string')
ans = is_palidrome()
if ans:
    print('it a palidrome')
else:
    print('it not a palidrome')

# Implement a program that swaps the values of two variables.
num1 = int(input("Enter a first number :"))
num2 = int(input("Enter a second number :"))
print("Before swapping", num1)
print("Before swapping", num2)

num1,num2 = num2,num1
print("After swapping", num1)
print("After swapping", num2)

# Create a program that takes a sentence as input and counts the number of words in it
sentence = input('Enter a word :')
words = sentence.split()
word_count = len(words)
print('word_count')



