#input a two digit number and print the added digits

from turtle import st


two_digit_number = input("Enter your two digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
result = first_digit+second_digit
print(result)