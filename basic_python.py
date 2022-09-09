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
