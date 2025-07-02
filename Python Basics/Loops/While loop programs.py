#Write a program that checks if a given number is positive, negative, or zero

number = int(input('Enter a number:'))

if number > 0:
  print('The postive number')
elif number < 0:
  print('The negative number')
else:
  print('The number is zero')


# create a loop print the 10 even number

for i in range(0, 21):
  if i % 2 == 0:
    print(i)


#Implement a program that finds the largest number in a list.
number_list = [20,30,99,20,40,89]

Largest = number_list[0]

for num in number_list:
  if num > Largest:
    Largest = num
  
  print(Largest)


# Create a program that takes a year as input and checks if it is a leap year or not

year = int(input('Enter a number :'))

if (year % 4 == 0 and year % 100 != 0)  or (year % 400 == 0):
  print('leap year')
else:
  print('not a leap year')


# Given a list of integers, find all the even numbers and store them in a new list
even_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i =1
for num in even_number:
  if num % 2 == 0:
    print(num)
    num = num +1


#Write a Python program to check if a given number is a prime number

def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(3))  # Output: True


# Create a program that generates the Fibonacci sequence up to a given number of terms


