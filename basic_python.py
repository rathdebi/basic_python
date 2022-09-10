# program to check even or odd
def check_even_or_odd(num):
    if num is None or num == 0:
        return False
    elif num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


# program to check prime number
def check_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return "NO PRIME"
        else:
            return "PRIME"


# program for fibonacci series of n-sequence     
def fibonacci(n):
    if n <= 0:
        return "Incorrect Output"
    data = [0, 1]
    if n > 2:
        for i in range(2, n):
            data.append(data[i - 1] + data[i - 2])
    return data[n - 1]


input = int(input())
for i in range(0, input):
    print(fibonacci(i))

# given a name list return all names as its camelcase

import camelcase

csc = camelcase.CamelCase()
name_list = input("enter list of name separated by a space").split()
name_list_camel_case = [csc.hump(name) for name in name_list]
print(name_list_camel_case)

# create a database in mysql and fech all records from a table
# python-connectvity implementation of mysql

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",  # local host in case you are using a local machine
    user="root",  # give your own user name
    passwd="password123",  # give your own password
)

# to perform SQL operation - enable cursor
my_db_cursor = my_db.cursor()
# using cursor to create a database
my_db_cursor.execute("CREATE DATABASE my_db")
print("database is created")

my_db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
    database="my_db"  # from above
)
my_db_cursor = my_db_connection.cursor()
my_db_cursor.execute("CREATE TABLE SALES(sales_id INT AUTO_INCREMENT PRIMARY KEY,
product_code
VARCHAR(255),
price
INT(8))")

sales_query = "INSERT INTO SALES (sales_id, product_code, price) VALUES (111, 'HP-Server-001', 100000)"

my_db_cursor.execute(sales_query)
db_fetched_data = my_db_cursor.fetchall()  # can use selected rows as per need
print(db_fetched_data)


# reverse the given integer and print it back
def reverse_integer(str):
    return int(str[::-1])


reverse_integer(str(453))

# writing num2words interpretation in an appending mode
# by reading file with 123 in it.

from num2words import num2words

with open("num2words.txt", "r") as reader_file:
    content_read = reader_file.read()

with open("num2words.txt", "a") as writer_file:
    # write back the num to word interpretation
    for content in num2words(content_read):
        writer_file.write(content)
        
        
        
# string manipulation
# return engine number from a give a number plate
# engine no is sum of all digits present in number plate

def get_engine_no_from_num_plate(number_plate:str):
    """return engine number from a given number number_plate
      which is sum of all digits present in number_plate
      if not found then return False"""
    engine_num = 0
    for char in number_plate:
        if char.isdigit():
            engine_num+= int(char)
        else:
            pass
    return engine_num if engine_num > 0 else "no engine number"

number_plate = input("please enter your number plate")
get_engine_no_from_num_plate(number_plate)


# program for finding repeating or unique element
# from a given string

input_name = input()
result =[]
for char in input_name:
    if char not in result and input_name.count(char)==1:
        result.append(char)
print("".join(result))

from collections import Counter
def repeating_characters(name:str):
    """find repeating characters from a string"""
    counter_dict = Counter(name)
    result = list()
    for character,count in counter_dict.items():
        if count == 1:
            result.append(character)
        else:
            pass
    return "".join(result)

# given a string return wonder if it is consisting of 3 distinct characters
# else return -1
# for a given string "aabbcc" return "Wonder" , for "aabccddee" return -1

input_name = input()
result =[]
for char in input_name:
    if char not in result and input_name.count(char)>=1:
        result.append(char)
print("Wonder" if len(result)==3 else -1)

# using a function
from collections import Counter
def wonderful_string(name:str):
    """return "Wonderful" from a string of exactly 3 different characters
    else -1"""

    counter_dict = Counter(name)
    result = list()
    for character,count in counter_dict.items():
        if count >= 1:
            result.append(character)
        else:
            pass
    return "Wonder" if len(result)== 3 else -1


# given a string return "yes" if it contains vowels else return "no"
import re
input_string = input()
if re.search("a|e|i|o|u",input_string):
    print("yes")
else:
    print("no")
    
# given a input string replace the middle index element by * in conext
# of odd and even string len size.
name_string = input()
new_name_string = list(name_string)
if len(name_string)% 2 != 0 or len(name_string) == 1:
    middle_index = int(len(name_string)//2)
    new_name_string[middle_index] = "*"
    print("".join(new_name_string))
else:
    middle_index1,middle_index2 = len(name_string)//2- 1, len(name_string)//2
    new_name_string[middle_index1:middle_index2+1] = "**"
    print("".join(new_name_string))
    
# write a program that calculates miles per gallon
# from vehicle having miles driven before a refuel by 
# gallons of gas the tank holds.

from random import randint
def calculate_miles_per_gallons(gallons:int,miles:int):
  """approximates number of miles per gallon that a car gets"""
  return miles//gallons

gallons = randint(10, 25)
miles = randint(200, 400)
print("enter gallons of gas that fuel tank holds :"+str(gallons))
print("enter miles driven before a needing a refuel :"+str(miles))
print("miles per gallon calculated is "+ str(calculate_miles_per_gallons(gallons,miles)) +".")


# grade determiner to determine grades of class students
def determine_grade(score:int):
    """determine grade of students basis on marks via rules- 
    score >= 90 : grade A
    score >= 80 and score < 90 : grade B
    score >= 70 and score < 80 : grade C
    score >= 60 and score < 70 : grade D
    if any student do not fall in above rules then he/she will be failed"""
    if score >= 90:
        print("Grade A")
    elif score >= 80 and score < 90:
        print("Grade B")
    elif score >= 70 and score < 80:
        print("Grade C")
    elif score >= 60 and score < 70:
        print("Grade D")
    else:
        print("Grade F")

score = int(input("enter your score :"))
determine_grade(score)

# create roman numeral system from a given english numeral system from 1 to 10
# for example 9 can be represented as IX.

def convert_english_numeral_to_roman(one_to_ten:int):   
    """given a english numeral from 1 to 10 at random, convert the same to its roman 
    numeral representation. for instance romal numeral of 9 would be IX"""
    if one_to_ten == 1:
        print("The roman numeral equivalent of " + str(one_to_ten) + " is I.")
    elif one_to_ten == 2:
        print("The roman numeral equivalent of " + str(one_to_ten) + " is II.")
    elif one_to_ten == 3:
        print("The roman numeral equivalent of " + str(one_to_ten) + " is III.")
    elif one_to_ten == 4:
        print("The roman numeral equivalent of " + str(one_to_ten) + " is IV.")
    elif one_to_ten == 5:
        print("The roman numeral equivalent of " + str(one_to_ten) + " is V.")
    elif one_to_ten == 6:
        print("The roman numeral equivalent of " + str(one_to_ten) + " is VI.")
    elif one_to_ten == 7:
        print("The roman numeral equivalent of " + str(one_to_ten) + " is VII.")
    elif one_to_ten == 8:
        print("The roman numeral equivalent of " + str(one_to_ten) + " is VIII.")
    elif one_to_ten == 9:
        print("The roman numeral equivalent of " + str(one_to_ten) + " is IX.")
    else:
        print("The roman numeral equivalent of " + str(one_to_ten) + " is X.")
one_to_ten = randint(1, 10)
convert_english_numeral_to_roman(one_to_ten)



# while loop exercises

counter = 10
while counter <= 10:
    print(counter)
    counter -= 1
    if counter == 0:
        break

# another approach
counter = int(input("enter a number: "))
sum = 0
while counter != 0:
    sum += counter
    counter -= 1
print("total of sum: "+str(sum))


# for loop exercises

word_string = "hello world"
for letter in word_string:
    print(letter)

# find a total length of a given string

input_string = input("enter a string: ")
counter = 0
for letter in input_string:
    counter += 1

print(input_string)
print(counter)


# write a program that iterates over 1 to 50
# if numbers that are multiple of 3 and 5 print 3Buzz5
# if numbers that are multiple of 3 but not 5 print 3Buzz
# if numbers that are multiple of 5 but not 3 print 5Buzz
# for numbers tht are not a multiple of 3 or 5 print 3NoBuzzNo5

def multiple_of_3and5(range_int):
    """return designated outputs if a given number is multple of 3 and 5"""
    for num in range_int:
        if num % 3 == 0 and num % 5 == 0:
            print(num, "3Buzz5")
        elif num % 3 == 0 and num % 5 !=0:
            print(num, "3Buzz")
        elif num % 3 != 0 and num % 5 == 0:
            print(num, "5Buzz")
        else:
            print(num, "3NoBuzzNo5")
            
range_int = range(1,51)
multiple_of_3and5(range_int)


# given a number find its factorial
# to verify that function is working as intended
# an input of 3 would give 6, 4 would give 20 as output
# and so on.

def find_factorial_of_number(fact_number):
    
    """given a number find its factorial which is multiplication of 
    same number to 1. for instance factorial of 3 is 3*2*1=6"""
    factorial = 1
    for num in range(fact_number, 1, -1):
        factorial *= num
    return factorial if fact_number > 1 else 1

input_number = int(input("enter a number: "))
find_factorial_of_number(input_number)

# using recurssion also works

def fact_recurssion(fact_num):
    """factorial of a number using recurssion"""
    if fact_num == 0 or fact_num == 1:
        return 1
    if fact_num > 1:
        return fact_num * fact_recurssion(fact_num - 1)
    
fact_recurssion(5) # will print 120, test it
