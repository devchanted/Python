#primitive datatypes

#Strings
print("Hello"[0])

#Integers
print(123+345)
print(123_456_789)

#float

pi = 3.14
print("example of float: " +str(pi))

#how to find type

num_char = len(input("what's your name? "))
print(type(num_char))

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

#datatype conversion

a = float("3.125")
print(type(a))
print(70 + a)