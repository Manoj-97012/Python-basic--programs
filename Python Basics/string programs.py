#Check if a string is a palindrome
from os import remove

str = input("Enter a string :")
r = str[::-1]
if r == str :
    print('it a  palidrome')
else:
    print('it not a palidrome')

# Check if a vowel is present in the string
def count_vowels_consantent(text):
    vowels = 'aeiouAEIOU'
    vowels_count = 0
    consantent_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consantent_count += 1

    print('vowels :', vowels_count)
    print('consantent :', consantent_count)


count_vowels_consantent('HelloWOrld')

#Create a function to reverse a given string

def reverse_string(s):
    return s[::-1]

s = "Manoj"
reversed_s = reverse_string(s)
print("Reversed string:", reversed_s)

#OR

#Reverse a string without using slicing
def reverse_string(s):
    reversed_ing=' '
    for char in s:
        reversed_ing=char+reversed_ing
    return reversed_ing

print(reverse_string("Manoj"))

#Given a list of words, concatenate them into a single string separated by space

List = ['Hello', 'Manoj', 'How','are', 'you' ]
result = " ".join(List)
print(result)

#Write a program that takes a sentence as input and counts the number of words in it

A = input('Enter a string :')
print(len(A))

#Implement a function that checks if a given string is a pangram (contains all letters of the alphabet)

#Will do later

#Given a string, write a function to remove all vowels from it and return the modified string

def Vowels_string(s):
    Vowels = 'aeiouAEIOU'
    result=''
    for char in s:
        if char not in Vowels:
            result += char # result = 'H' + 'l' = 'Hl'
    return result

print(Vowels_string('Helloworld'))

#create a function that takes a sentence as input and returns the sentence in reverse order
def string_senetence(s):
    words = s.split()
    return words==words[::-1]

print(string_senetence('s'))

# Given a list of names, count the number of names that  start with a vowel

def count_vowels(names):
    vowels = 'AEIOUaeiou'
    count = 0

    for name in names:
        if name and name[0] in vowels:
            count += 1
    return count

names_list = ["Almas", "Organge", "Manoj"]
print(count_vowels(names_list))

#Write a function to remove all duplicate characters from a given string

def remove_duplicates(S):
    seen = set()
    result = ' '

    for char in S:
        if char not in seen:
            seen.add(char)
            result +=char

print(remove_duplicates("programming"))




